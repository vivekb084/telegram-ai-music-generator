from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy.io.wavfile
import torch
import uuid
import os

app = FastAPI(title="Local MusicGen API")

print("Loading MusicGen model... (this may take a few minutes the first time)")
processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
print("Model loaded.")

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model.to(DEVICE)

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


class MusicRequest(BaseModel):
    prompt: str
    duration: int = 10


@app.post("/generate")
def generate(req: MusicRequest):

    # Prevent extremely long generations
    duration = max(1, min(req.duration, 30))

    inputs = processor(
        text=[req.prompt],
        padding=True,
        return_tensors="pt",
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    print(f"Generating: {req.prompt}")
    print(f"Duration: {duration}s")

    # Approximation: ~50 tokens ≈ 1 second
    max_new_tokens = duration * 50

    audio = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens
    )

    sample_rate = model.config.audio_encoder.sampling_rate

    filename = f"{uuid.uuid4()}.wav"
    filepath = os.path.join(OUTPUT_DIR, filename)

    scipy.io.wavfile.write(
        filepath,
        rate=sample_rate,
        data=audio[0, 0].cpu().numpy()
    )

    return {
        "success": True,
        "file": filename,
        "download_url": f"/download/{filename}"
    }


@app.get("/download/{filename}")
def download(filename: str):

    filepath = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(filepath):
        return {"error": "File not found"}

    return FileResponse(
        filepath,
        media_type="audio/wav",
        filename=filename,
    )
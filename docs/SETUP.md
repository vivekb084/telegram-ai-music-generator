# 🚀 Setup Guide

This guide walks you through setting up the Telegram AI Music Generator on your local machine.

## Prerequisites

Make sure you have the following installed:

- Python 3.11+
- Docker (optional, if running the API in Docker)
- n8n
- Ollama
- Telegram Account

---

# Step 1: Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

---

# Step 2: Start Ollama

Run:

```bash
ollama serve
```

The Ollama API will be available at:

```
http://localhost:11434
```

---

# Step 3: Start the MusicGen API

Navigate to your API directory.

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python app.py
```

The API should be available at:

```
http://localhost:8000
```

---

# Step 4: Create a Telegram Bot

1. Open Telegram.
2. Search for **@BotFather**.
3. Create a new bot using:

```
/newbot
```

4. Copy the bot token.

---

# Step 5: Configure n8n

Open n8n.

Import:

```
workflow/GenerateMusicFromText.json
```

Configure:

- Telegram Credentials
- Ollama Credentials

Update the HTTP Request node if your MusicGen API runs on a different host or port.

---

# Step 6: Activate the Workflow

Click **Activate**.

Send a message to your Telegram bot such as:

```
Generate relaxing piano music
```

The workflow will:

1. Receive the Telegram message.
2. Rewrite the prompt using Ollama.
3. Generate music using MusicGen.
4. Download the generated audio.
5. Send the audio back to Telegram.

---

# Troubleshooting

## Ollama not responding

Verify:

```bash
ollama list
```

and ensure the Ollama service is running.

---

## MusicGen API not reachable

Verify:

```
http://localhost:8000/docs
```

opens successfully.

---

## Telegram Bot doesn't respond

Check:

- Bot token
- n8n credentials
- Workflow is Active
- Telegram Trigger is connected

---

# Project Flow

```
Telegram User
        │
        ▼
Telegram Trigger
        │
        ▼
Ollama (Prompt Optimization)
        │
        ▼
Parse JSON
        │
        ▼
MusicGen API
        │
        ▼
Download Audio
        │
        ▼
Telegram Response
```
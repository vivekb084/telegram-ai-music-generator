# 🎵 Telegram AI Music Generator

Generate AI music directly from Telegram using **n8n**, **Ollama**, and **Facebook MusicGen**.

This project provides an end-to-end workflow that allows users to send a text prompt through Telegram, automatically optimize it with a local LLM, generate music locally, and receive the generated audio back in Telegram.

## ✨ Features

- 🎵 Generate music from natural language prompts
- 🤖 AI-powered prompt optimization using Ollama (Llama 3.2)
- ⏱ Automatic duration extraction from user prompts
- 💬 Telegram Bot integration
- 🎼 Local MusicGen API for music generation
- 📥 Automatic audio download
- 📤 Send generated audio directly back to Telegram
- 🔒 Fully local setup (No OpenAI API required)

---

## 🏗️ Workflow

```
Telegram User
      │
      ▼
Telegram Trigger
      │
      ▼
Ollama (Llama 3.2)
      │
      ▼
Parse JSON Response
      │
      ▼
MusicGen API
      │
      ▼
Download Generated Audio
      │
      ▼
Send Audio to Telegram
```

---

## 📁 Repository Structure

```
telegram-ai-music-generator/
│
├── workflow/
│   └── GenerateMusicFromText.json
│
├── screenshots/
│
├── docs/
│
├── api/
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🚀 Technologies Used

- n8n
- Ollama
- Llama 3.2
- Facebook MusicGen
- Python
- FastAPI
- Telegram Bot API

---

## 💡 Example Prompts

```
Generate relaxing piano music

Create 20 seconds of epic battle music

Happy ukulele background music

Meditation music with birds

Cyberpunk synthwave soundtrack
```
---


## 📸 Screenshots

### n8n Workflow

![Workflow](screenshots/workflow.png)

### Telegram Bot

![Telegram](screenshots/telegram-chat.png)

---

## 📦 Installation

1. Clone this repository.

```bash
git clone https://github.com/<YOUR_USERNAME>/telegram-ai-music-generator.git
```

2. Import the workflow from:

```
workflow/GenerateMusicFromText.json
```

3. Configure your Telegram credentials in n8n.

4. Start Ollama.

```bash
ollama run llama3.2
```

5. Start your MusicGen API.

6. Activate the workflow.

---

## 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

If you find this project useful, feel free to fork it and submit a pull request.

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
# ChatBot using PyTorch & Ollama

A **ChatGPT-style chatbot** built with **PyTorch** and **Ollama** for offline AI responses.  
This bot can answer both **predefined intents** (like greetings, items, payments) and **dynamic queries** (like weather, general questions) using a local LLM.

---

## Features

- **Hybrid Response System**:
  - **Supervised Intent Model**: Handles predefined intents and e-commerce queries.
  - **Local LLM (Ollama)**: Generates dynamic responses for any general question.
  
- **Offline AI**:
  - No API keys or external calls needed for Ollama models.
  - Works locally with lightweight models like `tinyllama`.

- **GUI**:
  - Modern **ChatGPT-style interface** using Tkinter.
  - Scrolled chat area, user input, and styled messages.

- **Expandable**:
  - Add more intents in `intents.json`.
  - Swap Ollama models for different sizes or capabilities.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/chatbot.git
cd chatbot
python train.py
python app.py

# Manoj AI

> A completely offline, modular, extensible AI assistant built in Python.

---

## Overview

Manoj AI is a local-first AI assistant designed to run entirely on your own computer without relying on cloud APIs.

Its long-term goal is to become a personal AI operating system capable of understanding natural language, managing files, assisting with programming, executing tasks, remembering information, and interacting with the user through voice.

Phase 0 focuses on building a stable AI core.

---

# Phase 0 Goals

- Local LLM
- Text Chat
- Configuration System
- Logging
- Prompt Management
- Modular Architecture

---

# Future Features

- Long-Term Memory
- Voice Recognition
- Text-to-Speech
- Coding Assistant
- File Management
- Plugin System
- Automation
- Vision
- Tool Calling
- Internet Search
- Multi-Agent System

---

# Project Structure

```
ManojAI/
│
├── main.py
│
├── app/
│
├── config/
│
├── llm/
│
├── chat/
│
├── system/
│
├── models/
│
├── logs/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Requirements

- Python 3.10+
- CUDA (Recommended)
- NVIDIA GPU (Optional)
- llama-cpp-python

---

# Installation

Create Virtual Environment

```bash
python -m venv Manoj
```

Activate

Windows

```powershell
.\Manoj\Scripts\activate
```

Linux

```bash
source Manoj/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Models

Place all GGUF models inside

```
models/base/
```

Example

```
models/base/Qwen3-4B-Instruct-Q4_K_M.gguf
```

Future LoRAs

```
models/loras/
```

---

# Coding Standards

- Python 3.10+
- Type Hints
- Google Style Docstrings
- PEP8
- Modular Design
- Single Responsibility Principle

---

# Architecture Principles

- No circular imports
- No hardcoded paths
- Configuration driven
- Offline first
- GPU acceleration when available
- Easy to extend
- Easy to test

---

# Current Phase

Phase 0

Status

🚧 In Development

---

# License

Private Development Project

Copyright © Darshan
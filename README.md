# Q-A-Chatbot-Using-Open-Source-LLM-s-using-Langchain-And-Ollama

## Overview
This project is an **end-to-end Question & Answer Chatbot** built using **LangChain** and **Ollama**, powered entirely by **open-source Large Language Models (LLMs).**
It allows users to ask natural language questions based on their own documents and receive context-aware, accurate responses.

Unlike cloud-based models like OpenAI, this chatbot runs locally using **Ollama**, offering both **privacy** and **cost-efficiency.**

## Features
- Uses open-source LLMs (via Ollama) instead of paid APIs
- Powered by **LangChain** for prompt orchestration and document retrieval
- Custom embeddings for semantic search
- Streamlit-based chat interface for interactive use
- Local execution — your data never leaves your system


## Tech Stack
- **Python 3.10**
- **LangChain** - for chaining and retrieval logic
- **Ollama** - for running open-source LLMs locally (here llama2 model is used)
- **Streamlit** - for frontend UI
- **PyPDF2 / LangChain DocumentLoaders** – for file processing


## Installation

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Chinmayee7697/Q-A-Chatbot-Using-Open-Source-LLM-s-using-Langchain-And-Ollama.git

cd Q-A-Chatbot-Using-Open-Source-LLM-s-using-Langchain-And-Ollama
```

### 2️⃣ Create and Activate Virtual Environment
```bash
conda create -p venv python==3.10

conda activate ./venv
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install and Run Ollama
- Download Ollama: [https://ollama.ai/download](https://ollama.ai/download)
- Pull a model (example: Mistral, LLaMA2, or any supported one):
```bash
ollama pull llama2
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

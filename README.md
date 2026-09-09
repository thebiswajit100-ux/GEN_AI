🤖 CustomChatBot — LangChain + Streamlit

A simple and customizable AI chatbot application built using LangChain and Streamlit. 
The application allows users to interact with an LLM through a clean web interface and provides a foundation for building more advanced Generative AI applications.

📌 Project Overview

CustomChatBot is a conversational AI application that uses:

LangChain — Framework for developing LLM-powered applications
OpenAI / LLM — Provides natural-language understanding and generation
Streamlit — Creates the interactive web application
Python — Core programming language
Environment Variables — Securely manages API credentials

**High-Level Architecture**

                    ┌──────────────────────┐
                    │       User           │
                    │  Enter Chat Message  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │     Web Interface    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      LangChain       │
                    │ Prompt + LLM Chain   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       LLM            │
                    │ OpenAI / Other LLM   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Generated Answer  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Streamlit       │
                    │   Display Response   │
                    └──────────────────────┘

🛠️ **Technologies Used**
- Technology	Purpose
- Python	Programming language
- LangChain	LLM application framework
- OpenAI	LLM provider
- Streamlit	Web UI

📈 **Future Enhancements**

The current chatbot can be extended with several Generative AI capabilities.

1. Conversation Memory

Store previous messages so that the chatbot can maintain context.

User
 ↓
Question
 ↓
Memory
 ↓
LLM
 ↓
Response
 ↓
Memory

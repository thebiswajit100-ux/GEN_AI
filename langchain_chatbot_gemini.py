from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain.chat_models import ChatOpenAI

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6JOrVWDafFtYrwrBzq13vAYUIm_akTmOMfVGLt7PMvVMQ"
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Langmith tracking
os.environ["LANGSMITH_TRACING_V2"]="true"

os.environ["LANGSMITH_API_KEY"]= "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"
#os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('GEMINI 2.5 FLASH CHATBOT - POWERED BY LANGSMITH (by Biswajit)')
input_text=st.text_input("How may I help you")

# openAI LLm
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",   # ✅ Correct model name
    temperature=0,
)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
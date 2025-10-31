from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## environment variables call

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langsmith tracing
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## creating chatbot

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries."),
        ("user","Question:{question}")
    ]
)

# streamlit framework
st.set_page_config(page_title="My App", layout="wide")

st.markdown("""
    <style>
        .navbar {
            background-color:#19195d;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: white;
            font-size: 18px;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;
            text-align: center;
            padding: 8px;
            font-size: 14px;
            color: #555;
        }
    </style>

    <div class="navbar">
        <div><b>AI ChatBot</b></div>
        <div>
            <a href="https://github.com/Chinmayee7697/">Visit my Github</a>
            <a href="https://www.langchain.com/">Langchain</a>
            <a href="https://ollama.com/">Ollama</a>
        </div>
    </div>
""", unsafe_allow_html=True)

st.title("Q&A Chatbot Using Open Source LLM's using Langchain And Ollama")
input_text=st.text_input("Search the topic you want")

st.markdown("""
    <footer>
        © 2025 Chatbot | Made with ❤️ by Chinmayee
    </footer>
""", unsafe_allow_html=True)


# open AI LLM call
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

## chain
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



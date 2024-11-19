from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
import streamlit as sl

template = "You are a helpful assistant. Answer the following question: {question}"
prompt = PromptTemplate(template=template, input_variables=["question"])
llm = Ollama(model="llama3.2:latest", base_url="http://localhost:11434")

sl.title("Local Ollama LLM")
question = sl.text_input("Ask me a question:")

outpur_parser = StrOutputParser()
chain = prompt | llm | outpur_parser

if question:
    sl.write(chain.invoke({"question": question}))

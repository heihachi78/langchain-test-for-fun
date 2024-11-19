from langchain.prompts import PromptTemplate
from localollamallm import LocalOllamaLLM

# Initialize the local Ollama language model with the API URL and model name
local_ollama_llm = LocalOllamaLLM(api_url="http://localhost:11434", model_name="llama3.2:latest")

# Define a prompt template
template = "You are a helpful assistant. Answer the following question: {question}"
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create a chain object
chain = prompt | local_ollama_llm

# Get user input and generate response
question = input("Ask me a question: ")
response = chain.invoke({"question": question})
print(response)

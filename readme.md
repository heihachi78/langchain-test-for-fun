# prerequisites
## Ollama
installed olama(https://ollama.com/) on localhost http://localhost:11434 with llama3.2:latest model

# steps to run

## create a virtual environment in python
python3 -m venv .venv

## switch to that virtual environment
source .venv/bin/activate

## install requirements
pip install -r requirements.txt

## run the project
streamlit run main.py
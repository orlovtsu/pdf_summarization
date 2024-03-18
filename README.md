# PDF Summarizer
This project is a Streamlit application that summarizes the content of PDF files using natural language processing (NLP) techniques.  

It utilizes the LangChain library and the OpenAI GPT-3.5 model for generating summaries.   

This application requires OpenAI API key. Summarization will be charged by OpenAI in accordance with their prices for API requests.  

## Features

- Upload a PDF file and get a concise summary of its content.
- The summary focuses on key facts and is typically 5-7 sentences long.
- The application uses a character-based text splitter for chunking the text.
- Embeddings are generated using the sentence-transformers/all-MiniLM-L6-v2 model.
- The summaries are generated using the GPT-3.5 model with a temperature setting of 0 for deterministic outputs.

## Installation

### Recommended way
To set up the project using `Docker`, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/orlovtsu/pdf_summarization.git
```
2. Navigate to the project directory and run:
```bash
docker compose build --no-cache
docker compose up
```
Once the docker is built and app is running, you can access it in your web browser at http://localhost:8501

### Alternative way
To set up project using streamlit, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/orlovtsu/pdf_summarization.git
```

2. Navigate to the project directory and install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Start the application using
```bash
streamlit run app.py
```
Once the application is running, you can access it in your web browser at http://localhost:8501

## Usage 

1. To run the application you will need your own OpenAI API Key:
- Register account at https://openai.com
- Create new secret key at https://platform.openai.com/api-keys
- Copy your key into the clipboard. The format of key is `sk-<48_hash_symbols>`

2. Once you have OpenAI key in the clipboard, paste it into the field "Enter your unique key:"
3. Send `Submit`
4. Click `Browse files` and select your PDF file
5. Once the file is uploaded click "Summarize PDF" and wait for a several seconds.

After the response you will see a summarized response and information about your query and cost of it.
>Tokens Used: 1924 Prompt Tokens: 1800 Completion Tokens: 124 Successful Requests: 1 Total Cost (USD): $0.005896

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.


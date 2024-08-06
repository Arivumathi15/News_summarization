# Web Content Search, Scrape, and Summarize Application

## Overview

This a Flask-api designed to automate the process of searching, scraping, and summarizing web content. This system leverages AI and specialized tools to provide a seamless experience for obtaining concise summaries of web content based on user queries.

## Key Features

### Search Functionality

- **Tool Used**: Tavily Search
- **Function**: Performs web searches based on user input.
- **Output**: Extracts and returns URLs relevant to the user's search query.

### Scrape Functionality

- **Tool Used**: FirecrawlApp
- **Function**: Scrapes the main content of the web pages identified in the search results.
- **Output**: Compiles the raw data from these web pages for further processing.

### Summarize Functionality

- **Tool Used**: OpenAI's GPT-4 model
- **Function**: Summarizes the compiled raw data.
- **Output**: Provides a concise summary of the content extracted from multiple web pages.

## Workflow and Endpoints

Three main endpoints in the Flask application to handle these functionalities:

### 1. Search Endpoint (`/search`)

- **Purpose**: Perform a web search based on user input and return the URLs of relevant web pages.
- **Method**: POST
- **Input**: JSON object containing the search query.
- **Output**: JSON array of URLs.

### 2. Scrape Endpoint (`/scrape`)

- **Purpose**: Perform a web search, scrape the content from the resulting URLs, and return the combined raw data.
- **Method**: POST
- **Input**: JSON object containing the search query.
- **Output**: Combined raw data from the scraped web pages.

### 3. Summarize Endpoint (`/summarize`)

- **Purpose**: Perform a web search, scrape the content from the resulting URLs, and return a summarized version of the combined raw data.
- **Method**: POST
- **Input**: JSON object containing the search query.
- **Output**: Summarized content.

## Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd your-repository
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add your API keys:

    ```ini
    OPENAI_API_KEY=your_openai_api_key
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    TAVILY_API_KEY = your_tavily_api_key
    ```

5. **Run the Application**

    ```bash
    python app.py
    ```

6. **Access the Endpoints**

    - **Search**: `POST /search` with JSON body `{ "content": "search query" }`
    - **Scrape**: `POST /scrape` with JSON body `{ "content": "search query" }`
    - **Summarize**: `POST /summarize` with JSON body `{ "content": "search query" }`


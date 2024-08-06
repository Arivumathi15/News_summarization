from firecrawl import FirecrawlApp
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json 
import pandas as pd 
from datetime import datetime
from langchain_community.tools.tavily_search import TavilySearchResults

# Function to perform a web search based on user content
def web_search(user_content):
    load_dotenv()  # Load environment variables from a .env file
    web_search_tool = TavilySearchResults(max_results=2)  # Initialize the search tool with a limit of 2 results
    web_search_results = web_search_tool.run(user_content)  # Perform the search with the given content
    
    # Extract URLs from the search results
    urls = [result['url'] for result in web_search_results]
    return urls  # Return the list of URLs

# Function to scrape data from a given URL
def scrape_data(url):
    load_dotenv()  # Load environment variables from a .env file
    app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))  # Initialize the FirecrawlApp with the API key
    
    # Scrape the URL, focusing on the main content of the page
    scraped_data = app.scrape_url(url, {'pageOptions': {'onlyMainContent': True}})
    
    # Check if 'markdown' key exists in the scraped data and return it
    if 'markdown' in scraped_data:
        return scraped_data['markdown']
    else:
        # Raise an error if 'markdown' key is not found
        raise KeyError("The key 'markdown' does not exist in the scraped data.")

# Function to summarize given data using OpenAI's API
def summarize_data(data):
    load_dotenv()  # Load environment variables from a .env file
    api_key = os.getenv('OPENAI_API_KEY')  # Retrieve the OpenAI API key from environment variables
    
    # Define the headers for the OpenAI API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the system message content for summarization
    system_message = """You are an intelligent summarization assistant. You are an expert in distilling comprehensive news 
                        articles into concise summaries.Your role involves analyzing and summarizing news content to highlight 
                        key points and important information. You have a strong background in understanding current events and 
                        translating complex information into easily digestible formats."""

    # Define the user message content with the data to be summarized
    user_message = f"Content:\n\n{data}"

    # Define the payload for the POST request to the OpenAI API
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    }

    # Send the POST request to the OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # Check if the response is successful
    if response.status_code == 200:
        # Convert the response to a Python dictionary
        output = response.json()
        
        # Extract the summarized content
        summarized_content = output['choices'][0]['message']['content']
        return summarized_content  # Return the summarized content
    else:
        # Return None if the request was not successful
        return None

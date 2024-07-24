# Import the necessary modules from Flask and the custom NewsAnalysis class
from flask import Flask, request, jsonify
from utils import NewsAnalysis

# Initialize the Flask application
app = Flask(__name__)

# Define the route for scraping data from the given URL
@app.route('/', methods=['POST'])
def data():
    # Get the JSON data from the request
    data = request.json
    # Extract the URL from the request data
    url = data.get('url')

    # If a URL is provided
    if url:
        # Create an instance of NewsAnalysis with the provided URL
        news_instance = NewsAnalysis(url=url)
        # Return the scraped data as a JSON response
        return jsonify({"Scraped_data": news_instance.scraped_data})
    else:
        # Return an error response if the URL is not provided
        return jsonify({"error": "URL is required."}), 400

# Define the route for summarizing the news content
@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the JSON data from the request
    data = request.json
    # Extract the URL from the request data
    url = data.get('url')
    
    # If no URL is provided, return an error response
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # Create an instance of NewsAnalysis with the provided URL
    news_instance = NewsAnalysis(url=url)

    # If news_instance is created and scraped_data is available
    if news_instance and news_instance.scraped_data:   
        # Generate a summary of the news content
        news_summary = news_instance.summary(action='summarize', scraped_data=news_instance.scraped_data)
        # Return the news summary as a JSON response
        return jsonify({"summary": news_summary})
    else:
        # Return an error response if scraped data is not available
        return jsonify({"error": "Scraped data is not available."}), 400

# Define the route for answering specific questions about the news content
@app.route('/qna', methods=['POST'])
def qna():
    # Get the JSON data from the request
    data = request.json
    # Extract the URL and question from the request data
    url = data.get('url')
    question = data.get('question')
    
    # If either URL or question is not provided, return an error response
    if not url or not question:
        return jsonify({"error": "URL and question are required"}), 400
    
    # Create an instance of NewsAnalysis with the provided URL
    news_instance = NewsAnalysis(url=url)

    # Generate an answer to the question based on the scraped news data
    answer = news_instance.qna(action='qna', question=question, scraped_data=news_instance.scraped_data)
    # Return the answer as a JSON response
    return jsonify({"answer": answer})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

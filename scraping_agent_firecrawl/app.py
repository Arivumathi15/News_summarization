from flask import Flask, request, jsonify
from functions import web_search, scrape_data, summarize_data

app = Flask(__name__)

# Route for performing a web search based on user content
@app.route('/search', methods=['POST'])
def search():
    data = request.json  # Get JSON data from the POST request
    content = data.get('content', '')  # Extract the 'content' field from the JSON data
    urls = web_search(content)  # Perform the web search
    return jsonify(urls)  # Return the search URLs as JSON

# Route for scraping data from URLs obtained via search
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json  # Get JSON data from the POST request
    content = data.get('content', '')  # Extract the 'content' field from the JSON data
    try:
        urls = web_search(content)  # Perform the web search to get URLs
        combined_raw_data = ""  # Initialize an empty string to hold combined raw data
        for url in urls:
            raw_data = scrape_data(url)  # Scrape data from each URL
            combined_raw_data += raw_data + "\n"  # Append the scraped data to combined_raw_data
        return jsonify(combined_raw_data)  # Return the combined raw data as JSON
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error message if an exception occurs

# Route for summarizing data from URLs obtained via search and scrape
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json  # Get JSON data from the POST request
    content = data.get('content', '')  # Extract the 'content' field from the JSON data
    try:
        urls = web_search(content)  # Perform the web search to get URLs
        combined_raw_data = ""  # Initialize an empty string to hold combined raw data
        for url in urls:
            raw_data = scrape_data(url)  # Scrape data from each URL
            combined_raw_data += raw_data + "\n"  # Append the scraped data to combined_raw_data
        summary = summarize_data(combined_raw_data)  # Summarize the combined raw data
        return summary  # Return the summary as a plain text response
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return an error message if an exception occurs

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

#the input should be like this --> {"content": "I need more about the latest news in Singapore"}
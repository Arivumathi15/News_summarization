# Import the NewsAnalysis class from the utils module
from utils import NewsAnalysis

if __name__ == "__main__":
    # Prompt the user to input the URL of the news website
    url = input("Copy paste your news website URL here: ")
    
    # Create an instance of the NewsAnalysis class with the provided URL
    news_instance = NewsAnalysis(url=url)
    
    # If a URL was provided, scrape the data from the website
    if url:
        scraped_data = news_instance.scraped_data
    
    # Prompt the user to choose an action
    user_action = input("Type which you want (summarize/qna/exit): ")

    # If the user chooses to summarize, process the scraped data
    if user_action == 'summarize':
        if scraped_data:
            # Generate a summary of the news content
            news_summary = news_instance.summary(action='summarize', scraped_data=scraped_data)
            print("News Summary:")
            print(news_summary)
        else:
            # Inform the user that scraped data is not available
            print("Scraped data is not there.")

    # Loop to keep asking the user for input until they choose to exit
    while True:
        # Prompt the user to choose an action
        user_action = input("Type which you want (summarize/qna/exit): ")   

        # If the user chooses to ask a question, process the question based on the scraped data
        if user_action == 'qna':        
            if scraped_data:
                # Prompt the user to enter a question about the news
                question = input("Enter your question about the news: ")
                # Get an answer to the question based on the news content
                answer = news_instance.qna(action='qna', scraped_data=scraped_data, question=question)
                print("Answer:")
                print(answer)
            else:
                # Inform the user that scraped data is not available
                print("Scraped data is not there.")
        
        # If the user chooses to exit, break the loop and end the program
        elif user_action == 'exit':
            print("Exiting the program.")
            break
        
        # Handle invalid inputs
        else:
            print("Invalid input. Please type 'summarize', 'qna', or 'exit'.")

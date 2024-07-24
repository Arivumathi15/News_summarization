# Import the Streamlit library and the custom NewsAnalysis class
import streamlit as st
from utils import NewsAnalysis

# Streamlit app setup
st.title("News Summarization and Q&A App")  # Set the title of the app

# URL input
url = st.text_input("Enter the URL of the news article")  # Create a text input for the user to enter the URL

# Initialize NewsAnalysis object
if url:
    # Create an instance of NewsAnalysis with the provided URL
    news_instance = NewsAnalysis(url)
    
    # Display the scraped data (optional)
    if st.checkbox("Show scraped data"):
        st.write(news_instance.scraped_data)  # Display the scraped data if the checkbox is checked

    # Summarization
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):  # Show a spinner while summarizing
            # Generate a summary of the news content
            news_summary = news_instance.summary(action='summarize', scraped_data=news_instance.scraped_data)
        st.subheader("Summary")  # Display a subheader for the summary section
        st.write(news_summary)  

    # Q&A
    question = st.text_input("Ask a question about the news article")  # Create a text input for the user to enter a question
    if st.button("Get Answer"):
        if question:
            with st.spinner("Fetching answer..."):  # Show a spinner while fetching the answer
                # Get an answer to the question based on the news content
                answer = news_instance.qna(action='qna', scraped_data=news_instance.scraped_data, question=question)
            st.subheader("Answer")  # Display a subheader for the answer section
            st.write(answer)  # Show the answer
        else:
            st.error("Please enter a question")  
else:
    st.info("Please enter a URL to start") 

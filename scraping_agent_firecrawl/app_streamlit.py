import streamlit as st
from functions import web_search, scrape_data, summarize_data

# Streamlit app layout
st.title("Web Content Summarizer")

# User input for content search
content = st.text_input("Enter content to search:", "")

if st.button("Search"):
    if content:
        urls = web_search(content)
        st.write("Search URLs:")
        st.write(urls)
    else:
        st.write("Please enter content to search.")

if st.button("Scrape"):
    if content:
        try:
            urls = web_search(content)
            combined_raw_data = ""
            for url in urls:
                raw_data = scrape_data(url)
                combined_raw_data += raw_data + "\n"
            st.write("Combined Raw Data:")
            st.write(combined_raw_data)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.write("Please enter content to search.")

if st.button("Summarize"):
    if content:
        try:
            urls = web_search(content)
            combined_raw_data = ""
            for url in urls:
                raw_data = scrape_data(url)
                combined_raw_data += raw_data + "\n"
            summary = summarize_data(combined_raw_data)
            st.write("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.write("Please enter content to search.")

#run command --> streamlit run app_streamlit.py
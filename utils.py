import os
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, TXTSearchTool, RagTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Language Model Initialization
# 'llm' is an instance of 'ChatOpenAI' with the model 'gpt-4o' and a temperature setting of 0.7.
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)

"""
Class "NewsAnalysis":
    '__init__' Method:
        - Initializes with a URL and scrapes the website content using 'ScrapeWebsiteTool'.
        - Sets up two agents:
            - 'self.text_summarizer': For summarizing news content using 'RagTool'.
            - 'self.qna_agent': For answering specific questions based on the news content using 'TXTSearchTool'.
"""

class NewsAnalysis:
    def __init__(self, url):
        # Store the provided URL
        self.url = url

        # Initialize the web scraping tool with the given URL
        web_scrape_tool = ScrapeWebsiteTool(website_url=url)
        # Run the tool to get the scraped data
        self.scraped_data = web_scrape_tool.run()

        # Initialize RagTool for summarization
        rag_tool = RagTool()
        # Create an agent for summarizing news content
        self.text_summarizer = Agent(
            role="News Summarization Specialist",
            goal="Summarize the latest news content efficiently",
            backstory="""You are an expert in distilling comprehensive news articles into concise summaries.
            Your role involves analyzing and summarizing news content to highlight key points and important information.
            You have a strong background in understanding current events and translating complex information into easily digestible formats.""",
            verbose=False,
            allow_delegation=False,
            tools=[rag_tool],
            llm=llm
        )

        # Initialize TXTSearchTool for Q&A
        qna_tool = TXTSearchTool()
        # Create an agent for answering questions about the news content
        self.qna_agent = Agent(
            role="News Q&A Specialist",
            goal="Answer specific questions based on the latest news content accurately",
            backstory="""You are an expert in providing precise and informative answers to questions about news articles.
            Your role involves thoroughly understanding news content and extracting relevant information to respond to inquiries.
            You have a keen ability to interpret and analyze current events, ensuring that your answers are both accurate and insightful.""",
            verbose=False,
            allow_delegation=False,
            tools=[qna_tool],
            llm=llm
        )

    """
    'summary' Method:
        - Uses the 'Crew' class to summarize the scraped news data. 
        - Defines a task with the description and expected output format, then executes it.
    """
    def summary(self, action, scraped_data):
        if action == 'summarize':
            # Create a Crew instance with the text summarizer agent
            crew = Crew(
                agents=[self.text_summarizer],
                tasks=[Task(
                    description="""Summarize the extracted news content, using scraped data {scraped_data} and 
                    Provide a suitable heading and extract the key points in bullet points format.""",
                    expected_output=""" Heading: Give suitable heading to this news

                                        Date: Date of this news posted  

                                        Summary: summary of the this whole extracted data """,
                    agent=self.text_summarizer
                )],
                verbose=1
            )

            # Start the Crew instance to get the text summary
            text_summary = crew.kickoff(inputs={'scraped_data': scraped_data})
            return str(text_summary)
        
    """
    'qna' Method:
        - Uses the 'Crew' class to provide answers to specific questions about the news content.
        - Defines a task with the question and expected output format, then executes it.
    """
    def qna(self, action, scraped_data, question):
        if action == "qna":
            # Create a Crew instance with the Q&A agent
            crew = Crew(
                agents=[self.qna_agent],
                tasks=[Task(
                    description="""Answer specific questions based on the extracted news content {scraped_data}.
                    Provide accurate answers to the questions asked.""",
                    expected_output="accurate answers to the {question}",
                    agent=self.qna_agent
                )],
                verbose=1
            )

            # Start the Crew instance to get the answer to the question
            qna = crew.kickoff(inputs={'question': question, 'scraped_data': scraped_data})
            return str(qna)

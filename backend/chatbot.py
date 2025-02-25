from langchain_openai import OpenAI

from langchain_experimental.agents import create_pandas_dataframe_agent
from backend.data_loader import load_titanic_data
from backend.visualization import generate_visualization
import os
from dotenv import load_dotenv, find_dotenv
import time
import openai


# Load Titanic data
df = load_titanic_data()


# Load .env file
backend_path = os.path.dirname(os.path.abspath(__file__))

env_path = os.path.join(backend_path, ".env")

load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please check your .env file.")

print(f"API Key Loaded: {api_key[:5]}********")  


llm = OpenAI(openai_api_key=api_key)
agent = create_pandas_dataframe_agent(llm, df, allow_dangerous_code=True)


def extract_chart_type_and_data(question):
    """Uses LLM to extract chart type and relevant dataset column from user query."""
    chart_keywords = ["bar chart", "pie chart", "histogram", "scatter plot", "line chart"]
    
    llm_response = agent.run(f"Extract the chart type (if any) and the data column needed from this query: {question}")
    
    # Find if any known chart type is mentioned in the query
    chart_type = None
    for keyword in chart_keywords:
        if keyword in question.lower():
            chart_type = keyword.replace(" chart", "")
            break

    # Extract relevant data column from LLM response
    column_name = None
    for col in df.columns:
        if col.lower() in llm_response.lower():
            column_name = col
            break

    return chart_type, column_name


def safe_openai_call(agent, question, retries=3):
    for attempt in range(retries):
        try:
            return agent.invoke(question)
        except openai.RateLimitError:
            wait_time = 2 ** attempt 
            print(f"Rate limited. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    return "Error: Too many requests. Try again later."




def process_query(question):
    """Handles user query, determines visualization dynamically, and returns both text + chart."""
    response_text = safe_openai_call(agent, question)

    chart_type, column_name = extract_chart_type_and_data(question)

    image_path = None
    if chart_type and column_name:
        image_path = generate_visualization(chart_type, column_name)

    return response_text, image_path

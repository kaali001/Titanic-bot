from fastapi import FastAPI, Query
from backend.chatbot import process_query
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Welcome to Titanic Chatbot!"}

@app.get("/query")
async def query_titanic(question: str = Query(..., description="Your question")):
    """Handles Titanic dataset queries and visualizations."""
    try:
        response_text, image_path = process_query(question)
        return {"response": response_text, "image": image_path}
    except Exception as e:
        logging.error(f"Error processing query: {str(e)}")
        return {"error": str(e)}

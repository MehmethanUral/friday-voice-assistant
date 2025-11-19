# serper_utils.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

HEADERS = {
    "X-API-KEY": "66a61efb4ebfc473d8ee10457417a6894bf0125d",
    "Content-Type": "application/json"
}

API_URL = "https://google.serper.dev/search"

def ask_serper(query):
    data = {"q": query}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        if response.status_code == 200:
            results = response.json()
            if "answerBox" in results and "answer" in results["answerBox"]:
                return results["answerBox"]["answer"]
            elif "organic" in results and len(results["organic"]) > 0:
                return results["organic"][0].get("snippet", "Sorry, I couldn't find anything useful.")
            else:
                return "I couldn't find any relevant information."
        else:
            return f"Serper API error: {response.status_code}"
    except Exception as e:
        return f"An error occurred while searching: {e}"

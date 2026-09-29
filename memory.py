import os
from pathlib import Path
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("HINDSIGHT_API_KEY", "")

# Fix accidental duplicate prefix
if api_key.startswith("hsk_hsk_"):
    api_key = api_key[4:]

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=api_key,
)

BANK_ID = "meeting-memory"

# Local fallback memory for demo when Hindsight credits are unavailable
local_memories = []


def store_memory(meeting_text):
    local_memories.append(meeting_text)

    try:
        return client.retain(
            bank_id=BANK_ID,
            content=meeting_text
        )
    except Exception:
        return {"status": "stored_locally"}


def recall_memory(query):
    # Try Hindsight first
    try:
        result = client.recall(
            bank_id=BANK_ID,
            query=query
        )
        return result
    except Exception:
        # Demo fallback
        if local_memories:
            return local_memories[-1]

        return "No meeting memory found."
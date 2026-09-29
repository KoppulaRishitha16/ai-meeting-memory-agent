import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv(".env")

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=os.getenv("HINDSIGHT_API_KEY"),
)

result = client.recall(
    bank_id="meeting-memory",
    query="What does ABC Corp need?"
)

print(result)
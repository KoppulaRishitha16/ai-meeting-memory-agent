import os
from dotenv import load_dotenv
from hindsight_client import Hindsight

load_dotenv()

client = Hindsight(
    base_url=os.getenv("HINDSIGHT_API_URL"),
    api_key=os.getenv("HINDSIGHT_API_KEY"),
)

client.retain(
    bank_id=os.getenv("HINDSIGHT_BANK_ID"),
    content="""
    Meeting with ABC Corp.
    They need an analytics dashboard by Friday.
    They prefer email communication.
    """
)

print("Meeting memory stored successfully!")
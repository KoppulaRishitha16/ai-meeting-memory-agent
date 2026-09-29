# AI Meeting Memory & Follow-up Agent

An AI-powered meeting assistant that remembers important meeting details and uses them to create personalized follow-up messages.

## Problem

Important meeting details such as customer requirements, deadlines, communication preferences, and commitments can easily be forgotten after a meeting.

## Solution

This project provides a meeting memory assistant that:

- Stores meeting notes
- Recalls relevant meeting information
- Retrieves important commitments and preferences
- Generates a personalized follow-up email

## How It Works

1. Enter meeting notes.
2. Store the meeting information in memory.
3. Ask a question about the previous meeting.
4. Recall the relevant information.
5. Generate a personalized follow-up email.

## Example

### Meeting Memory

> I met with ABC Corp. They need an analytics dashboard by Friday. They prefer email communication.

### Recall

**Question:** What does ABC Corp need?

**Memory:** ABC Corp needs an analytics dashboard by Friday and prefers email communication.

### Follow-up

The agent generates a personalized email using the recalled meeting information.

## Technology

- Python
- Streamlit
- Hindsight
- Hindsight Python Client
- LLM-ready architecture

## Hindsight Integration

Hindsight is used as the memory layer for storing and recalling meeting information. The application is designed around the retain → recall workflow so that previous meeting context can be used in later interactions.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

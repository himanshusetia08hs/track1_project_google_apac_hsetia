
# # Essential libraries/ methods 
import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

# # ADK methods/ functions
from google.adk.agents.llm_agent import Agent

# # --- Setup Logging and Environment ---
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

# --- Prompt Optimizer Agent ---
root_agent = Agent(
    model=model_name,
    name='prompt_optimizer_agent',
    description='Analyzes user prompts and provides a high-quality, refined version.',
    instruction="""
    You are a Prompt Engineer and Hygiene Specialist. Your goal is to analyze the user's input and rewrite it into a high-quality prompt.

    For every input, you MUST return a response in this exact format:

    LABEL: [Clear / Ambiguous / Incomplete / Unsafe]
    
    REFINED PROMPT: [Rewrite the user's input into a professional, clear, and detailed prompt. If the input is 'Unsafe', state: 'Cannot refine due to safety policy.']

    Logic:
    1. If the input is 'Incomplete' (e.g., "python code"), the REFINED PROMPT should expand it into a useful request (e.g., "Write a clean, documented Python script to solve [X] problem").
    2. If the input is 'Ambiguous' (e.g., "make it better"), assume a general helpful context and rewrite it clearly.
    3. If the input is 'Clear', the REFINED PROMPT should still polish it for even better results from an AI.

    Do not answer the user's question. Only provide the Label and the Refined Prompt.
    """,
)
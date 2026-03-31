
## **🛡️ Prompt Hygiene & Optimization Agent**

Built with Google ADK & Gemini 1.5 Flash

This "AI Gatekeeper" addresses the "Garbage-In, Garbage-Out" issue. It functions as an initial layer that analyzes text, assesses its quality (Hygiene Labeling), and automatically converts unclear intent into professionally crafted prompts.

------------------------------------------------

**🧠 Automated Flow**

- The agent uses a structured 5-Step Flow to clean and refine AI inputs:
- User Input: Accepts unclear or "imperfect" prompts (e.g., "write math lesson").
- Cloud Run Endpoint: Receives the request and activates the ADK logic.
- Gemini Reasoning: Determines the intent and produces a detailed, improved version.
- Structured Output: Provides a clear LABEL and the REFINED PROMPT.
- Downstream Use: The output is ready for use by a primary LLM or an automated API system.

------------------------------------------------

**🛠️ Technical Features**

- Intent Classification: Labels prompts as Clear, Ambiguous, Incomplete, or Unsafe.
- Automated Refinement: Uses Gemini to rewrite prompts with professional context and structure.
- Security Guardrails: Identifies harmful inputs and prevents refinement to maintain safety standards.
- Scalable Infrastructure: Hosted on Google Cloud Run using a custom service account for secure, serverless execution.

------------------------------------------------

📁 Repository Structure

├── agent.py          # Core Agent logic using google-adk

├── requirements.txt  # Dependencies (google-adk, python-dotenv, etc.)

├── README.md         # Project documentation

└── .env.example      # Template for environment variables

------------------------------------------------

**⚙️ Local Development**

1. Prerequisites
- Python 3.10+
- Google Cloud SDK (gcloud) authenticated with gcloud auth application-default login

2. Setup & Run
- Install ADK: pip install google-adk python-dotenv
- Run locally: adk run .

------------------------------------------------

------------------------------------------------

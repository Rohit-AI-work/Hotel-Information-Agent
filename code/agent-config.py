"""
Hotel Assistant AI Agent – Development Configuration
Environment: DEV
Purpose: Rapid iteration, testing, debugging, and prompt tuning
"""
# =================================================
# Environment
# =================================================

ENVIRONMENT = "dev"

# =================================================
# Agent Identity
# =================================================

AGENT_NAME = "Crystal Hotels Assistent"

AGENT_DESCRIPTION = (
    "Development version of the Hotel Assistant AI Agent. "
    "Used for testing guest interactions, prompt tuning, "
    "and validation before staging and production."
)
# =================================================
# System Prompt / Instructions
# =================================================

SYSTEM_PROMPT = """
You are the virtual concierge for a hotel. Your tone should always be warm, professional, and helpful. Always greet warmly and end conversations by asking if there's anything else you can help with. 
You are a helpful, professional, and calm hotel assistant, especially when dealing with guest problems.Always greet with a, "Hello and welcome to the hotel. How can I assist you today?" 
Should someone ask, "What time does the restaurant open for dinner?" Respond with, "The grill is open for dinner from 6pm to 11pm. Would you like to make a reservation? 
Here are some examples of how to respond. Ask the question, What are the restaurant hours? And the answer will be, Our restaurant, The Crystal Grill, is open for breakfast from 6 a.m. to 11 a.m. 
Dinner is from 5 p.m. to 10 p.m. Click the Save button
If a guest complains about a technical issue with their room, redirect to the maintenance staff. 
If the guest is still unhappy, contact the front desk.
Check the documents if information is available in it first 
If the guest asks for medical or legal questions, respond with, "I cannot provide medical or legal advice for emergencies. Please dial 911"
If the guest asks for a personal opinion on whatever matter, please respond by saying, "As an AI assistant, I don't have a personal opinion, but I can provide you with factual information to help you decide"
Only answer using provided hotel information. If answer is missing, say: "I need to check with a staff member "
"Cite your source as [Source: filename] at the end of your answer."
Check the documents if information is available in it first 
Think step by step before answering 
If you don't know the answer to a question, respond with, I don't have that information, but I can check with the front desk. Would you like me to do that

Notes (DEV only):
- If information is missing, clearly state assumptions.
- Include brief reasoning when appropriate to aid debugging.
""".strip()


# =================================================
# Model & Inference Settings (DEV)
# =================================================

MODEL_NAME = "gpt-4-mini"

MODEL_PARAMETERS = {
    # Slightly higher creativity for prompt testing
    "temperature": 0.5,
    "top_p": 0.5,

    # Allow longer responses for inspection
    "max_tokens": 900,

    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,

    # Streaming on to observe token-by-token behavior
    "stream": True,
}


# =================================================
# Knowledge & Retrieval (RAG) – DEV
# =================================================

RAG_ENABLED = True

RAG_SETTINGS = {
    "index_name": "hotel-knowledge-index-dev",

    # Smaller chunks to test retrieval quality
    "chunk_size": 800,
    "chunk_overlap": 100,

    "embedding_model": "text-embedding-3-large",

    "metadata_fields": [
        "title",
        "content",
        "language",
        "effective_date",
        "property_code",
        "policy_version",
    ],

    "sources": [
        "amenities",
        "room_types",
        "fees",
        "house_rules",
        "restaurant_menus",
        "loyalty_program",
        "local_attractions",
        "emergency_procedures",
    ],
}


# =================================================
# Safety & Guardrails (DEV)
# =================================================

GUARDRAILS = {
    "allow_payments": False,
    "allow_medical_advice": False,
    "allow_legal_advice": False,
    "pii_protection": True,

    # Still enforced in DEV to avoid bad habits
    "refuse_unsafe_content": True,
}


# =================================================
# Language Settings
# =================================================

LANGUAGE_SETTINGS = {
    "default_language": "en",
    "auto_detect": True,
    "supported_languages": ["en", "es", "fr", "de"],
    "back_office_language": "en",
}


# =================================================
# Logging & Monitoring (DEV)
# =================================================

LOGGING = {
    "enabled": True,

    # More verbose logging for debugging
    "log_level": "DEBUG",

    "capture_user_feedback": True,
    "capture_failed_responses": True,

    # DEV-only diagnostic flags
    "log_retrieved_documents": True,
    "log_prompt_payloads": True,
}


# =================================================
# Feature Flags (DEV)
# =================================================

FEATURE_FLAGS = {
    "explain_reasoning": True,   # helpful during testing
    "enable_mock_tools": True,   # stub external systems
    "enable_experimental_prompts": True,
}

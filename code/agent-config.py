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

AGENT_NAME = "Hotel Assistant – Crystal Hotels (DEV)"

AGENT_DESCRIPTION = (
    "Development version of the Hotel Assistant AI Agent. "
    "Used for testing guest interactions, prompt tuning, "
    "and validation before staging and production."
)


# =================================================
# System Prompt / Instructions
# =================================================

SYSTEM_PROMPT = """
You are Crystal Hotels’ virtual concierge (development environment).

Your goals:
- Be helpful, friendly, and accurate.
- Prioritize guest safety, privacy, and correctness.
- Use only approved hotel knowledge when answering questions.

Rules:
- Always verify identity for booking lookups or changes
  (last name + confirmation code or approved verification).
- Never disclose room numbers or personal data.
- Never accept payments directly.
  Route payment requests to the secure checkout URL.
- Be proactive but concise.
- Offer next best actions and summarize confirmations.
- For operational requests (extra towels, late checkout),
  create a service ticket with priority and ETA,
  then confirm back to the guest.
- Detect the user’s language and respond in that language.
  For critical confirmations, include an English summary
  prefixed with "Back office:".
- If content is unsafe, ambiguous, or out of policy,
  refuse politely and suggest a safe alternative.

Notes (DEV only):
- If information is missing, clearly state assumptions.
- Include brief reasoning when appropriate to aid debugging.
""".strip()


# =================================================
# Model & Inference Settings (DEV)
# =================================================

MODEL_NAME = "gpt-5-mini"

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

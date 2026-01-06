#Hotel Information Agent

An AI-powered hotel information assistant designed to answer common guest questions accurately and professionally. This project demonstrates the use of Azure AI Foundry to build, test, and validate a domain-focused conversational agent with clear boundaries and reliable behavior.

Overview

The Hotel Information Agent acts as a virtual hotel concierge, helping guests quickly access essential information such as amenities, restaurant hours, and checkout times. The agent is designed with a focus on accuracy, friendliness, and trustworthiness, making it suitable for real-world customer-facing use.

Key Features
	•	Answers questions about hotel amenities
	•	Provides restaurant hours and dining information
	•	Responds to check-out time and stay-related inquiries
	•	Maintains a polite, welcoming concierge tone
	•	Avoids guessing and respects defined knowledge boundaries

Architecture and Technologies
	•	Model: gpt-4-mini
	•	Agent Instructions:
You are a helpful hotel concierge attending to guest inquiries and concerns. Be polite, welcoming, and professional, and provide accurate information based on approved hotel knowledge.

Demonstration
The agent was tested using realistic guest scenarios, including:
	•	Asking about hotel amenities (e.g., pool, Wi-Fi, fitness center)
	•	Checking restaurant opening and closing hours
	•	Confirming check-out times
	•	Handling unclear or out-of-scope questions by politely deferring to hotel staff

Testing was performed using the Azure AI Foundry Playground, ensuring that responses:
	•	Matched the uploaded hotel documentation
	•	Followed the defined concierge tone
	•	Avoided hallucinations or unsupported claims

This validation process helped confirm that the agent behaves reliably in common, real-world guest interactions.

Lessons Learned
	•	Prompt engineering matters: Clear, specific instructions significantly improve tone consistency and response accuracy.
	•	Define boundaries early: Explicitly limiting what the agent can and cannot answer reduces risk and builds trust.
	•	Testing is critical: Functional, edge-case, and safety testing help catch issues before launch.
	•	Accuracy over creativity: In hospitality use cases, reliable information is more important than expressive language.
	•	User trust is earned: Consistent, correct answers encourage guests to rely on the agent confidently.

Future Improvements
	•	Add multilingual support for international guests
	•	Integrate live data sources (e.g., restaurant availability)
	•	Expand agent personas (family advisor, local guide, business traveler)
	•	Implement monitoring and feedback loops for continuous improvement

Conclusion

This project demonstrates how a focused, well-tested AI agent can deliver real value in a hospitality setting. By combining clear instructions, structured testing, and thoughtful design, the Hotel Information Agent serves as a strong foundation for production-ready conversational AI systems.

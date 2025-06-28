# 🌐 Language Translator Agent

A GenAI Agent that translates text between:
- English -> Hindi
- English -> German

Built for the [GenAI AgentOS Hackathon](https://github.com/genai-works-org/genai-agentos)

---

## 💡 Features

- Idiomatic, natural translation (not literal)
- Fast, local execution using HuggingFace Transformers
- AgentOS-compatible (`agent.yaml` included)

---

## 🛠️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/aaryanpawar16/language-translator-agent.git
   cd language-translator-agent
2.Install dependencies:
pip install -r requirements.txt

3.Run agent:
../genai-agentos/agentos run .

4.Test API:
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Good morning", "source_lang": "en", "target_lang": "hi"}'

## 🔗 Live Agent (Bonus)

This agent is live and accessible via ngrok:

**Endpoint**:  
`https://0e72-2401-4900-57c7-911b-b064-1a28-d020-9029.ngrok-free.app/translate`

You can test it using a `POST` request with JSON payload:
```json
{
  "text": "I love learning new languages.",
  "source_lang": "en",
  "target_lang": "de"
}

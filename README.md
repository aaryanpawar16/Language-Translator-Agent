# 🌐 Language Translator Agent

A GenAI Agent that translates text between:
- English → Hindi
- English → German

Built for the [GenAI AgentOS Hackathon](https://github.com/genai-works-org/genai-agentos)

---

## 💡 Features

- Idiomatic, natural translation (not literal)
- Fast, local execution using HuggingFace Transformers
- AgentOS-compatible (`agent.yaml` included)

---

## 🛠️ How to Run

1. **Clone this repo**:
   ```bash
   git clone https://github.com/aaryanpawar16/language-translator-agent.git
   cd language-translator-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the agent**:
   ```bash
   ../genai-agentos/agentos run .
   ```

4. **Test the API**:
   ```bash
   curl -X POST http://localhost:5000/translate \
     -H "Content-Type: application/json" \
     -d "{\"text\": \"Good morning\", \"source_lang\": \"en\", \"target_lang\": \"hi\"}"
   ```

---

## 🔗 Live Agent (Bonus)

This agent is live and accessible via ngrok:

**Endpoint**:  
```
https://e72e-2401-4900-57cc-5dfb-ed0b-8c61-4d2c-6276.ngrok-free.app/translate
```

### Example Request:
```json
{
  "text": "I love learning new languages.",
  "source_lang": "en",
  "target_lang": "de"
}
```

---

## 🎥 Watch a Demo Video

[![Demo Video](https://img.youtube.com/vi/6ndFi3hqTNA/0.jpg)](https://youtu.be/6ndFi3hqTNA)

> Click the thumbnail to watch the 2-minute demo.

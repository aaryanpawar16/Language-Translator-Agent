from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)

MODEL_MAP = {
    "en-hi": "Helsinki-NLP/opus-mt-en-hi",
    "en-de": "Helsinki-NLP/opus-mt-en-de"
}

tokenizers = {}
models = {}

for lang_pair, model_name in MODEL_MAP.items():
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    tokenizers[lang_pair] = tokenizer
    models[lang_pair] = model

IDIOM_MAP = {
    "under the weather": "sick",
    "break a leg": "good luck",
    "hit the sack": "go to sleep",
    "spill the beans": "reveal the secret",
    "once in a blue moon": "very rarely",
    "piece of cake": "very easy",
    "costs an arm and a leg": "very expensive",
    "let the cat out of the bag": "reveal the secret",
    "feeling blue": "feeling sad",
    "kick the bucket": "die",
    "beat around the bush": "avoid the point",
    "the ball is in your court": "it's your decision",
    "add fuel to the fire": "make things worse",
    "barking up the wrong tree": "blaming the wrong person",
    "cry over spilled milk": "regret something that's already done",
    "call it a day": "stop working",
    "cut to the chase": "get to the point",
    "get a taste of your own medicine": "receive the same bad treatment",
    "give someone the cold shoulder": "ignore someone",
    "hit the nail on the head": "be exactly right",
    "in hot water": "in trouble",
    "let sleeping dogs lie": "avoid restarting old conflicts",
    "pulling your leg": "joking",
    "see eye to eye": "agree",
    "sit on the fence": "not decide",
    "speak of the devil": "someone just mentioned appears",
    "take it with a grain of salt": "not take seriously",
    "throw in the towel": "give up",
    "up in the air": "uncertain",
    "burning the midnight oil": "working late",
    "raining cats and dogs": "raining heavily",
    "bite the bullet": "endure pain or hardship",
    "bend over backwards": "make extra effort",
    "by the skin of your teeth": "barely",
    "get cold feet": "become nervous",
    "hit the books": "start studying",
    "go the extra mile": "put in more effort",
    "in the blink of an eye": "very quickly",
    "jump the gun": "act too early",
    "miss the boat": "miss an opportunity",
    "on thin ice": "in a risky situation",
    "pull yourself together": "calm down",
    "the best of both worlds": "benefits of two different things",
    "throw someone under the bus": "betray someone",
    "your guess is as good as mine": "I don't know either",
    "cut corners": "do something badly to save time or money",
    "hit the road": "leave",
    "the last straw": "final limit",
    "walking on air": "very happy",
    "not playing with a full deck": "crazy",
    "run out of steam": "lose energy"
}

def replace_idioms(text):
    lowered = text.lower()
    for idiom, replacement in IDIOM_MAP.items():
        if idiom in lowered:
            text = text.replace(idiom, replacement)
    return text

@app.route('/')
def home():
    return "✅ Language Translator Agent is running!"

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get("text")
    source = data.get("source_lang")
    target = data.get("target_lang")

    lang_pair = f"{source}-{target}"

    if lang_pair not in models:
        return jsonify({"error": f"Translation for {lang_pair} not supported."}), 400

    preprocessed_text = replace_idioms(text)

    tokenizer = tokenizers[lang_pair]
    model = models[lang_pair]

    inputs = tokenizer(preprocessed_text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    output = tokenizer.decode(translated[0], skip_special_tokens=True)

    return jsonify({"translated_text": output})

@app.route("/api/agents/register", methods=["POST"])
def register_agent():
    data = request.json
    print(f"📥 Received agent registration: {data}")
    return jsonify({
        "id": data.get("id"),
        "name": data.get("name"),
        "description": data.get("description")
    }), 200
@app.route("/api/agents/<agent_id>", methods=["GET"])
def get_agent(agent_id):
    return jsonify({
        "agent_id": agent_id,
        "agent_name": "language-translator",
        "agent_description": "Translate English to Hindi and German with idiomatic awareness",
        "input_parameters": {}
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
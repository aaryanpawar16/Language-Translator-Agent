import requests

print("Language Translator")
print("Choose an option:")
print("1. English to Hindi")
print("2. English to German")

choice = input("Enter your choice (1 or 2): ").strip()
text = input("Enter the English text to translate: ").strip()

if choice == '1':
    source = "en"
    target = "hi"
elif choice == '2':
    source = "en"
    target = "de"
else:
    print("Invalid choice.")
    exit()

payload = {
    "text": text,
    "source_lang": source,
    "target_lang": target
}

try:
    response = requests.post("http://localhost:5000/translate", json=payload)
    result = response.json()

    if 'translated_text' in result:
        print("✅ Translated Text:", result["translated_text"])
    else:
        print("❌ Error:", result.get("error", "Unknown error"))

except Exception as e:
    print("❌ Failed to connect to the translation server:", e)

from openai import OpenAI
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import references as ref

TOPIC = "Wie man AI ready als Start Up wird"

PROMPT = f"""
Generiere eine ausführliche, SEO-optimierte informative Seite (Long-Form Content) 
im Plain-Text-Format für das Thema {TOPIC}.

Die Seite soll für meinen Blog https://www.create-dot.com/marketing-blog erstellt werden.

Hier sind aktuelle Seiten als Beispiel:
{ref.get_blog_pages()}
"""

def generate_text_gemini(prompt):
    print("Generating text ...")
    load_dotenv()
    api_keys = os.environ.get('GEMINI_API_KEY')

    with open("instructions.txt", "r") as f:
        system_instructions = f.read()


    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instructions),
        contents=prompt
    )

    print(response.text)

    return response.text


def generate_text_openai(prompt):
    print("Generating text ...")

    load_dotenv()
    api_keys = os.environ.get('OPENAI_API_KEY')

    with open("instructions.txt", "r") as f:
        system_instructions = f.read()


    client = OpenAI()

    response = client.responses.create(
        model="o4-mini",
        input=prompt + system_instructions
    )

    print(response.output_text)

    return response.output_text


def save_text(topic, text):
    print("Saving text ...")
    topic = topic.lower().replace(" ", "_")

    page_name = f"SEO Page/{topic}.txt"
    page_counter = 0

    while True:
        if not os.path.exists(page_name):
            with open(page_name, "w") as f:
                f.write(text)
            break
        else:
            page_counter += 1
            page_name = f"SEO Page/{topic}_{page_counter}.txt"


def main():
    text = generate_text_gemini(TOPIC)
    save_text(TOPIC, text)


if __name__ == "__main__":
    main()
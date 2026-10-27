import json
from pathlib import Path
from llm import client, MODEL

# Session 5: Load saved conversation history
CHAT_FILE = Path(__file__).with_name("chat.json")

if CHAT_FILE.exists():
    with CHAT_FILE.open("r", encoding="utf-8") as file:
        history = json.load(file)
else:
    history = []

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "quit":
        # Save conversation history before quitting
        with CHAT_FILE.open("w", encoding="utf-8") as file:
            json.dump(history, file, indent=2, ensure_ascii=False)

        print("Conversation saved to chat.json")
        break

    history.append({"role": "user", "content": user_input})

    # Session 4: Stream the reply
    stream = client.chat.completions.create(
        model=MODEL,
        max_tokens=500,
        messages=history,
        temperature=0,
        stream=True,
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": False
            }
        },
    )

    print("Bot: ", end="", flush=True)
    reply = ""

    for chunk in stream:
        if not chunk.choices:
            continue

        piece = chunk.choices[0].delta.content or ""
        print(piece, end="", flush=True)
        reply += piece

    print()

    if reply:
        history.append({"role": "assistant", "content": reply})
    else:
        print("No answer text was received.")
        history.pop()


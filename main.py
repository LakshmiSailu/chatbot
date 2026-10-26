
from llm import client, MODEL

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "Reply with exactly: Hello!"}
    ],
    max_tokens=512,
    temperature=0,
    extra_body={
        "chat_template_kwargs": {
            "enable_thinking": False
        }
    },
)

message = response.choices[0].message
print("Model:", MODEL)
print("Finish reason:", response.choices[0].finish_reason)
print("Answer:", repr(message.content))


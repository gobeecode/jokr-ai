import ollama


class Joker:

    def __init__(self, model: str = 'llama3.2', topic: str = 'any'):
        self.model = model
        self.topic = topic

    def get_joke_messages(self):
        system_prompt = ("You are an assistant that is capable of telling a humorous joke on any topic. "
                         "Just reply with the joke. Don't add any additional text in the beginning or end of the joke.")
        user_prompt = f"Tell a creative joke on {self.topic}."
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return messages

    def tell_a_joke(self):
        messages = self.get_joke_messages()
        print(f"Please wait...")
        response = ollama.chat(model=self.model, messages=messages, stream=True)
        for chunk in response:
            content = chunk.get("message", {}).get("content", "")
            print(content, end='', flush=True)


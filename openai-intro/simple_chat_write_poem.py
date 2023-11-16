from openai import OpenAI
import dotenv

dotenv.load_dotenv()

if __name__ == '__main__':
    client = OpenAI()

    resp = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages=[
            {
                'role': 'system',
                'content': 'You are a poetic assistant, skilled in explaining programming concepts with creative '
                           'flairs.'
            },
            {
                'role': 'user',
                'content': 'Compose a poem that explains the concept of recursion in programming'
            }
        ]
    )

    print(resp.choices[0].message.content)
    print(resp.usage)
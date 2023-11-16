from openai import OpenAI
import dotenv

dotenv.load_dotenv()

if __name__ == '__main__':
    client = OpenAI()

    resp = client.chat.completions.create(
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant'
            },
            {
                'role': 'user',
                'content': 'Who won the World Cup in 2018?'
            },
            {
                'role': 'assistant',
                'content': 'France won the World Cup in 2018'
            },
            {
                'role': 'user',
                'content': 'Which Asian countries participated in?'
            }
        ],
        model='gpt-4'
    )

    print(f'Response: {resp.choices[0].message.content}')
    print(f'Total usage: {resp.usage}')
from openai import OpenAI
import dotenv

dotenv.load_dotenv()


if __name__ == '__main__':
    client = OpenAI()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': 'say hello in japanese'
            }
        ],
        # model='gpt-3.5-turbo'
        model='gpt-4'
    )

    print(chat_completion.choices[0].message.content)

import os
import openai
openai.api_key = os.getenv("OPENAI_KEY") 
openai.api_key = 'your api key' 
    

messages = [
    {"role": "system", "content": "You are a kind helpful Mental Health assistant Chat Bot. You should strictly give answers only to Mental Health releated Queries and if the given content can't be answered then say I don't know "},
]

print("Your new assistant is ready!")

def click(question):
   while input != "quit()":
        message = question
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        #print("\n" + "Chat Bot: "+ reply + "\n")
        return reply
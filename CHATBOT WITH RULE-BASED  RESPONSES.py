import re
import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you( doing)?', ["I'm just a program, but I'm here to help you out with the problems feel free to ask any!"]),
    (r'what is your name?', ['I am a simple chatbot created to assist you.']),
    (r'bye|exit', ['Goodbye! Have a great day!']),
    (r'(.*) your name(.*)', ['My name is Alex and I am a Chatbot.']),
    (r'(.*) help (.*)', ['How can I assist you?']),
    (r'(.*) weather (.*)', ['I am not sure about the weather. You can check a weather app or website.']),
    (r'(.*)', ['I\'m sorry, I don\'t understand that. Can you please rephrase?'])
]

chatbot = Chat(patterns, reflections)

def start_chatbot():
    print("Hello! I am a chatbot named Alex. How can I assist you today?")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

if __name__ == "__main__":
    start_chatbot()

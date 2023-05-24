import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["hello %1, how are you"]
    ],
    [
        r"Hello|Hi",
        ["Hey There"]
    ],
    [
        r"How are You?",
        ["I am Fine. How are you"]
    ],
    [
        r"I am Fine",
        ["Good to know"]
    ],
    [
        r"How is the weather in (.*)",
        ["It is very pleasant in %1 "]

    ]

]

chatbot = Chat(pairs, reflections)

print("Welcome to ChatBot! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    print(chatbot.respond(user_input))

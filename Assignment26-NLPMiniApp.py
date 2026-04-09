import random

# Predefined responses
responses = {
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "your name": ["I'm a chatbot created by Shweta "]
}


def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot:", random.choice(responses["bye"]))
            break

        found = False
        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Chatbot: Sorry, I don't understand.")


# Run chatbot
chatbot()
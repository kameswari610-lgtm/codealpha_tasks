def chatbot():
    print("Welcome to My Chatbot")

    while True:
        message = input("You: ").strip().lower()

        if message == "hiii":
            print("Bot: Hello! Welcome.")

        elif message == "how are you chatbot":
            print("Bot: I am fine. Thank you!")

        elif message == "what is python":
            print("Bot: Python is a popular programming language.")

        elif message == "who created python":
            print("Bot: Python was created by Guido van Rossum.")

        elif message == "what is your name":
            print("Bot: My name is Chatbot.")

        elif message == "what can you do":
            print("Bot: I can answer simple questions.")

        elif message == "bye chatbot":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
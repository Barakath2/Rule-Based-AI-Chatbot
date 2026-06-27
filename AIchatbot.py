print("🤖 Welcome to AI Chatbot")
print("Type 'exit' to quit")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: I am Decode AI Chatbot.")

    elif user == "what is the time":
        print("Bot: Sorry, I dont have access to the current time.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")


print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How are you?")

    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Chatbot: My name is Python Bot.")

    elif user == "what can you do":
        print("Chatbot: I can chat with you!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")

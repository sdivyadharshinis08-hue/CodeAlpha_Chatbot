def get_reply(message):
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm a simple chatbot."
    elif message == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("Chatbot: Type 'hello', 'how are you', or 'bye'.")
    while True:
        user = input("You: ")
        reply = get_reply(user)
        print("Chatbot:", reply)
        if user.lower().strip() == "bye":
            break


main()
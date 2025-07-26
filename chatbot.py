print("Welcome to Simple AI Chatbot (Rule-Based). Type 'exit' to quit.")

while True:
    user_input = input("You: ").lower()

    if 'hello' in user_input or 'hi' in user_input:
        print("Bot: Hello! How can I help you with AI concepts?")
    
    elif 'what is ai' in user_input:
        print("Bot: AI stands for Artificial Intelligence, where machines mimic human intelligence.")
    
    elif 'What are Applications of ai' in user_input:
        print("Bot: AI is used in healthcare, finance, education, self-driving cars, and more.")
    
    elif 'what is nlp' in user_input:
        print("Bot: NLP is Natural Language Processing. It helps computers understand human language.")

    elif 'what is today Weather' in user_input:
        print("Bot : I cuold not Check Weather But Today You have Nice day!")

    elif 'what are the Data Types' in user_input:
        print("Bot: Here are the main data types in most programming languages (like Python, Java, C, etc.)")
    
    elif 'thanks' in user_input or 'thank you' in user_input:
        print("Bot: You're welcome! Feel free to ask more questions.")
    
    elif user_input == 'exit':
        print("Bot: Goodbye! Have a great day.")
        break
    
    else:
        print("Bot: I'm still learning! Can you ask something related to AI?")

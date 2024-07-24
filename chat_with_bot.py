from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Define your chatbot creation function
def create_custom_chatbot():
    chatbot = ChatBot(
        'TestBot',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.MathematicalEvaluation'
        ],
        tagger_language='en_core_web_sm'  # Explicitly specify the spaCy model
    )
    return chatbot

# Create the chatbot with the custom configuration
chatbot = create_custom_chatbot()

# Train the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

print("ChatBot created and trained successfully")

# Start interactive chat
print("Hello! I am TestBot. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print(f"TestBot: {response}")

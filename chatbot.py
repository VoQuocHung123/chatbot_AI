from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Travelbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',

    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',

        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'none',
            'maximum_similarity_threshold': 0.80
        }
    ],
       
    read_only=True
)


trainer = ChatterBotCorpusTrainer(chatbot)


trainer.train('./training_data')




from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# chatbot = ChatBot("Johnny Five", read_only=True)  inhabilita el entrenamiento
chatbot_train = ChatBot("InvBot")

conversacion = [
    "Hola!",
    "Hola! Como estas?",
    "Bien y tu?",
    "Bien tambien, en que te puedo ayudar?",
    "Quiero ver una pelicula",
    "Yo te hare una recomendacion"
]

chatbot_train.set_trainer(ListTrainer)
# recibe una lista ordenada con frases
#chatbot_train.train(conversacion)


# Para entrenar con un corpus


chatbot = ChatBot(
    'Export Example Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./db_tutorial_esp.json'
)

chatbot.train('chatterbot.corpus.spanish')



print("termine de entrenar")





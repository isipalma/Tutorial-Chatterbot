from chatterbot import ChatBot

# Instanciamos el bot que fue entrenado con el corpus, con read_only = True para que solamente responda y no entrene
chatbot = ChatBot(
    "My ChatterBot", read_only=True,
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./db_tutorial_esp.json'
)
# Bot que fue entrenado con ListTrainer, para utilizar este comente el chatbot superio y descomente este
# chatbot = ChatBot("Samuel Simplesco", read_only=True)

try:
    while True:
        texto = str(input("query: "))
        respuesta_bot = chatbot.get_response(texto)
        print(respuesta_bot)
except KeyboardInterrupt:
    pass

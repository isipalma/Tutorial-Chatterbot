from chatterbot import ChatBot


chatbot = ChatBot(
    "My ChatterBot",
storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./db_tutorial_esp.json'
)


respuesta_bot = chatbot.get_response('hi')

while True:
    texto = str(input("query: "))
    respuesta_bot = chatbot.get_response(texto)
    print(respuesta_bot)
## Tutorial-Chatterbot ##

Tutorial de cómo crear su propio chat bot paso a paso y se detallan las especificaciones de como personalizarlo para distintos usos.
# Requisitos previos: #
Para poder utilizar chatterbot hay que instalar:

1) La libreria chatterbot

> Usando pip:

> > pip install chatterbot

> Instalando desde source (se debe tener instalado git)
> >  git clone https://github.com/gunthercox/ChatterBot.git

> >  pip install ./ChatterBot

> Una vez instalado se puede verificar la version utilizando el comando "python -m chatterbot --version"



2) La libreria nltk

Para Mac/Unix
> sudo pip install -U nltk


Para Windows (32-bit binary installation)
> 1. Instalar NLTK: http://pypi.python.org/pypi/nltk

> 2. Para corrobar que se instalo: Start>Python35, luego usar import nltk


3) Instalar el jsondb que utiliza la librería

> ejecutar comando: pip install git+https://github.com/gunthercox/jsondb.git

# Entrenamiento:

Antes de crear alguna instancia del bot este necesita una base de datos con la cual procesar las frases que se le entreguen.

Para este objetivo la libreria chatterbot ofrece cuatro metodos de entrenamiento:

1) ListTrainer

Este método consiste en hacer entrenar al bot en base a una lista donde cada elemento es una frase de una conversacion y se rige segun un orden donde el elemento en la posicion i+1 corresponde a la respuesta a la frase en la posicion i. En otras palabras, la lista que recibe el bot es una secuencia de frases ordenadas secuencialmente que forman una sola conversacion. Cabe destacar que el bot puede recibir más de una lista para entrenar.

Ejemplo:
```
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ejemplo")
###### aqui se selecciona el entrenador
chatterbot.set_trainer(ListTrainer)

chatterbot.train([
    "Hola!",
    "Hola",
    "Como estas?",
    "Bien y tu?",
    "Bien tambien"
])
chatterbot.train([
    "Te casarias conmigo?",
    "El sistema se ha caido, intente mas tarde",
    "rayos"])
```
Tambien es posible agregar una lista con una frase que este en otra conversacion, de esta forma el bot puede responder dos cosas distintas al mismo input


2) ChatterBotCorpusTrainer

Este entre al bot con una base de datos que viene en la libreria chatterbot (se les conoce como Corpus) de algun idioma especifico


> from chatterbot.trainers import     ChatterBotCorpusTrainer

> chatterbot = ChatBot("Ejemplo idioma")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

>chatterbot.train(
    "chatterbot.corpus.english"
)

Si no se desea entrenar al bot con todo el corpus esta la posibilidad de solamente

chatterbot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

3) UbuntuCorpusTrainer

Este entrenador entrena automaticamente al bot utilizando un data set que posee casi un millon de conversaciones, sin embargo se encuentra en idioma ingles.

4) TwitterTrainer

Permite entrenar con tweets de Twitter



Para seleccionar el entrenador es posible agregarlo como parametro al bot al momento de isntanciarlo en vez de utilizar el metodo "set trainer"

>chatbot = ChatBot(
    'Ejemplo',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

Para ver el source del codigo de este ultimo entrenador ingrese al siguiente link http://chatterbot.readthedocs.io/en/stable/training.html

Ademas de utilizar estos entrenadores tambien es posible entrenar a tu chatbot mediante inputs manuales:
> chatbot = ChatBot("alumno")

> while True:

>entrada = input("query:")

>respuesta = chatbot.get_response(entrada)

>print(respuesta)

# Definiendo el contenedor del bot:

Por defecto, si no se especifica que tipo de archivo contendra la base de datos del bot este por defecto guardara todo en un archivo database.db.
Si se desea optar por otro tipo de almacenaje se debe especificar en los parametros del bot el tipo de almacenaje y el archivo donde se guardaran los datos antes de entrenarlo:

>chatbot = ChatBot(
    'Ejemplo almacen',
    trainer='chatterbot.trainers.ListTrainer',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    database='./db_tutorial_esp.json'
)


# Instanciando el Bot:

Una vez entrenado el bot ahora lo instanciaremos para poder hablar con el.

Es bastante importante que agreguemos un parametro llamado Read_only=True, ya que con esto el bot dejara de aprender los inputs que reciba y solamente procesará la frase que recibio y entregará una respuesta.

El bot que se instancie puede recibir distintos parametros, lo cual lo hace bastante personalizable, pero el más básico es:

```
from chatterbot import ChatBot
chatbot = ChatBot("Samuel Simplesco", read_only=True)```

Este bot tomara una base de datos predefinida (database.db) ya que ninguna fue especificada en los parametros.

Ahora, para darle un input y obtener una respuesta se utiliza el metodo .get_response(string). Este metodo entega un string, a menos que el parametro output_format del bot sea distinto a 'text'.
```
entrada = input("Ingrese frase")
respuesta = chatbot.get_response(entrada)
print(respuesta)```

# Creando tus propias clases:

Como ya se menciono antes esta libreria es bastante versatil y personalizable, principalmente porque permite crear tus propios adaptadores logicos, metodos de almacenamiento, metodo de entrenamiento, basicamente puedes hace run bot desde cero.

Para esto basta con crear tu clase que herede de    e implemente los metodos básicos de esa clase. He aqui un ejemplo al crear un adaptador logico propio:

```
from chatterbot.logic import LogicAdapter
# heredo de la clase LogicAdapter
class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)
# Estos dos metodos siempre deben ser creados

# statement es un objeto de tipo statement que posee el atributo 'text'
    def can_process(self, statement):

        # Este metodo determina si es posible encontrar una respuesta para
        # el statement entregado. Si la respuesta es si entrega True, sino
        # entrega False y no se ejecuta process
        return True

    def process(self, statement):
        # Este metodo crea la repsuesta a partir del statement entregado.

        import random
        # Uno de los parametros que entrega este metodo es confidence, el cual
        # es un numero del 0 al 1 que determina que tan precisa es la respuesta.
        # Este numero sirve principalmente en el caso de que se utilicen más
        # de un LogicAdapter, pues el que entregue una respuesta con el confidence
        # más cercano a 1 será el output elegido por el bot.
        confidence = random.uniform(0, 1)

        #  Para este ejemplo se esta entregando el mismo statement.
        selected_statement = statement

        return confidence, selected_statement


```

De la misma forma se pueden crear StorageAdapter, Trainers, entre otros. Para ver como se componen cada clase y que metodos deben ser implementados se debe ingresar al github https://github.com/gunthercox/ChatterBot y ver el codigo de cada clase .



# Instrucciones para el tutorial:

En la carpeta Tutorial se encuentran dos archivos .py, con uno de estos es posible entrenar de forma rapida un chatbot mediante el entrenador ChatterBotCorpusTrainer o entrenar un bot con ListTrainer. Con el otro es posible hablar con cualquiera de los dos bots mediante la consola de python.

Para seleccionar cada uno se deben seguir las isntrucciones indicadas en los mismos archivos

Si aparecen advertencias indeseadas en la consola, ya sean por el JsonFileStorageAdapter o por la libreria nltk siga estas instrucciones:

Para evitar el warning de JsonFileStorageAdapter debe agregar el keyword silence_performance_warning=True entre los parametros del bot.

```
chatbot = ChatBot(
    "My ChatterBot", read_only=True,
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    silence_performance_warning=True,    # aqui
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    output_format="text",
    database='./db_tutorial_esp.json')
```
    
    
Este mensaje aparece pues se recomienda no utilizar json para procesos demasiado grandes.

Para evitar los mensajes de la libreria la primera vez que corra su codigo debe poseer los permisos de la libreria, y para esto agregue las siguientes lineas de codigo al inicio de su programa, pero para las proximas ocasiones en que lo corra borrelas.

```
import ssl

try:    
    _create_unverified_https_context = ssl._create_unverified_context

except AttributeError:
    pass

else:
    ssl._create_default_https_context = _create_unverified_https_context
```

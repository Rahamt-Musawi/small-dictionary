from flask import Flask
from flask_socketio import SocketIO
import nltk
from nltk.corpus import wordnet
# import spacy
import requests
from bs4 import BeautifulSoup

nltk.download('wordnet')
# load the English language model
# nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")

# define a function to get the definitions, synonyms, and example sentences for a word
def get_web_word_info(word):
    # get the HTML for the word's page on Merriam-Webster
    response = requests.get(f"https://www.merriam-webster.com/dictionary/{word}")
    soup = BeautifulSoup(response.content, "html.parser")

    # find the main definition
    
    main_def = soup.find("span", class_="dtText")
    if main_def is not None:
        main_def = main_def.text.strip(":")
    
    # find the example sentences
    examples = []
    for example in soup.find_all("span", class_="t has-aq"):
        examples.append(example.text)

    # return the word information as a dictionary
    return {
        "word": word,
        "definition": main_def,
        "examples": examples,
    }



message = 'Hello from Backend :)'
syn = list()
ant = list()
web_word_def=list()
web_word_example=list()


@socketio.on('message')
def handle_message(data):
    syn.clear()
    ant.clear()
    web_word_def.clear()
    web_word_example.clear()

    web_word_info = get_web_word_info(data)

    web_word_def.append(web_word_info['definition'])

    print("Examples:")
    for example in web_word_info["examples"]:
        print(f"- {example.strip()}")
        web_word_example.append(example)


    global message
    message = data
    synsets = wordnet.synsets(message)

    if synsets:
        synset = synsets[0]  # choose the first synset
        definition = synset.definition()  # get the definition of the synset
        examples = synset.examples()
        # synonyms= [str(lemma.name()) for lemma in synset.lemmas()]
        for synset in synsets:
            for lemma in synset.lemmas():
                # syn.clear()
                if lemma.name() not in syn:
                    syn.append(lemma.name())    #add the synonyms
                if lemma.antonyms():    #When antonyms are available, add them into the list
                    # ant.clear()
                    if lemma.antonyms()[0].name() not in ant:
                        ant.append(lemma.antonyms()[0].name())
        

        word_information=[  
        {"word": message},
        {"definition":definition, "web_definition": web_word_def},  
        {"synonyms": ', '.join(syn)},
        {"antonyms": ', '.join(ant)},
        {"examples": ', '.join(examples), "web_examples": web_word_example}]
 
        socketio.emit("response", word_information)

    else:
        socketio.emit("not_found", f"No definitions found for '{message}'. Please make sure if the spelling is correct. Currently, only English single words are supported in this dictionary.")
        print(f"No definitions found for '{message}'")

    return 'Message sent from backend'


if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=5000, ssl_context=('server.crt', 'server.key'))




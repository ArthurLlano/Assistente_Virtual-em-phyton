import speech_recognition as sr
import re
import pyttsx3
import webbrowser
from datetime import datetime

nome = ""

def get_current_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time

def get_current_date():
    current_date = datetime.now().strftime("%d/%m/%Y")
    return current_date

while True:
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
        mic.adjust_for_ambient_noise(source)
        print("Vamos começar, fale alguma coisa...")
        audio = mic.listen(source)
        try:
            frase = mic.recognize_google(audio, language='pt-BR')
            print("Você falou: " + frase)

            if re.search(r'\b' + "ajudar" + r'\b', format(frase)):
                engine.say("Você precisa de ajuda")
                engine.runAndWait()
                print("Algo relacionado à ajuda.")

            elif re.search(r'\b' + "meu nome é " + r'\b', format(frase)):
                t = re.search('meu nome é (.*)', format(frase))
                nome = t.group(1)
                print("Entendi, vou salvar seu nome como " + nome)
                engine.say("Entendi, vou salvar seu nome como " + nome)
                engine.runAndWait()

            elif re.search(r'\b' + "internet" + r'\b', format(frase)):
                engine.say("Abrindo o navegador")
                engine.runAndWait()
                webbrowser.open("https://www.google.com")
                print("Comando para abrir o navegador detectado.")

            elif re.search(r'\b' + "vagabunda" + r'\b', format(frase)):
                print("Corno manso " + nome)
                engine.say("Corno manso " + nome)
                engine.runAndWait()    

            elif re.search(r'\b' + "Que dia é hoje" + r'\b', format(frase)):
                current_date = get_current_date()
                engine.say("Hoje é " + current_date)
                engine.runAndWait()

            elif re.search(r'\b' + "Que horas são" + r'\b', format(frase)):
                current_time = get_current_time()
                engine.say("Agora são " + current_time)
                engine.runAndWait()

            elif re.search(r'\b' + "desligar" + r'\b', format(frase)):
                print("Desligando a assistente virtual...")
                engine.say("Desligando a assistente virtual.")
                engine.runAndWait()
                break

        except sr.UnknownValueError:
            print("Ops, algo deu errado.")


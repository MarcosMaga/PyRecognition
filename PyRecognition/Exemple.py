import PyRecognition

while True:
    speech = PyRecognition.recognition('pt-BR')
    print(speech)

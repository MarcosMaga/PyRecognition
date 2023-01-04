from PyRecognition import PyRecognition

recognizer = PyRecognition('en-US')

while True:
    speech = recognizer.recognition()
    print(speech)


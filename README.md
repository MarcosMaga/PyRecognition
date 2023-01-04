# PyRecognition 0.2v

**PyRecognition** is a module that seeks to bring a recognition of
quality voice and speed of response for python.

## Functions

* `PyRecognition.recognition()` - Returns what was recognized by the system.

### Requisits

* Selenium. `pip install selenium`
* Google Chrome 87+.
* Windows.

#### Como usar?

* Download the repository and extract it into your project folder.
* Download the ChromeDrive for your version of Google Chrome
* importe o modulo usando `from PyRecognition import PyRecognition`.
* Instantiate **PyRecognition** with `recognizer = PyRecognition(language)`
* Get the value using `speech = recognizer.recognition()`
* See the **Exemple.py**

from flask import Flask, render_template, request
import speech_recognition as sr
import time 
app = Flask(__name__)
mic = sr.Microphone()
recog = sr.Recognizer()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        with mic as audio:
            print("Espere un momento")
            recog.adjust_for_ambient_noise(audio)
            print("Puedes hablar en 3 segundo" )
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            resultado =  recog.listen(audio, timeout=15)
            texto = recog.recognize_google(resultado, language='es-ES')
            return render_template('index.html', audio=texto)
if __name__ == '__main__':
    app.run(debug=True)
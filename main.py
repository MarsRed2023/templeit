import speech_recognition as sr
import time

mic = sr.Microphone()
recog = sr.Recognizer()
palabras = ["Casa", "Carro"]
pword = []
while True:
    print("Tendras 5 segundos para decir la palabra")
    try:
        with mic as audio:
            print("Wait a moment...")
            recog.adjust_for_ambient_noise(audio)
            print("Ya puedes hablar en 3 segundos")
            time.sleep(3)
            audio = recog.listen(audio, timeout=3)
            texto = recog.recognize_google(audio, language="es-ES")
            return render_template('index.html', audio = texto)
    except:
        print("Hubo un problema, intentalo de nuevo")


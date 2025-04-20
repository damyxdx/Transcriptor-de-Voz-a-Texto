import speech_recognition as sr 
import datetime

# Crear archivo .txt con nombre basado en fecha y hora
nombre_archivo = datetime.datetime.now().strftime("transcripcion_%Y-%m-%d_%H-%M-%S.txt")

# Iniciar reconocedor y micrófono
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Transcribiendo... (Ctrl+C para salir)\n")
print(f"📝 Guardando en: {nombre_archivo}\n")

try:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            audio = recognizer.listen(source)
            try:
                texto = recognizer.recognize_google(audio, language="es-AR")
                print("🗣️", texto)
                with open(nombre_archivo, "a", encoding="utf-8") as f:
                    f.write(texto + "\n")
            except sr.UnknownValueError:
                print("[No se entendió]")
except KeyboardInterrupt:
    print("\n🛑 Transcripción finalizada.")
    print(f"📄 Archivo guardado: {nombre_archivo}")

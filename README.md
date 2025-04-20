# 🎙️ Transcriptor de Voz a Texto en Tiempo Real

Este script utiliza la librería `speech_recognition` para convertir tu voz en texto en tiempo real a través del micrófono. Cada transcripción se guarda automáticamente en un archivo `.txt` con nombre basado en la fecha y hora.

---

## 🛠️ Requisitos

Antes de ejecutar el script, asegurate de tener instaladas las siguientes dependencias:

```bash
pip install SpeechRecognition
pip install PyAudio

▶️ Cómo usar
Descargá el script: import_speech_recognition_as_sr.py

Ejecutalo desde la terminal:

bash

python import_speech_recognition_as_sr.py
Comenzá a hablar. El script transcribirá automáticamente todo lo que digas.

Cada línea transcripta se guarda en un archivo llamado:

transcripcion_YYYY-MM-DD_HH-MM-SS.txt
Para detener la transcripción, presioná Ctrl + C.

📂 Salida
El archivo de salida se crea en el mismo directorio que el script. Cada línea de texto representa una oración detectada por el micrófono.

🧠 Notas
El idioma de reconocimiento está configurado en es-AR (Español - Argentina).

El script ajusta el micrófono al ruido ambiente antes de comenzar.

Si no se entiende lo que decís, se mostrará [No se entendió].

📞 Créditos
Desarrollado por Alberto Damian Garcia
Email: adamiangarcia93@gmail.com

---

## 🇺🇸 README - Real-Time Speech to Text Transcriber

```markdown
# 🎙️ Real-Time Speech to Text Transcriber

This script uses the `speech_recognition` library to convert your voice into text in real-time using your microphone. Each transcription is automatically saved into a `.txt` file named with the current date and time.

---

## 🛠️ Requirements

Make sure you have the following dependencies installed:

```bash
pip install SpeechRecognition
pip install PyAudio
⚠️ On some systems, PyAudio may require additional setup.
For Windows, you can use:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

▶️ How to Use
Download the script: import_speech_recognition_as_sr.py

Run it in the terminal:

python import_speech_recognition_as_sr.py
Start speaking. The script will transcribe your speech in real time.

The transcription is saved in a file named:

transcripcion_YYYY-MM-DD_HH-MM-SS.txt
To stop the transcription, press Ctrl + C.

📂 Output
The output file is saved in the same directory as the script. Each line corresponds to a detected speech segment.

🧠 Notes
Language is set to es-AR (Spanish - Argentina).

The script adjusts for ambient noise before recording.

If speech is not understood, it will display [No se entendió].

📞 Credits
Developed by Alberto Damian Garcia
Email: adamiangarcia93@gmail.com

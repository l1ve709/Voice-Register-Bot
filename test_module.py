import speech_recognition as sr

recognizer = sr.Recognizer()

async def listen_for_audio():
    try:
        with sr.Microphone() as source:
            print("Dinleniyor...")
            audio_data = recognizer.listen(source, timeout=10) 

        command = recognizer.recognize_google(audio_data, language='tr-TR')
        print(f'Algılanan ses: {command}')
        return command
    except sr.UnknownValueError:
        print('Ses algılanamadı.')
        return None
    except sr.RequestError as e:
        print(f'Ses tanıma servisi hatası: {e}')
        return None

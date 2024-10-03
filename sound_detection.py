# # Our main function is here.
# The bot can detect and "understand" the human voice
# ! GitHub l1ve709

import discord
from discord.ext import commands, tasks
import asyncio
import speech_recognition as sr
import wave
import pyaudio

l1ve709_token = ""  # bot token
txt_channel = 1287819739871055953  # Text channel to print detected sounds
vc_channel_id = 1288171063494316245  # Voice channel ID the bot will join
intents = discord.Intents.all()
l1ve709 = commands.Bot(command_prefix='.', intents=intents)

@l1ve709.event
async def on_ready():
    print(f'{l1ve709.user.name}')

    vc_channel = l1ve709.get_channel(vc_channel_id)
    if vc_channel:
        await vc_channel.connect()
        print(f'Connected to {vc_channel.name}')
        await listen_for_audio()

async def listen_for_audio():
    recognizer = sr.Recognizer()
    text_channel = l1ve709.get_channel(txt_channel)
    voice_client = discord.utils.get(l1ve709.voice_clients)

    while True:
        audio_data = await record_audio()

        if audio_data is not None:
            try:
                command = recognizer.recognize_google(audio_data, language='tr-TR')  # Language set to TR this a default setting channge this
                print(f'Perceived sound: {command}')
                
                await text_channel.send(f'Perceived sound: **{command}**')
            except sr.UnknownValueError:
                print('No sound detected')
            except sr.RequestError as e:
                print(f'Speech Recognition service error: {e}')

        await asyncio.sleep(1)  

async def record_audio():
    recognizer = sr.Recognizer()
    audio_data = []

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
    
    duration = 5  # Record for 5 seconds
    print(f"Recording for {duration} seconds..")
    
    for _ in range(0, int(16000 / 1024 * duration)):
        data = stream.read(1024)
        audio_data.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_file = sr.AudioData(b''.join(audio_data), 16000, 2)
    return audio_file

l1ve709.run(l1ve709_token)



## Coming Soon

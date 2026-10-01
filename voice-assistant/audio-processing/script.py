import io
import os
import asyncio
import sounddevice as sd
import scipy.io.wavfile as wavfile
import edge_tts
import pygame
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
pygame.mixer.init()

DURATION = 4 
SAMPLERATE = 16000
VOICE = "pt-BR-AntonioNeural"
SYSTEM_PROMPT = """
You are a helpful assistant
"""

async def speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]
    
    audio_stream = io.BytesIO(audio_data)
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

async def main():
    print("--- (Ctrl+C to stop) ---")
    while True:
        print("\n[Ouvindo...]")
        recording = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
        sd.wait()
        
        buffer = io.BytesIO()
        wavfile.write(buffer, SAMPLERATE, recording.flatten())
        buffer.seek(0)

        print("[Processando...]")
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[
                    types.Part.from_bytes(data=buffer.read(), mime_type="audio/wav"),
                    "Respond briefly to the user's speech."
                ],
                config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
            )
            
            ai_text = response.text
            print(f"{ai_text}")

            await speak(ai_text)
            
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 
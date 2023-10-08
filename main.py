import os
from elevenlabs import generate, save, set_api_key, Voice, VoiceSettings
from dotenv import load_dotenv

load_dotenv()

set_api_key(os.environ.get("ELEVEN_LABS_API_KEY"))

title = "Hackers And Painters"

voice = Voice(
    voice_id='', # Paul Graham
    settings=VoiceSettings(stability=0.3, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
)

def generate_essay_voiceover(title):
    with open(f'./essays/{title}.txt', 'r') as file:
        text = file.read()

        audio = generate(
            text=text,
            voice=voice,
            model="eleven_multilingual_v2"
        )

        save(audio, f'./voiced/{title}.mp3')



generate_essay_voiceover(title)
    


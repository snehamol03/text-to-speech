import streamlit as st
import pyttsx3
from pydub import AudioSegment
import io
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def text_to_speech(text):
    # Ensure the audio directory exists
    audio_dir = "audio"
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    # Save the speech to an audio file
    audio_path = os.path.join(audio_dir, "output.wav")
    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    
    # Load the audio file and return it
    audio = AudioSegment.from_wav(audio_path)
    return audio

# Streamlit app setup
st.title("Simple Text to Speech Converter")

text_input = st.text_area("Enter the text you want to convert to speech")

if st.button("Convert"):
    if text_input.strip():
        st.write("Generating speech...")
        audio = text_to_speech(text_input)
        
        # Convert audio to a format Streamlit can handle
        with io.BytesIO() as audio_buffer:
            audio.export(audio_buffer, format="wav")
            st.audio(audio_buffer, format="audio/wav")
        
        st.success("Speech generated and played successfully!")
    else:
        st.error("Please enter some text to convert to speech.")

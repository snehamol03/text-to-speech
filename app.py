import streamlit as st
from gtts import gTTS
import io

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    
    # Save the speech to an in-memory file
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    
    return audio_buffer

# Streamlit app setup
st.title("Simple Text to Speech Converter")

text_input = st.text_area("Enter the text you want to convert to speech")

if st.button("Convert"):
    if text_input.strip():
        st.write("Generating speech...")
        audio_buffer = text_to_speech(text_input)
        
        # Display the audio player in Streamlit
        st.audio(audio_buffer, format="audio/mp3")
        
        st.success("Speech generated and played successfully!")
    else:
        st.error("Please enter some text to convert to speech.")

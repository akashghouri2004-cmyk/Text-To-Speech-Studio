import base64
import os
from gtts import gTTS
import streamlit as st

st.set_page_config(page_title="Text to Speech Studio", page_icon="🎵", layout="centered")
st.title("🎵 Premium Text to Speech Studio")
st.write("Convert your English or Urdu text into speech online.")

if "text_input_val" not in st.session_state:
    st.session_state.text_input_val = ""

uploaded_file = st.file_uploader("📂 Load a text file (.txt)", type=["txt"])
if uploaded_file is not None:
    st.session_state.text_input_val = uploaded_file.read().decode("utf-8")

text_to_convert = st.text_area("Enter Text:", value=st.session_state.text_input_val, height=200, placeholder="Type or paste text...")

col1, col2 = st.columns(2)
with col1:
    lang_display = st.selectbox("Language:", ["English", "Urdu"])
    selected_lang = "en" if lang_display == "English" else "ur"
with col2:
    speed_display = st.selectbox("Reading Speed:", ["Normal", "Slow"])
    selected_speed = True if speed_display == "Slow" else False

if st.button("🎵 Convert & Generate Audio", use_container_width=True):
    if not text_to_convert.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Processing audio..."):
            try:
                tts = gTTS(text=text_to_convert, lang=selected_lang, slow=selected_speed)
                filename = "online_speech.mp3"
                tts.save(filename)
                with open(filename, "rb") as f:
                    audio_bytes = f.read()
                st.success("Sound track successfully generated!")
                st.audio(audio_bytes, format="audio/mp3")
                st.download_button(label="💾 Download MP3 File", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3", use_container_width=True)
                if os.path.exists(filename):
                    os.remove(filename)
            except Exception as e:
                st.error(f"Error details: {e}")

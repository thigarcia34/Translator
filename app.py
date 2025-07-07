import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import numpy as np
import av

st.set_page_config(page_title="Tradutor de Voz", layout="centered")
st.title("🎧 Tradutor de Voz em Tempo Real (Inglês → Português)")

translator = Translator()

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        audio = frame.to_ndarray()
        # Apenas um placeholder, o real reconhecimento será manual
        return frame

def reconhecer_e_traduzir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙️ Fale agora...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto_ingles = recognizer.recognize_google(audio, language='en-US')
        st.success(f"Você disse (inglês): {texto_ingles}")

        traducao = translator.translate(texto_ingles, src='en', dest='pt')
        st.success(f"Tradução (português): {traducao.text}")

    except sr.UnknownValueError:
        st.error("❌ Não entendi o que você disse.")
    except sr.RequestError as e:
        st.error(f"Erro de conexão com o serviço de voz: {e}")

if st.button("🎤 Traduzir minha voz"):
    reconhecer_e_traduzir()

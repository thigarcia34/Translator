import streamlit as st
import speech_recognition as sr
from googletrans import Translator

st.set_page_config(page_title="Tradutor de Voz", layout="centered")
st.title("🎧 Tradutor de Voz em Tempo Real (Inglês → Português)")

translator = Translator()

def reconhecer_e_traduzir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙️ Fale algo em inglês...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto_ingles = recognizer.recognize_google(audio, language='en-US')
        st.success(f"Você disse (em inglês): {texto_ingles}")

        traducao = translator.translate(texto_ingles, src='en', dest='pt')
        st.success(f"Tradução (português): {traducao.text}")

    except sr.UnknownValueError:
        st.error("❌ Não entendi o que você disse.")
    except sr.RequestError as e:
        st.error(f"Erro de conexão com o serviço de voz: {e}")

if st.button("🎤 Traduzir minha voz"):
    reconhecer_e_traduzir()

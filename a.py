import streamlit as st
from googletrans import Translator, LANGUAGES

# Translator function
def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.src, translation.text  # Returns detected language and translated text

# Streamlit UI
st.title("Language Translator using Google Translate  API ")
st.write("Automatically detects the input language and translates it.")

# User input
text_input = st.text_area("Enter text to translate:")

# Target Language Selection
dest_lang = st.selectbox("Select Target Language", options=LANGUAGES.keys(),
                         index=list(LANGUAGES.keys()).index("en"), format_func=lambda x: LANGUAGES[x])

# Translate Button
if st.button("Translate"):
    if text_input:
        detected_lang, translated_text = translate_text(text_input, dest_lang)
        st.success(f"**Translated Text:** {translated_text}")
    else:
        st.warning("Please enter some text to translate.")

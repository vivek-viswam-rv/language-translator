import streamlit as st
import time

st.set_page_config(page_title="English to French Translator")
st.title("English to French Translator")

text = st.text_area("Source text", height=200, placeholder="Please enter your English text here...")
translate_btn = st.button("Translate")

if translate_btn:
    if not text.strip():
        st.warning("Please enter text to translate!")
    else:
        status = st.empty()
        status.info("Translating...")
        try:
            # result = translator(text)
            time.sleep(2)
            st.write("Here's your translation:")
            st.write(text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
        finally:
            status.empty()

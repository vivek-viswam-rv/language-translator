import streamlit as st
import time

st.set_page_config(page_title="French to English Translator")
st.title("French to English Translator")

text = st.text_area("Source text", height=200, placeholder="Please enter your French text here...")
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


import streamlit as st
import random

# Lista med roliga emojis
emojis = ["😀", "😂", "🤣", "😎", "🤔", "🤯", "🥳", "🤠", "👽", "🤖", "🦄", "🍕", "🌈", "🚀"]

st.title("EE22 Chatta med Emojis! 🎉")

# Initiera chat-historiken
if "messages" not in st.session_state:
    st.session_state.messages = []

# Funktion för att generera ett svar med en slumpmässig emoji
def generate_response(prompt):
    return f"{prompt} {random.choice(emojis)}"

# Visa tidigare meddelanden
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Hantera användarens input
if prompt := st.chat_input("Vad vill du säga?"):
    # Lägg till användarens meddelande till historiken
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generera och visa svaret
    response = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

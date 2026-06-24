import json
from pathlib import Path
from datetime import datetime

import streamlit as st

st.markdown("""

<style> /* Apenas o campo username */ .username div[data-baseweb="input"] > div { border: 2px solid #4f8bf9; border-radius: 12px; transition: all 0.3s ease; } .username-input div[data-baseweb="input"] > div:hover { border-color: #2563eb; } .username-input div[data-baseweb="input"] > div:focus-within { border-color: #2563eb; box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.15); } </style>

<script> window.addEventListener('load', function() { const inputs = window.parent.document.querySelectorAll('input'); inputs.forEach(input => { if (input.getAttribute('aria-label') === 'Username') { input.closest('[data-testid="stTextInput"]') ?.classList.add('username-input'); } }); }); </script>

""", unsafe_allow_html=True)


ARQUIVO_MENSAGENS = Path("mensagens.json")

st.set_page_config(layout="wide", page_icon="💭")

def carregar_mensagens():  #buscar mensagens
    if not ARQUIVO_MENSAGENS.exists():
        return []
    try:
        with open(ARQUIVO_MENSAGENS, "r",encoding="utf-8") as arquivo:
             return json.load(arquivo)
    expect json.JSONDecodeError:
        return[]
  
def salvar_mensagens(mensagens):   #salvar mensagens
    with open(ARQUIVO_MENSAGENS, "w",encoding="utf-8") as arquivo>
    json.dump(mensagens,arquivo,indent=-4, ensure_ascii=False)
horario =datetime.now(.strftime("%d/%m%Y, %H:%M:%S"))

mensagens.append(("time:horario,"
                   "username":username
                   "mensagens":mensagens""))
salvar_mensagens(mensagens)

st.title("Chat Público 😉 ")
username = st.sidebar.text_input("Nome do usúario", key="username", value="Anonimo")
st.button("Teste", type="primary")

@st.fragment(run_every=3)
def renderizar_chat():
    mensagens=carregar_mensagens()
    with st.container(border=True,height=500):
         for msg in mensagens:
             st.write(f"{msg["time"]} {msg["username"]}: {msg["mensagem"]}")
renderizar_chat()

if entrada_mensagens:
    adicionar_mensagens(username,entrada_mensagem)
    st.rerum
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

# Charger les données
df = pd.read_pickle("df_moviesOK.pkl")

# Titre avec une barre horizontale en HTML
st.markdown("<h3 style='text-align: center;'>CINE CHER</h3><hr>", unsafe_allow_html=True)

# Afficher la barre de recherche
search_query = st.text_input("Rechercher", placeholder="Insérer un film ou un nom d'acteur")

# Titre Streamlit
st.title("Recommandation")

# Afficher 6 champs pour images (2 x 3)
row1 = st.columns(3)
row2 = st.columns(3)
grid = [col.container(height=200) for col in row1 + row2]

# Définir une fonction d’assistance pour dessiner deux chats noirs.
def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")

# Définir une autre fonction d’assistance pour dessiner deux chats orange
def orange_cats():
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")

#(Facultatif) Testez vos fonctions en appelant chacune d’entre elles dans une carte de grille.
with grid[0]:
    black_cats()
with grid[1]:
    orange_cats()

# Utilisez un décorateur @st.experimental_fragment et commencez votre définition de fragment de chat noir.
@st.experimental_fragment
def herd_black_cats(card_a, card_b, card_c):
    #Ajout d’un bouton pour réexécuter ce fragment.
    st.button("Top recommandation")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()

@st.experimental_fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("Top films populaire")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()

@st.experimental_fragment
def top_meilleurs_films(card_a, card_b, card_c):
    st.button("Top meilleurs films")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()

#Afficher dans barre latérale
with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[1].empty(), grid[2].empty())
    herd_orange_cats(grid[3].empty(), grid[4].empty(), grid[5].empty())



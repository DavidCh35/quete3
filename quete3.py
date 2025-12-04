import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

#Vérifie si la clé 'logged_in' existe dans l'état de session
#Si elle n'existe pas on la met sur False
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
#Idem pour le nom d'utilisateur
if 'username' not in st.session_state:
    st.session_state['username'] = None
#Protection contre NameError
login_button = False
#Chargement du fichier CSV avec les utilisateurs
users = pd.read_csv("users.csv", sep=",")

#Si l'utilisateur est connecté on affiche tout
if st.session_state['logged_in'] == True:
    #Création de la barre latérale
    with st.sidebar:
        #Bouton de déconnexion
        bouton_deconnexion = st.button("Déconnexion")
        #Message de bienvenue + affichage nom de l'user
        st.text("Bienvenue " + st.session_state['username'])
        #Action de déconnexion
        if bouton_deconnexion:
            st.session_state['logged_in'] = False

        #Menu de navigation
        selection = option_menu(menu_title=None, options = ["Accueil", "Photos"], icons=["house", "camera"], default_index=0)
    #Contenu des différentes pages
    if selection == "Accueil":
        st.subheader("Bienvenue sur ma page")
    elif selection == "Photos":
        st.subheader("voici des photos de capybaras")
        #Création des colonnes pour avoir les images sur la meme ligne
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("capybara1.jpg")
        with col2:
            st.image("capybara2.jpg")
        with col3:
            st.image("capybara3.jpg")

#Affichage si l'utilisateur n'est pas connecté
else:
    st.title("Page de Connexion")
    username_input = st.text_input("Nom d'utilisateur")
    #type=password permet de masquer le mot de passe lors de la saisie
    #password_input : stocke le mot de passe saisi par l'utilisateur
    password_input = st.text_input("Mot de passe", type='password')
    login_button = st.button("Se connecter")
#vérification
if login_button:
    #Cherche une ligne ou le nom et mot de passe sont bons
    user_found = users[(username_input == users['name']) & (password_input == users['password'])]
    #Verif du succès : si PAS vide
    if user_found.empty == False:
    #Mise à jour de la session
        st.session_state['logged_in'] = True
        st.session_state['username'] = user_found['name'].iloc[0]
    #Message d'erreur
    else:
        st.error("L'username ou le password est/sont incorrect")

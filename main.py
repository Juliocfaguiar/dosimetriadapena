import streamlit as st
from streamlit_option_menu import option_menu
import home, calcular, cadastro, dashboard

st.set_page_config(
    page_title="Dosimetria",
    page_icon=":scales:",
    layout="wide",
)

class Multiapp:
    def __init__(self):  # Corrigido de __int__ para __init__
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({  # Corrigido de self.app para self.apps
            "title": title,
            "function": function,
        })

    def run(self):  # Adicionado self como parâmetro
        app = option_menu(
            None,
            ["Home", "Calcular", "Cadastro de Delito", "Dashboard"],
            icons=[
                "house-fill",
                "database",
                "person-circle",
                "pc-display-horizontal",
            ],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )

        if app == "Home":
            home.app()
        elif app == "Calcular":
            calcular.app()
        elif app == "Cadastro de Delito":
            cadastro.app()
        elif app == "Dashboard":
            dashboard.app()


# Instância e execução
multiapp = Multiapp()
multiapp.run()
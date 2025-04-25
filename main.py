import streamlit as st
from streamlit_option_menu import option_menu
import home, calcular, cadastro,dashboard,simulacao


st.set_page_config(
    page_title="Dosimetria",
    page_icon=":scales:",
    layout="wide",
)

class Multiapp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run() :

        app = option_menu(None,
                          ['Home',
                           'Calcular',
                           'Cadastro de Delito',
                           'Dashboard',
                            'Simulação',
                          ],
                          
            icons=['house-fill','database','person-circle','pc-display-horizontal','display','display',], 
            menu_icon="cast", default_index=0, orientation="horizontal")
    
        
        if app == "Home":
            home.app()
        elif app == "Calcular":
            calcular.app()
        elif app == "Cadastro de Delito":
            cadastro.app()
        elif app == "Dashboard":
            dashboard.app()
        if app == "Simulação":
            simulacao.app()
    run()
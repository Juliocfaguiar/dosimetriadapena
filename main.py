
import streamlit as st
from streamlit_option_menu import option_menu
import home, calcular, cadastro,dashboard


st.set_page_config(
        page_title = "Dosimetria",
        page_icon =":scales:",
        layout = "wide",

    )

class Multiapp:
    
    def __int__(self):
        self.apps = []
    def add_app(self,title,function):
        self.app.append({
            "title"     : title,
            "function"  : function
        })

    def run() :

        app = option_menu(None,
                          ['Home',
                           'Calcular',
                           'Cadastro de Delito',
                           'Dashboard',
                          ],
                          
            icons=['house-fill','database','person-circle','pc-display-horizontal','display','display',], 
            menu_icon="cast", default_index=0, orientation="horizontal")
    
        
        if app == "Home":
            home.app()
        if app == "Calcular":
            calcular.app()  
        if app == "Cadastro de Delito":
            cadastro.app()    
        if app == "Dashboard":
            dashboard.app()
    run()
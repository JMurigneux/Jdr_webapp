import streamlit as st
import pandas as pd
import json
image_path='images/'


######################
# Page Title
######################

st.set_page_config(page_title="JDR_PERSO",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")



######################
#SIDEBAR
######################

 
try:
    a=st.session_state["character_loaded"]
    
except KeyError:
    st.session_state["data_perso"]={
    "nom_personnage": "", 
    "PV": 0, "PSY": 0, "max_PV" : 0,"max_PSY":0,
    "Physique": 0, 
    "Social": 0,
    "Mental": 0, 
    "nom_competence_1": "", 
    "bonus_competence_1": 0, 
    "nom_competence_2": "", 
    "bonus_competence_2": 0, 
    "nom_competence_3": "", 
    "bonus_competence_3": 0, 
    "nom_competence_4": "", 
    "bonus_competence_4": 0,
    "nom_competence_5": "", 
    "bonus_competence_5": 0,
    "nom_don_1": "", 
    "cout_don_1": 0, 
    "nom_don_2": "", 
    "cout_don_2": 0, 
    "nom_don_3": "", 
    "cout_don_3": 0, 
    "nom_don_4": "", 
    "cout_don_4": 0}


st.session_state["nouveau_perso"]={}

def creation_perso():
    st.session_state["data_perso"]=st.session_state["nouveau_perso"].copy()
    st.session_state["data_perso"]["PV"]=st.session_state["data_perso"]["max_PV"]
    st.session_state["data_perso"]["PSY"]=st.session_state["data_perso"]["max_PSY"]

    st.session_state["character_loaded"]=True

try:
    a=st.session_state["character_loaded"]
except:
    a=False

st.sidebar.write("# Upload ta fiche de personnage")
uploaded_file = st.sidebar.file_uploader("")
if uploaded_file is not None:
    fiche_perso_upload = json.load(uploaded_file)
    # st.json(fiche_perso_upload, expanded=True)

    try:
        a=st.session_state["character_loaded"]
    except KeyError:
        st.session_state["old_data"]=fiche_perso_upload.copy()
        st.session_state["data_perso"]=fiche_perso_upload.copy()
        st.session_state["data_perso"]["nom_personnage"]=st.session_state["data_perso"]["nom_personnage"].replace("_"," ")
        st.session_state["character_loaded"]=True

else:
    st.sidebar.write("# Ou crée ton personnage") 
    # crée le nouveau perso
    st.sidebar.button("création du personnage",key=25,on_click=creation_perso)
    st.session_state["nouveau_perso"]["nom_personnage"]=(st.sidebar.text_input("Nom du personnage", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, placeholder="Nom du personnage", disabled=False))


    #stats
    st.session_state["nouveau_perso"]["max_PV"]=int(st.sidebar.text_input("PV", value=0, max_chars=None, key=0, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    st.session_state["nouveau_perso"]["max_PSY"]=int(st.sidebar.text_input("PSY", value=0, max_chars=None, key=1, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    st.session_state["nouveau_perso"]["Physique"]=int(st.sidebar.text_input("Physique", value=0, max_chars=None, key=2, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    st.session_state["nouveau_perso"]["Social"]=int(st.sidebar.text_input("Social", value=0, max_chars=None, key=3, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))
    st.session_state["nouveau_perso"]["Mental"]=int(st.sidebar.text_input("Mental", value=0, max_chars=None, key=4, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #competences
    st.sidebar.write("## Compétences") 

    st.session_state["nouveau_perso"]["nom_competence_1"]=(st.sidebar.text_input("Nom compétence 1", max_chars=None, key=5, type="default", help=None, autocomplete=None, on_change=None, placeholder="compétence 1", disabled=False))
    st.session_state["nouveau_perso"]["bonus_competence_1"]=int(st.sidebar.text_input("Bonus compétence 1", value=0, max_chars=None, key=6, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_competence_2"]=(st.sidebar.text_input("Nom compétence 2",  max_chars=None, key=7, type="default", help=None, autocomplete=None, on_change=None, placeholder="compétence 2", disabled=False))
    st.session_state["nouveau_perso"]["bonus_competence_2"]=int(st.sidebar.text_input("Bonus compétence 2", value=0, max_chars=None, key=8, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_competence_3"]=(st.sidebar.text_input("Nom compétence 3",  max_chars=None, key=9, type="default", help=None, autocomplete=None, on_change=None, placeholder="compétence 3", disabled=False))
    st.session_state["nouveau_perso"]["bonus_competence_3"]=int(st.sidebar.text_input("Bonus compétence 3", value=0, max_chars=None, key=10, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_competence_4"]=(st.sidebar.text_input("Nom compétence 4", max_chars=None, key=11, type="default", help=None, autocomplete=None, on_change=None, placeholder="compétence 4", disabled=False))
    st.session_state["nouveau_perso"]["bonus_competence_4"]=int(st.sidebar.text_input("Bonus compétence 4", value=0, max_chars=None, key=12, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_competence_5"]=(st.sidebar.text_input("Nom compétence 5", max_chars=None, key=27, type="default", help=None, autocomplete=None, on_change=None, placeholder="compétence 5", disabled=False))
    st.session_state["nouveau_perso"]["bonus_competence_5"]=int(st.sidebar.text_input("Bonus compétence 5", value=0, max_chars=None, key=28, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    #dons
    st.sidebar.write("## Dons") 

    st.session_state["nouveau_perso"]["nom_don_1"]=(st.sidebar.text_input("Nom don 1",  max_chars=None, key=13, type="default", help=None, autocomplete=None, on_change=None, placeholder='don 1', disabled=False))
    st.session_state["nouveau_perso"]["cout_don_1"]=int(st.sidebar.text_input("Coût don 1", value=0, max_chars=None, key=14, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_don_2"]=(st.sidebar.text_input("Nom don 2",  max_chars=None, key=15, type="default", help=None, autocomplete=None, on_change=None, placeholder='don 2', disabled=False))
    st.session_state["nouveau_perso"]["cout_don_2"]=int(st.sidebar.text_input("Coût don 2", value=0, max_chars=None, key=16, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_don_3"]=(st.sidebar.text_input("Nom don 3",  max_chars=None, key=17, type="default", help=None, autocomplete=None, on_change=None, placeholder='don 3', disabled=False))
    st.session_state["nouveau_perso"]["cout_don_3"]=int(st.sidebar.text_input("Coût don 3", value=0, max_chars=None, key=18, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))

    st.session_state["nouveau_perso"]["nom_don_4"]=(st.sidebar.text_input("Nom don 4",  max_chars=None, key=19, type="default", help=None, autocomplete=None, on_change=None, placeholder='don 4', disabled=False))
    st.session_state["nouveau_perso"]["cout_don_4"]=int(st.sidebar.text_input("Coût don 4", value=0, max_chars=None, key=20, type="default", help=None, autocomplete=None, on_change=None, placeholder=None, disabled=False))



#TITRE
try:
    if st.session_state["data_perso"]["nom_personnage"]!='':
        titre_page=st.session_state["data_perso"]["nom_personnage"]
    else:
        titre_page="Fiche de personnage"
except:
    titre_page='Fiche de personnage'
st.title(titre_page)
st.write('''
   
''')
st.write('''
   
''')


#Buttons effect

def f_plushp():
    st.session_state["data_perso"]["PV"]+=1

def f_minushp():
    st.session_state["data_perso"]["PV"]-=1

def f_pluspsy():
    st.session_state["data_perso"]["PSY"]+=1

def f_minuspsy():
    st.session_state["data_perso"]["PSY"]-=1

# Fiche perso
left_column, right_column = st.columns((1,1))

with left_column:
    stats_tab="| PV | "+str(st.session_state["data_perso"]["PV"])+" / "+str(st.session_state["data_perso"]["max_PV"])+" |\n"
    stats_tab+="""| ----------- | ----------- |
"""
    stats_tab+="| **PSY** | **"+str(st.session_state["data_perso"]["PSY"])+" / "+str(st.session_state["data_perso"]["max_PSY"])+"** |\n"
    stats_tab+="| **Physique** | **"+str(st.session_state["data_perso"]["Physique"])+"** |\n"
    stats_tab+="| **Social** | **"+str(st.session_state["data_perso"]["Social"])+"** |\n"
    stats_tab+="| **Mental** | **"+str(st.session_state["data_perso"]["Mental"])+"** |\n"
    st.write(stats_tab)

    competences_tab="| Compétence | Bonus |\n"
    competences_tab+="| ----------- | ----------- |\n"
    if(st.session_state["data_perso"]["nom_competence_1"]!=''):
        competences_tab+="| "+str(st.session_state["data_perso"]["nom_competence_1"])+" | "+str(st.session_state["data_perso"]["bonus_competence_1"])+" |\n"
    if(st.session_state["data_perso"]["nom_competence_2"]!=''):
        competences_tab+="| "+str(st.session_state["data_perso"]["nom_competence_2"])+" | "+str(st.session_state["data_perso"]["bonus_competence_2"])+" |\n"
    if(st.session_state["data_perso"]["nom_competence_3"]!=''):
        competences_tab+="| "+str(st.session_state["data_perso"]["nom_competence_3"])+" | "+str(st.session_state["data_perso"]["bonus_competence_3"])+" |\n"
    if(st.session_state["data_perso"]["nom_competence_4"]!=''):
        competences_tab+="| "+str(st.session_state["data_perso"]["nom_competence_4"])+" | "+str(st.session_state["data_perso"]["bonus_competence_4"])+" |\n"
    if(st.session_state["data_perso"]["nom_competence_5"]!=''):
        competences_tab+="| "+str(st.session_state["data_perso"]["nom_competence_5"])+" | "+str(st.session_state["data_perso"]["bonus_competence_5"])+" |\n"
    
    st.write(competences_tab)

    dons_tab="| Don | Coût |\n"
    dons_tab+="| ----------- | ----------- |\n"
    if(st.session_state["data_perso"]["nom_don_1"]!=''):
        dons_tab+="| "+str(st.session_state["data_perso"]["nom_don_1"])+" | "+str(st.session_state["data_perso"]["cout_don_1"])+" |\n"
    if(st.session_state["data_perso"]["nom_don_2"]!=''):
        dons_tab+="| "+str(st.session_state["data_perso"]["nom_don_2"])+" | "+str(st.session_state["data_perso"]["cout_don_2"])+" |\n"
    if(st.session_state["data_perso"]["nom_don_3"]!=''):
        dons_tab+="| "+str(st.session_state["data_perso"]["nom_don_3"])+" | "+str(st.session_state["data_perso"]["cout_don_3"])+" |\n"
    if(st.session_state["data_perso"]["nom_don_4"]!=''):
        dons_tab+="| "+str(st.session_state["data_perso"]["nom_don_4"])+" | "+str(st.session_state["data_perso"]["cout_don_4"])+" |\n"
    st.write(dons_tab)


with right_column: 
    
    plushp=st.button("+1 PV",key=21,on_click =f_plushp)
    minushp=st.button("-1 PV",key=22,on_click =f_minushp)
    pluspsy=st.button("+1 PSY",key=23,on_click =f_pluspsy)
    minuspsy=st.button("-1 PSY",key=24,on_click =f_minuspsy)


# dll fiche de perso

stats_str_format = json.dumps(st.session_state["data_perso"])

if st.session_state["data_perso"]["nom_personnage"]!='':
    nom_perso=st.session_state["data_perso"]["nom_personnage"].replace(" ","_")
else:
    nom_perso='personnage_stats'

st.download_button(
    label="Télécharge ta fiche de personnage",
    file_name=nom_perso+".json",
    mime="application/json",
    data=stats_str_format,
)


# if plushp:
#     st.session_state["data_perso"]["PV"]+=1
#     plushp=False
# if minushp:
#     st.session_state["data_perso"]["PV"]-=1
#     minushp=False

# st.write(st.session_state.to_dict())
# st.write(st.session_state["data_perso"].keys())

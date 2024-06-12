import streamlit as st
import plotly.express as px
import mysql.connector as mc
import pandas as pd
from datetime import date

# definition de la fonction principale
def main():

    # configuration de la page
    st.set_page_config(page_title="Transfromateur 1", page_icon="📈")

    # connection à la base de données
    conn = mc.connect(
        host="localhost",
        database="natch_dex",
        user="root",
        passwd="")

    # créer un curseur
    cursor = conn.cursor()

    # créer sql pour selectionner la table transformateur 1
    cursor.execute("SELECT * FROM transformateur_1")

    # recuperation des données
    data = [ table[0] for table in cursor.fetchall()]

    # Convertir les données en DataFrame Pandas
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame(data, columns=columns)

    # création des differentes colonnes
    col1, col2, = st.columns(2)
    
    # courbe pour O2
    dioxygene = px.line(df, x="Date", y="O2")

    col1.plotly_chart(dioxygene)
    


    ################ entrer les données dans la base des données ###################
    if st.button("Ajouter Données"):

        Date = st.date_input("Choisissez une date", value=date(2023, 6, 12),
                            min_value=date(2020, 1, 1),
                            max_value=date(2025, 12, 31),
                            key="date_input",
                            help="Sélectionnez une date dans le calendrier")
        O2 = st.number_input(label="Dioxygène", min_value=0)
        CO2 = st.number_input(label="Dioxide de carbone", min_value=0)
        H2 = st.number_input(label="Dihydrogène", min_value=0)
        CH4 = st.number_input(label="Valeur du CH4", min_value=0)
        C2H6 = st.number_input(label="Valeur du C2H6", min_value=0)
        C2H4 = st.number_input(label="Valeur du C2H4", min_value=0)
        C2H2 = st.number_input(label="Valeur du C2H2", min_value=0)
        Tension_rupture = st.number_input(label="Tension de rupture", min_value=0)
        Eau = st.number_input(label="Valeur en eau", min_value=0)
        if st.button("Enregistrer"):
            # Insérer les données dans la base de données
            sql = "INSERT INTO transformateur_1(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")
    





if __name__=="__main__":
    main()
import streamlit as st
import plotly.express as px
import mysql.connector as mc
import pandas as pd
from datetime import date

# definition de la fonction principale
def main():

    # configuration de la page
    st.set_page_config(page_title="Transfromateur 2", page_icon="📈")

    # connection à la base de données
    conn = mc.connect(
        host="localhost",
        database="natch_dex",
        user="root",
        passwd="")

    # créer un curseur
    cursor = conn.cursor()

    # créer sql pour selectionner la table transformateur 1
    cursor.execute("SELECT * FROM transformateur_2")

    # recuperation des données
    data = [ list(table) for table in cursor.fetchall()]

    # Convertir les données en DataFrame Pandas
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame(data, columns=columns)

    # création des differentes colonnes
    col1, col2, = st.columns(2)
    
    # courbe pour O2
    dioxygene = px.line(df, x="Date", y="O2")
    col1.plotly_chart(dioxygene)

    # courbe pour dioxyde de carbone
    co2 = px.line(df, x="Date", y="CO2")
    col2.plotly_chart(co2)

    # courbe pour dihydrogne
    hydrogene = px.line(df, x="Date", y="H2")
    col1.plotly_chart(hydrogene)

    # courbe pour ch4
    ch4 = px.line(df, x="Date", y="CH4")
    col2.plotly_chart(ch4)

    # courbe pour c2h6
    c2h6 = px.line(df, x="Date", y="C2H6")
    col1.plotly_chart(c2h6)

    # courbe pour c2h4
    c2h4 = px.line(df, x="Date", y="C2H4")
    col2.plotly_chart(c2h4)

    # courbe pour c2h2
    c2h2 = px.line(df, x="Date", y="C2H2")
    col1.plotly_chart(c2h2)

    # courbe pour tension de rupture
    rupture = px.line(df, x="Date", y="Tension_Rupture")
    col2.plotly_chart(rupture)

    # courbe pour eau
    eau = px.line(df, x="Date", y="Eau")
    col1.plotly_chart(eau)

if __name__=="__main__":
    main()
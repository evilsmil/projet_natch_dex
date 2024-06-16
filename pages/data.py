import streamlit as st
import plotly.express as px
import mysql.connector as mc
import pandas as pd
from datetime import date

# definition de la fonction principale
def main():

    # configuration de la page
    st.set_page_config(page_title="Configuration", page_icon="📈")
     
     
    # créer la liste des transformateurs
    liste_transformateur = ["transformateur_1", "transformateur_2", "transformateur_3",
                                "transformateur_4", "transformateur_5", "transformateur_6",
                                "transformateur_7", "transformateur_8"]
        
    boutton = st.selectbox("Choisir le transformateur", liste_transformateur)
    

    ################ entrer les données dans la base des données ###################
    Date = st.date_input("Choisissez une date", value=date(2023, 6, 12),
                        min_value=date(2020, 1, 1),
                        max_value=date(2025, 12, 31),
                        key="date_input",
                        help="Sélectionnez une date dans le calendrier", 
                        format="DD/MM/YYYY")
    O2 = st.number_input(label="Dioxygène", min_value=0)
    CO2 = st.number_input(label="Dioxide de carbone", min_value=0)
    H2 = st.number_input(label="Dihydrogène", min_value=0)
    CH4 = st.number_input(label="Valeur du CH4", min_value=0)
    C2H6 = st.number_input(label="Valeur du C2H6", min_value=0)
    C2H4 = st.number_input(label="Valeur du C2H4", min_value=0)
    C2H2 = st.number_input(label="Valeur du C2H2", min_value=0)
    Tension_rupture = st.number_input(label="Tension de rupture", min_value=0)
    Eau = st.number_input(label="Valeur en eau", min_value=0)


    # connection à la base de données
    conn = mc.connect(
        host="localhost",
        database="natch_dex",
        user="root",
        passwd="")

    # créer un curseur
    cursor = conn.cursor()


    ########################## touche pour le transformateur 1 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_1":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_1")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)


    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_1(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")
        

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_1"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")



    ########################## touche pour le transformateur 2 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_2":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_2")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)

    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_2(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_2"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")



    ########################## touche pour le transformateur 3 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_3":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_3")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)


    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_3(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_3"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")



    ########################## touche pour le transformateur 4 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_4":

        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_4")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)

    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_4(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        
        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_4"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")



    ########################## touche pour le transformateur 5 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_5":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_5")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)


        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_5(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        
        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_5"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")


    ########################## touche pour le transformateur 2 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_6":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_6")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)

    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_6(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_6"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")


    ########################## touche pour le transformateur 7 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_7":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_7")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)

    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_7(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_7"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")



    ########################## touche pour le transformateur 8 ######################

    # créer une condition sur les boutton
    if boutton=="transformateur_8":
        # créer sql pour selectionner la table transformateur 1
        cursor.execute("SELECT * FROM transformateur_8")

        # recuperation des données
        data = [ list(table) for table in cursor.fetchall()]

        # Convertir les données en DataFrame Pandas
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame(data, columns=columns)

    
        # Insérer les données dans la base de données
        if st.button("Enregistrer")==True:
            sql = "INSERT INTO transformateur_8(Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, \
                Tension_rupture, Eau) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (Date, O2, CO2, H2, CH4, C2H6, C2H4, C2H2, Tension_rupture, Eau)
            cursor.execute(sql, values)
            conn.commit()
            st.success("Données enregistrées avec succès!")

        ############## supprimer les données dans la base de données ############
        # Ajout d'un bouton "Supprimer tout"
        if st.button("Supprimer toutes les données",type='primary', use_container_width=True):
            # Exécution de la requête SQL pour supprimer toutes les données
            sql = "DELETE FROM transformateur_8"
            cursor.execute(sql)
            conn.commit()

            st.success("Toutes les données ont été supprimées avec succès!")

if __name__=="__main__":
    main()
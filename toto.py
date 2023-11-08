
import streamlit as st

import snowflake.connector

def generate_create_user_sql(conn, user):
    sql = f"CREATE USER {user} PASSWORD = 'password';"
    return sql

def main():
    st.title("Formulaire de saisie d'une liste d'utilisateurs")
    user_list = st.text_input("Entrez une liste d'utilisateurs, séparés par des virgules")
    user_list = user_list.split(",")
    st.write("Liste d'utilisateurs :", user_list)

    conn = snowflake.connector.connect(
        user='<user>',
        password='<password>',
        account='<account>',
        warehouse='<warehouse>',
        database='<database>',
        schema='<schema>'
    )

    for user in user_list:
        st.write(f"Création de l'utilisateur {user}...")
        sql = generate_create_user_sql(conn, user)
        st.code(sql, language='sql')

    conn.close()

if __name__ == "__main__":
    main()


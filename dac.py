import psycopg2
import streamlit as st


def connect():

    try:
        return psycopg2.connect(
            host=st.secrets["postgres"]["host"],
            port=st.secrets["postgres"]["port"],
            database=st.secrets["postgres"]["database"],
            user=st.secrets["postgres"]["user"],
            password=st.secrets["postgres"]["password"],
            sslmode=st.secrets["postgres"].get("sslmode", "require"),
            connect_timeout=10,
        )

    except (psycopg2.Error, KeyError) as error:
        st.error(f"Database connection failed: {error}")
        return None


def add_answers(age, gender, programming_language, favourite_color):

    connection = connect()
    if connection is None:
        return False

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    " INSERT INTO questioned (age, gender, planguage, favcolor) VALUES (%s, %s, %s, %s);", (age,  gender,  programming_language, favourite_color) 
                    )

        return True

    except psycopg2.Error as error:
        st.error(f"Could not save the answers: {error}")
        return False

    finally:
        connection.close()


def show_answers():

    connection = connect()
    if connection is None:
        return []

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute( "SELECT id, age, gender,  planguage, favcolor FROM questioned ORDER BY id;")

                return cursor.fetchall()

    except psycopg2.Error as error:
        st.error(f"Could not load the answers: {error}")
        return []

    finally:
        connection.close()


def clear_answers():

    connection = connect()
    if connection is None:
        return False

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE questioned RESTART IDENTITY;")
        return True

    except psycopg2.Error as error:
        st.error(f"Could not clear the answers: {error}")
        return False

    finally:
        connection.close()
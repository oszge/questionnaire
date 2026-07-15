import streamlit as st
import pandas as pd
import dac


st.set_page_config(
    page_title="Questionnaire"
    )

st.header(
    "Questioning Form", width="stretch", text_alignment="center"
)

def submit_answers():
    age = st.session_state.age
    gender = st.session_state.gender
    p_language = st.session_state.language
    fav_color = st.session_state.color

    if age == "-- Select age --":
        st.error("Please select your age!", icon="🚨")
    elif gender == "-- Select gender --":
        st.error("Please select a gender!", icon="🚨")
    elif p_language == "-- Select programming language --":
        st.error("Please select a programming language!", icon="🚨")
    elif fav_color == "-- Select color --":
        st.error("Please select a favourite color!", icon="🚨")
    else:
        age=int(age)
        dac.add_answers(age, gender, p_language, fav_color)

        with open("answers.txt", "a", encoding="utf-8") as f:
            f.write(f"{age}, {gender}, {p_language}, {fav_color}\n")

        st.session_state.submitted = True

def clear_answers():
    dac.clear_answers()
    open("answers.txt", "w").close()

def reset_answers():
    st.session_state.age = "-- Select age --"
    st.session_state.gender = "-- Select gender --"
    st.session_state.language = "-- Select language --"
    st.session_state.color = "-- Select color --"


age = st.selectbox('Age', ["-- Select age --"] + list(range(1, 121)), key="age")
gender = st.selectbox("Gender: ",("-- Select gender --", "Male", "Female", "Else"), key="gender")
p_language = st.selectbox("Programming language:", ("-- Select programming language --", "Python", "C#", "C++", "Java", "Javascript"), key="language")
fav_color = st.selectbox("Favourite color:", ("-- Select color --", "White", "Black", "Orange", "Yellow", "Grey", "Purple", "Pink", "Blue", "Turqoise", "Green", "Brown"), key="color")

submit, reset, clear = st.columns([1,1,1])

with submit:
    if st.button(
        "Submit answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=submit_answers
        ):
        if st.session_state.get("submitted", False):
            st.success("Successfully submitted your answers!", width="stretch", icon="🔥")
            st.session_state.submitted = False
            
with reset:
    if st.button(
        "Reset answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=reset_answers
        ):
        st.success("Elements successfully set back to default value.", width="stretch", icon="🔥")

with clear:
    if st.button(
        "Clear answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=clear_answers
        ):
        st.success("Successfully cleared the previous answers!", width="stretch", icon="🔥")

answers = dac.show_answers()
df = pd.DataFrame(
    answers, columns=["ID", "Age", "Gender", "Programming Language", "Favourite Color"]
    )
st.dataframe(df)
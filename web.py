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

    st.session_state.submitted = False

    if age == "-- Select age --":
        st.session_state.error_message= ("Please select your age!")
        return
    elif gender == "-- Select gender --":
        st.session_state.error_message = ("Please select a gender!")
        return
    elif p_language == "-- Select programming language --":
        st.session_state.error_message = ("Please select a programming language!")
        return
    elif fav_color == "-- Select color --":
        st.session_state.error_message = ("Please select your color!")
        return
    else:
        age=int(age)
        dac.add_answers(age, gender, p_language, fav_color)
        st.session_state.submitted = True

def clear_answers():

    cleared = dac.clear_answers()
    st.session_state.cleared = cleared

def reset_answers():
    st.session_state.age = "-- Select age --"
    st.session_state.gender = "-- Select gender --"
    st.session_state.language = "-- Select language --"
    st.session_state.color = "-- Select color --"
    st.session_state.reset_completed = True


age = st.selectbox('Age', ["-- Select age --"] + list(range(1, 121)), key="age")
gender = st.selectbox("Gender: ",("-- Select gender --", "Male", "Female", "Else"), key="gender")
p_language = st.selectbox("Programming language:", ("-- Select programming language --", "Python", "C#", "C++", "Java", "Javascript"), key="language")
fav_color = st.selectbox("Favourite color:", ("-- Select color --", "White", "Black", "Orange", "Yellow", "Grey", "Purple", "Pink", "Blue", "Turqoise", "Green", "Brown"), key="color")

submit, reset, clear = st.columns([1,1,1])

with submit:
    st.button(
        "Submit answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=submit_answers
        )
            
with reset:
    st.button(
        "Reset answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=reset_answers
        )

with clear:
    st.button(
        "Clear answers", 
        width="content", 
        type="primary", 
        use_container_width=True, 
        on_click=clear_answers
        )

if st.session_state.get("submitted", False):
    st.success("Successfully submitted your answers!")
    st.session_state.submitted = False

if st.session_state.get("error_message"):
    st.error(st.session_state.error_message)
    st.session_state.error_message = None

if st.session_state.get("reset_completed", False):
    st.success("Elements successfully set back to default value.")
    st.session_state.reset_completed = False

if st.session_state.get("cleared", False):
    st.success("Successfully cleared the previous answers!")
    st.session_state.cleared = False

answers = dac.show_answers()

df = pd.DataFrame(
    answers, columns=["ID", "Age", "Gender", "Programming Language", "Favourite Color"]
    )

st.subheader("Submitted answers")
st.dataframe(df)
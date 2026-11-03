import streamlit as st

st.title("⚙️ Setup")

# Fake storage until the database exists
if "settings" not in st.session_state:
    st.session_state.settings = {"university": "Default (10-point CGPA)", "min_attendance": 75}
if "subjects_list" not in st.session_state:
    st.session_state.subjects_list = []

st.subheader("Your college")
st.session_state.settings["university"] = st.selectbox(
    "University",
    ["Default (10-point CGPA)", "My University"],
)
st.session_state.settings["min_attendance"] = st.number_input(
    "Minimum attendance %", value=75, min_value=1, max_value=100
)

st.subheader("Add a subject")
with st.form("add_subject", clear_on_submit=True):
    name = st.text_input("Subject name")
    credits = st.number_input("Credits", min_value=1, max_value=10, value=4)
    semester = st.number_input("Semester", min_value=1, max_value=12, value=1)
    submitted = st.form_submit_button("Add subject")
    if submitted and name:
        st.session_state.subjects_list.append(
            {"name": name, "credits": credits, "semester": semester}
        )
        st.success(f"Added {name}")

st.subheader("Your subjects")
if st.session_state.subjects_list:
    st.table(st.session_state.subjects_list)
else:
    st.info("No subjects yet. Add one above.")
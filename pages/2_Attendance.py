import streamlit as st
from core.attendance import attendance_percent, classes_can_skip, classes_needed

st.title("📝 Attendance")

# Fake data until the database exists
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Maths": {"attended": 30, "total": 36},
        "Physics": {"attended": 20, "total": 30},
        "Programming": {"attended": 28, "total": 30},
    }

min_percent = st.number_input("Minimum attendance %", value=75, min_value=1, max_value=100)
subject = st.selectbox("Subject", list(st.session_state.subjects.keys()))
data = st.session_state.subjects[subject]

col1, col2 = st.columns(2)
if col1.button("✅ Mark present"):
    data["attended"] += 1
    data["total"] += 1
if col2.button("❌ Mark absent"):
    data["total"] += 1

m1, m2, m3 = st.columns(3)
m1.metric("Attendance", f"{attendance_percent(data['attended'], data['total'])}%")
m2.metric("Classes you can skip", classes_can_skip(data["attended"], data["total"], min_percent))
m3.metric("Classes needed", classes_needed(data["attended"], data["total"], min_percent))
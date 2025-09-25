import streamlit as st
import json

st.title("CG Checklist App")
st.markdown("This app displays a checklist based on the CG Milestone Process Outline.")

# Load checklist structure
try:
    with open("checklist_structure.json", "r") as f:
        checklist = json.load(f)
except Exception as e:
    st.error(f"Error loading checklist: {e}")
    checklist = {}

# Display checklist
if checklist:
    st.subheader("Checklist Items")
    completed = []
    for item in checklist.get("milestones", []):
        if st.checkbox(item):
            completed.append(item)

    if completed:
        st.success(f"Completed {len(completed)} item(s):")
        for item in completed:
            st.write(f"- {item}")
    else:
        st.info("No items completed yet.")
else:
    st.warning("Checklist is empty.")

import streamlit as st

# Title and description
st.title("CG Checklist App")
st.markdown("Welcome to your checklist app! Use this to track tasks, goals, or project steps.")

# Sample checklist items
tasks = [
    "Define project goals",
    "Gather resources",
    "Build initial prototype",
    "Test functionality",
    "Deploy and share"
]

# Create checkboxes for each task
st.subheader("Your Checklist")
completed = []
for task in tasks:
    if st.checkbox(task):
        completed.append(task)

# Show completed tasks
if completed:
    st.success(f"✅ You've completed {len(completed)} task(s):")
    for task in completed:
        st.write(f"- {task}")
else:
    st.info("No tasks completed yet. Let's get started!")

# Optional: Add a text input to add new tasks (basic version)
st.subheader("Add a new task")
new_task = st.text_input("Enter a task:")
if new_task:
    st.write(f"📌 You added: {new_task} (Note: This won't save yet — we can add that feature next!)")

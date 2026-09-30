import streamlit as st
from datetime import datetime


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="My To-Do List",
    page_icon="✅",
    layout="centered"
)


# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: #EAF4FF;
}

.main-title {
    text-align: center;
    color: #243B53;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #627D98;
    font-size: 16px;
    margin-bottom: 20px;
}

.counter {
    text-align: center;
    color: #4A90E2;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 20px;
}

.task-box {
    background-color: white;
    padding: 12px;
    border-radius: 8px;
    margin-bottom: 8px;
    border: 1px solid #DCEBFF;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TASK STORAGE ----------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []


# ---------------- FUNCTIONS ----------------

def add_task(task_name, priority):

    task_name = task_name.strip()

    if task_name == "":
        st.warning("Please enter a task.")
        return

    new_task = {
        "name": task_name,
        "priority": priority,
        "completed": False,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    st.session_state.tasks.append(new_task)

    st.success("Task added successfully!")


def delete_task(task_number):

    if not st.session_state.tasks:
        st.warning("There are no tasks.")
        return

    st.session_state.tasks.pop(task_number)

    st.success("Task deleted successfully!")


def complete_task(task_number):

    if not st.session_state.tasks:
        st.warning("There are no tasks.")
        return

    st.session_state.tasks[task_number]["completed"] = (
        not st.session_state.tasks[task_number]["completed"]
    )


def clear_tasks():

    if not st.session_state.tasks:
        st.info("There are no tasks to clear.")
        return

    st.session_state.tasks.clear()

    st.success("All tasks cleared!")


# ---------------- TITLE ----------------

st.markdown(
    '<div class="main-title">MY TO-DO LIST</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Organize your tasks and stay productive'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- TASK COUNTER ----------------

total = len(st.session_state.tasks)

completed = sum(
    task["completed"]
    for task in st.session_state.tasks
)

remaining = total - completed

st.markdown(
    f'<div class="counter">'
    f'{remaining} Tasks Remaining &nbsp; • &nbsp; '
    f'{completed} Completed'
    f'</div>',
    unsafe_allow_html=True
)


# ---------------- INPUT AREA ----------------

with st.form("add_task_form"):

    task_name = st.text_input(
        "Task",
        placeholder="Enter your task here..."
    )

    priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"],
        index=1
    )

    add_button = st.form_submit_button(
        "＋ Add Task",
        use_container_width=True
    )

    if add_button:
        add_task(task_name, priority)


# ---------------- TASK LIST ----------------

st.subheader("📋 Your Tasks")


if len(st.session_state.tasks) == 0:

    st.info("No tasks yet. Add your first task above!")

else:

    # Display all tasks

    for number, task in enumerate(
        st.session_state.tasks,
        start=1
    ):

        if task["completed"]:
            status = "✅"
        else:
            status = "○"

        st.markdown(
            f"""
            <div class="task-box">
                <b>{number}. {status} {task["name"]}</b>
                <br>
                <small>
                Priority: <b>{task["priority"]}</b>
                &nbsp;&nbsp;|&nbsp;&nbsp;
                Date: {task["date"]}
                </small>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ---------------- SELECT TASK ----------------

    st.write("### Select a Task")

    task_options = []

    for number, task in enumerate(
        st.session_state.tasks,
        start=1
    ):
        task_options.append(
            f"{number}. {task['name']}"
        )

    selected_task = st.selectbox(
        "Choose a task",
        task_options
    )

    selected_number = task_options.index(
        selected_task
    )


    # ---------------- BUTTONS ----------------

    col1, col2, col3 = st.columns(3)


    # Complete button

    with col1:

        if st.button(
            "✓ Complete / Undo",
            use_container_width=True
        ):

            complete_task(selected_number)

            st.rerun()


    # Delete button

    with col2:

        if st.button(
            "🗑️ Delete",
            use_container_width=True
        ):

            delete_task(selected_number)

            st.rerun()


    # Clear button

    with col3:

        if st.button(
            "🧹 Clear All",
            use_container_width=True
        ):

            st.session_state.confirm_clear = True


# ---------------- CLEAR CONFIRMATION ----------------

if st.session_state.get("confirm_clear", False):

    st.warning(
        "Are you sure you want to clear all tasks?"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Yes, Clear All",
            use_container_width=True
        ):

            clear_tasks()

            st.session_state.confirm_clear = False

            st.rerun()


    with col2:

        if st.button(
            "Cancel",
            use_container_width=True
        ):

            st.session_state.confirm_clear = False

            st.rerun()

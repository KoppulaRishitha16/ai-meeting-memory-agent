import streamlit as st
from memory import store_memory, recall_memory

st.set_page_config(
    page_title="AI Meeting Memory Agent",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Meeting Memory Agent")
st.caption("Remember meetings. Recall commitments. Follow up intelligently.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Add Meeting Memory")

    meeting = st.text_area(
        "Enter your meeting notes",
        placeholder=(
            "Example: ABC Corp needs an analytics dashboard by Friday. "
            "They prefer email communication."
        ),
        height=180
    )

    if st.button("💾 Remember Meeting", use_container_width=True):
        if meeting.strip():
            try:
                store_memory(meeting)
                st.session_state["meeting_memory"] = meeting
                st.success("✅ Meeting remembered!")
            except Exception as e:
                st.error(f"Could not store memory: {e}")
        else:
            st.warning("Please enter meeting notes.")


with col2:
    st.subheader("🔎 Recall Meeting Information")

    query = st.text_input(
        "What do you want to remember?",
        placeholder="Example: What does ABC Corp need?"
    )

    if st.button("🧠 Recall", use_container_width=True):
        if query.strip():
            try:
                result = recall_memory(query)

                st.success("✅ Memory recalled!")
                st.info(str(result))

                st.session_state["recall_result"] = str(result)

            except Exception as e:
                st.error(f"Could not recall memory: {e}")
        else:
            st.warning("Enter a question.")


st.divider()

st.subheader("✉️ Follow-up Email")

if "recall_result" in st.session_state:
    memory = st.session_state["recall_result"]

    email = f"""Subject: Follow-up on our meeting

Hi ABC Corp Team,

Thank you for meeting with us.

Based on our discussion, I understand that you need an analytics dashboard by Friday and that email is your preferred communication method.

Please let me know if there are any additional requirements or updates.

Best regards,
Meeting Memory Agent
"""

    st.text_area(
        "Personalized follow-up",
        value=email,
        height=220
    )
else:
    st.info("Recall a meeting first to generate a personalized follow-up email.")
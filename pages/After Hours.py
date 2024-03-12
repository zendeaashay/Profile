import hmac
import streamlit as st


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()  # Do not continue if check_password is not True.

st.title("After Hours")

# Define the options for your interests
options = ['Trekking', 'Hyperloop Project', 'Surfing', 'Photography']
selected_option = st.selectbox("Select Interest", options)

# Display the content based on the selected option
if selected_option == 'Trekking':
    st.subheader("Trekking")


elif selected_option == 'Hyperloop Project':
    st.subheader("Hyperloop Project")

elif selected_option == 'Surfing':
    st.subheader("Surfing")

elif selected_option == 'Photography':
    st.subheader("Photography")


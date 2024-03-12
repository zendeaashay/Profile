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

# Define the options for your interests and their corresponding images or icons
interests = {
    'Trekking': 'trekking_icon.png',
    'Hyperloop Project': 'hyperloop_icon.png',
    'Surfing': 'surfing_icon.png',
    'Photography': 'photography_icon.png'
}

# Track the current selected option
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = None

# Create a horizontal line of buttons with icons
cols = st.columns(len(interests))
for index, (interest, icon) in enumerate(interests.items()):
    with cols[index]:
        # You can use an image as a button by wrapping st.image in st.button
        if st.button(interest):
            st.session_state['selected_option'] = interest
        st.image(icon, width=100, caption=interest)

# Display the content based on the selected option
selected_option = st.session_state['selected_option']
if selected_option == 'Trekking':
    st.subheader("Trekking")
    # Content for Trekking...

elif selected_option == 'Hyperloop Project':
    st.subheader("Hyperloop Project")
    # Content for Hyperloop Project...

elif selected_option == 'Surfing':
    st.subheader("Surfing")
    # Content for Surfing...

elif selected_option == 'Photography':
    st.subheader("Photography")
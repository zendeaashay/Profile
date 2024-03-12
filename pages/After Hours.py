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
# Custom styling for images to ensure they all display the same size
st.markdown("""
    <style>
    .interest-image {
        height: 150px; /* or any other fixed height */
        width: auto;
        object-fit: cover; /* this will ensure the aspect ratio is maintained */
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)
# Define the options for your interests and their corresponding images or icons
interests = {
    'Trekking': 'photos/trek/Image.jpeg',
    'Hyperloop Project': 'photos/hyp/3.png',
    'Surfing': 'photos/surf/1 DSC_0055.JPG',
    'Photography': 'photos/photo/21.jpg'
}

# Define experiences for each interest
experiences = {
    'Trekking': "Your experience description for Trekking...",
    'Hyperloop Project': "Your experience description for Hyperloop Project...",
    'Surfing': "Your experience description for Surfing...",
    'Photography': "Your experience description for Photography..."
}

# Track the current selected option
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = 'Trekking'  # Set a default selection

# Create a horizontal line of buttons with images
cols = st.columns(len(interests))
for index, (interest, icon) in enumerate(interests.items()):
    with cols[index]:
        if st.button(interest):
            st.session_state['selected_option'] = interest
        # Make all images the same size
        st.image(icon, use_column_width=False)

# Display the content based on the selected option
selected_option = st.session_state['selected_option']
if selected_option:
    st.subheader(selected_option)

    # Display a container with the experience paragraph
    st.markdown(f"""
    <div style="background-color: rgba(255, 255, 255, 0.8); margin: 10px 0; padding: 20px; border-radius: 10px;">
        <p>{experiences[selected_option]}</p>
    </div>
    """, unsafe_allow_html=True)
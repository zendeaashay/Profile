
import streamlit as st

# Function to convert Google Drive sharing URL to direct link
def get_gdrive_directlink(file_id):
    return f"https://drive.google.com/uc?id={file_id}&export=media"

# List of Google Drive file IDs for your photos and videos
file_ids = [
    "1A4bWe6W-KhMRCzN1j67UWFoAvcBtKUph",  # Add the rest of your file IDs here
    # ... more file IDs
]

# Convert file IDs to direct links
photo_urls = [get_gdrive_directlink(file_id) for file_id in file_ids]

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
    'Trekking': 'image.jpg',
    'Hyperloop Project': 'photos/hyp/3.png',
    'Surfing': 'photos/surf/1 DSC_0055.JPG',
    'Photography': 'photos/photo/21.jpg'
}

# Define experiences for each interest
experiences = {
    'Trekking': ["""I've found my greatest adventures on the slopes of the Himalayas, trading the comfort of the familiar for the thrill of the ascent. Trekking isn't just a hobby; it's a series of moments where each step reveals a new horizon and a test of my own mettle. From the impromptu snow sculptures—my chilly high-altitude tributes—to the quiet companionship of trail dogs and the cheer of local guides, every trek is a story etched in snow.

Up there, where the air is crisp and the skies a clear blue canvas, the mountains challenge me, the cold invigorates me, and the journey transforms me. Through the camaraderie with fellow hikers and the silent solidarity of shared struggles, I've discovered that the summit is just a bonus. It's the laughter, the grit, and the unexpected detours that truly chart my love for the trek. """, ['photos/trek/Image.jpeg', 'photos/trek/20220110_095542.png', 'photos/trek/P1380367.JPG', 'photos/trek/P1380563.JPG', 'photos/trek/P1380186.JPG', 'photos/trek/P1370805.JPG', 'photos/trek/P1370726.MOV']],
    'Hyperloop Project': [" ", ['photos/hyp/1.png', 'photos/hyp/2.png', 'photos/hyp/3.png', 'photos/hyp/4.png']],
    'Surfing': [" ", ['photos/surf/1 DSC_0055.JPG', 'photos/surf/3 bDSC_0277.JPG', 'photos/surf/4 DSC_0426.JPG', 'photos/surf/5 DSC_0780.JPG',
        'photos/surf/6 DSC_0944.JPG',
        'photos/surf/7 DSC_0183.JPG',
        'photos/surf/8 DSC_0423.JPG',
        'photos/surf/8 DSC_0423~2.JPG',
        'photos/surf/9 DSC_0708.JPG',
        'photos/surf/10 DSC_0805.JPG',
        'photos/surf/10 DSC_0805~2.JPG']],
    'Photography': [" ", ['photos/photo/29.jpg', 'photos/photo/30.mp4', 'photos/photo/P1010768.JPG', 'photos/photo/P1010774.JPG', 'photos/photo/P1010800.JPG', 'photos/photo/P1010825.JPG', 'photos/photo/P1010826.JPG', 'photos/photo/1.jpg', 'photos/photo/01.jpg', 'photos/photo/2.jpg', 'photos/photo/3.jpg', 'photos/photo/5.jpg', 'photos/photo/6.jpg', 'photos/photo/7.jpg', 'photos/photo/15.jpg', 'photos/photo/18.jpg', 'photos/photo/21.jpg', 'photos/photo/22.jpg', 'photos/photo/23.jpg', 'photos/photo/24.jpg']],
}

# Track the current selected option
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = None

# Create a horizontal line of buttons with the representative icon for each interest
cols = st.columns(len(interests))
for index, (interest, icon) in enumerate(interests.items()):
    with cols[index]:
        if st.button(interest):
            st.session_state['selected_option'] = interest
        # Show only the representative icon here, not the slideshow
        st.image(icon, width=100)


if 'image_index' not in st.session_state:
    st.session_state['image_index'] = 0

# Define the navigation functions and bind them to the session state
def previous_image():
    st.session_state['image_index'] = (st.session_state['image_index'] - 1) % len(trek_images)

def next_image():
    st.session_state['image_index'] = (st.session_state['image_index'] + 1) % len(trek_images)

st.session_state['previous_image'] = previous_image
st.session_state['next_image'] = next_image
# Define your button styles and events
prev_button = """
    <button style='font-size: 20px;' onclick='previous_image()'>◀</button>
"""

next_button = """
    <button style='font-size: 20px;' onclick='next_image()'>▶</button>
"""
# Initialize image_index on first run
if 'image_index' not in st.session_state:
    st.session_state['image_index'] = 0

selected_option = st.session_state.get('selected_option')
if selected_option:
    st.subheader(selected_option)

    if selected_option == 'Trekking':
        trek_description, trek_images = experiences[selected_option]
        st.markdown(trek_description, unsafe_allow_html=True)

        # Create Previous and Next buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                previous_image()

        with col2:
            if st.button("Next"):
                next_image()

        # Get the current image or video
        current_media = trek_images[st.session_state['image_index']]

        # Check if the current media is a video
        if current_media.endswith('.MOV'):
            st.video(current_media)
        else:
            st.image(current_media, use_column_width=True)
def previous_surf_image():
    surf_images = experiences['Surfing'][1]
    st.session_state['surf_image_index'] = (st.session_state['surf_image_index'] - 1) % len(surf_images)

def next_surf_image():
    surf_images = experiences['Surfing'][1]
    st.session_state['surf_image_index'] = (st.session_state['surf_image_index'] + 1) % len(surf_images)

if 'surf_image_index' not in st.session_state:
    st.session_state['surf_image_index'] = 0  # Initialize it with the first image index

# Then in your app where you are displaying the images:

if selected_option == 'Surfing':
        surf_description, surf_images = experiences[selected_option]
        st.markdown(surf_description, unsafe_allow_html=True)

        # Create Previous and Next buttons for surfing
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                previous_surf_image()

        with col2:
            if st.button("Next"):
                next_surf_image()

        # Display the current surfing image
        st.image(surf_images[st.session_state['surf_image_index']], use_column_width=True)        
# Navigation functions for Hyperloop Project
def previous_hyperloop_image():
    hyperloop_images = experiences['Hyperloop Project'][1]
    st.session_state['hyperloop_image_index'] = (st.session_state['hyperloop_image_index'] - 1) % len(hyperloop_images)

def next_hyperloop_image():
    hyperloop_images = experiences['Hyperloop Project'][1]
    st.session_state['hyperloop_image_index'] = (st.session_state['hyperloop_image_index'] + 1) % len(hyperloop_images)

if 'hyperloop_image_index' not in st.session_state:
    st.session_state['hyperloop_image_index'] = 0  # Initialize it with the first image index

# Display function for the selected option
def display_selected_option(selected_option):
    if selected_option == 'Trekking':
        trek_description, trek_images = experiences[selected_option]
        st.markdown(trek_description, unsafe_allow_html=True)
        # ... (your existing trekking display code)

    elif selected_option == 'Surfing':
        surf_description, surf_images = experiences[selected_option]
        st.markdown(surf_description, unsafe_allow_html=True)
        # ... (your existing surfing display code)

    elif selected_option == 'Hyperloop Project':
        hyperloop_description, hyperloop_images = experiences[selected_option]
        st.markdown('Our design was selected by the European Hyperloop Competition! Check out this [Instagram Post](https://www.instagram.com/p/CY8vJVKNu0q/?hl=es-la)', unsafe_allow_html=True)

        # Create Previous and Next buttons for Hyperloop Project
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous", on_click=previous_hyperloop_image):
                pass

        with col2:
            if st.button("Next", on_click=next_hyperloop_image):
                pass

        # Display the current Hyperloop image
        current_image = hyperloop_images[st.session_state['hyperloop_image_index']]
        st.image(current_image, use_column_width=True)

    
# Check if the 'photo_image_index' is in the session state, otherwise initialize it
if 'photo_image_index' not in st.session_state:
    st.session_state['photo_image_index'] = 0

# Define navigation functions for Photography
def previous_photo_image():
    st.session_state['photo_image_index'] = (st.session_state['photo_image_index'] - 1) % len(experiences['Photography'][1])

def next_photo_image():
    st.session_state['photo_image_index'] = (st.session_state['photo_image_index'] + 1) % len(experiences['Photography'][1])

# Display function for the Photography section
def display_photography():
    selected_option = st.session_state.get('selected_option')
    if selected_option == 'Photography':
        photo_description, photo_media = experiences[selected_option]
        st.markdown(photo_description, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous Photo"):
                previous_photo_image()
        with col2:
            if st.button("Next Photo"):
                next_photo_image()
        
        current_media = photo_media[st.session_state['photo_image_index']]
        if current_media.endswith('.MOV') or current_media.endswith('.mp4'):
            st.video(current_media)
        else:
            st.image(current_media, use_column_width=True)

# Main display logic
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Photography':
        display_photography()
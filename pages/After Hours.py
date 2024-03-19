
import streamlit as st


st.title("Take a look at my post work hours")
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
    'loopMIT': 'photos/hyp/3.png',
    'Surfing': 'photos/surf/1 DSC_0055.JPG',
    'Snaps': 'photos/photo/21.jpg',
    'Tony Hawk': 'photos/hawk/WSBC0461.JPG',
    'Fireflies': 'photos/fire/P1280437.JPG',
    'Terrace': 'photos/terr/P1360084.JPG',
    'Paintings': 'photos/Paint/6.jpg'
}


# Define experiences for each interest
experiences = {
    'Trekking': ["""I've found my greatest adventures on the slopes of the Himalayas, trading the comfort of the familiar for the thrill of the ascent. Trekking isn't just a hobby; it's a series of moments where each step reveals a new horizon and a test of my own mettle. From the impromptu snow sculptures—my chilly high-altitude tributes—to the quiet companionship of trail dogs and the cheer of local guides, every trek is a story etched in snow.

Up there, where the air is crisp and the skies a clear blue canvas, the mountains challenge me, the cold invigorates me, and the journey transforms me. Through the camaraderie with fellow hikers and the silent solidarity of shared struggles, I've discovered that the summit is just a bonus. It's the laughter, the grit, and the unexpected detours that truly chart my love for the trek. """, ['photos/trek/Image.jpeg', 'photos/trek/1.JPEG', 'photos/trek/2.JPG', 'photos/trek/3.JPG', 'photos/trek/4.JPG', 'photos/trek/5.JPG', 'photos/trek/6.JPG', 'photos/trek/20220110_095542.png', 'photos/trek/P1380367.JPG', 'photos/trek/P1380563.JPG', 'photos/trek/P1380186.JPG', 'photos/trek/P1370805.JPG', 'photos/trek/P1370726.MOV']],
    'loopMIT': ["""Diving into the vanguard of transport innovation, my tenure with the Hyperloop project represented a foray into the pulsating heart of high-speed, sustainable mobility. At the confluence of visionary innovation and grounded pragmatism, the endeavor was a vibrant testament to the boundless reaches of human creativity, relentlessly challenging the conventional confines of possibility.

During my journey with LoopMIT at the Manipal Institute of Technology, spanning from February 2019 to July 2021, I was privileged to co-lead the Vehicle Dynamics Department. Within this cadre of 20 adept students, we partiicipated in SpaceX's prestigious Hyperloop competition.

My contributions were multifaceted and profound:

Innovation in Motion: I was instrumental in the ingenious design and precision engineering of our Hyperloop pod's suspension system and chassis. Employing magnetic levitation technology, we minimized drag and friction within a vacuum tunnel, propelling our design into the competition's final echelon.

Mentorship and Leadership: I spearheaded the creation of an exhaustive mentoring program for novices, meticulously designed to bolster their competencies in research methodologies and analysis simulations. This initiative not only fostered a culture of continuous learning but also entailed the adept management of the department's fiscal resources and the diligent documentation of our team's evolutionary trajectory.

Technological Mastery: My proficiency with advanced engineering tools such as Autodesk Fusion360 and SolidWorks was pivotal. Through these platforms, I executed intricate designs of the Hyperloop pod and conducted comprehensive motion analyses, thereby enhancing the design's efficiency and ensuring operational integrity.

Aerodynamic Excellence: I guided the exploration and application of sophisticated computational fluid dynamics and aerodynamic simulations, culminating in a significant 16% decrement in aerodynamic drag. This optimization was instrumental in augmenting the pod's velocity, a critical factor in our competitive arsenal.

Collaborative Synergy: I orchestrated the harmonious integration of the pod's mechanical, electrical, and software subsystems, leading a cross-functional team to surpass the competition's benchmarks with a prototype that epitomized seamless functionality.

Fiscal Acumen: My strategic foresight in fundraising was demonstrated by securing $5,000 in sponsorships and procuring state-of-the-art components from tech conglomerates, thereby fueling the advanced development of our Hyperloop prototype.

In essence, my odyssey with the Hyperloop project was a confluence of engineering brilliance, collaborative synergy, and visionary leadership, collectively steering us toward what could be the dawn of a new era in transportation.
""", ['photos/hyp/1.png', 'photos/hyp/2.png', 'photos/hyp/3.png', 'photos/hyp/4.png']],
    'Surfing': ["Surfing, for me, is about freedom. It's just me and the waves, and maybe a few good friends when they decide to wake up early enough. Each swell is a new challenge; no two rides are ever the same, which is kind of like life, I guess. I like chasing that sweeping rush, the moment where everything clicks and I'm gliding across the water like it's second nature. Sure, I wipe out sometimes, but where's the fun without a few salty spills? It's all part of the adventure. ", ['photos/surf/5 DSC_0780.JPG', 'photos/surf/8 DSC_0423~2.JPG', 'photos/surf/1 DSC_0055.JPG', 'photos/surf/3 bDSC_0277.JPG', 'photos/surf/4 DSC_0426.JPG', 
        'photos/surf/6 DSC_0944.JPG',
        'photos/surf/7 DSC_0183.JPG',
        'photos/surf/9 DSC_0708.JPG',
        'photos/surf/10 DSC_0805~2.JPG']],
    'Snaps': ["I love to take my camera out and just capture what catches my eye. There's something awesome about getting the perfect shot of a wild animal or a really cool view. It's like I get to freeze a piece of that moment and keep it. Whether it’s a tiger lounging around or a beautiful sunset, if it looks cool to me, I’ll snap it. Simple as that. ", ['photos/photo/29.jpg', 'photos/photo/30.mp4', 'photos/photo/P1010768.JPG', 'photos/photo/P1010774.JPG', 'photos/photo/P1010800.JPG', 'photos/photo/P1010825.JPG', 'photos/photo/P1010826.JPG', 'photos/photo/1.jpg', 'photos/photo/01.jpg', 'photos/photo/2.jpg', 'photos/photo/3.jpg', 'photos/photo/5.jpg', 'photos/photo/6.jpg', 'photos/photo/7.jpg', 'photos/photo/15.jpg', 'photos/photo/18.jpg', 'photos/photo/21.jpg', 'photos/photo/22.jpg', 'photos/photo/23.jpg', 'photos/photo/24.jpg']],
    'Tony Hawk': ["Meet my friend, Tony Hawk! When I was in 11th grade, Tony used to visit our home terrace. That's when I decided to use my camera, remote controlled from my phone, and another device called BirdCam which is essentially a motion-activated camera system. Enjoy Mr Hawk's flights!", ['photos/hawk/WSBC0461.JPG', 'photos/hawk/01.mp4', 'photos/hawk/02.mp4', 'photos/hawk/13~2.mp4', 'photos/hawk/14~3.mp4', 'photos/hawk/WSBC0094.JPG', 'photos/hawk/WSBC0098.JPG', 'photos/hawk/WSBC0471.JPG', 'photos/hawk/WSBC0556.JPG', 'photos/hawk/WSBC0700.JPG', 'photos/hawk/WSBC0794.JPG']],
    'Fireflies': ["A couple of years ago, me and my my friends embarked on an adventure to venture 6 hours deep into the jungles of Maharashtra, India to find Hotaru-Tai (Japanese for 'a troop of fireflies'). It quickly turned into a spooky experience when we found all kindsof dangerous insects, snakes and the most scary of them all, Scorpians! But we were soon rewarded for our perseverance when we found  what we were looking for...  ", ['photos/fire/P1280412.JPG', 'photos/fire/P1280417.JPG', 'photos/fire/P1280421.JPG', 'photos/fire/P1280427.JPG', 'photos/fire/P1280455.JPG', 'photos/fire/1.JPG', 'photos/fire/2.JPG', 'photos/fire/3.JPG', 'photos/fire/4.jpeg']],
    'Terrace': [""" My balcony terrace serves as a humble sanctuary in the midst of urban hustle, a sliver of solace where nature greets me in its most unassuming forms. It's here, amidst potted plants and the open sky, that I've witnessed the quiet ballet of day turning to night, of seasons weaving through their cycles.

This little oasis has played host to a variety of visitors - from the fleeting flutter of butterflies to the diligent bees, from the vibrant blossoms of spring to the muted tones of autumn. Each creature, each petal tells a story, a whisper of the world's seamless tapestry right at my doorstep.

Through the lens of my camera, I've tried to capture these unsung moments: the dew on a spider's web, the dance of light and shadow, the symmetry in leaves, and the fleeting expressions of my non-human guests. Each photograph is a chapter, a pause in time, celebrating the ordinary's hidden beauty.

Welcome to my terrace - a place where nature's simplicity meets the complexity of life, a reminder to look, to see, to pause.""", ['photos/terr/P1360084.JPG', 'photos/terr/P1360099.JPG', 'photos/terr/P1360139.JPG', 'photos/terr/P1360200.JPG', 'photos/terr/P1360201.JPG', 'photos/terr/P1360241.JPG', 'photos/terr/P1360246.JPG', 'photos/terr/P1360257.JPG', 'photos/terr/P1360263.JPG', 'photos/terr/P1360270.JPG', 'photos/terr/P1360290.JPG', 'photos/terr/P1360291.JPG', 'photos/terr/P1360293.JPG']],
     'Paintings': ["When I cannot explain things or feelings in words, I paint...", ["photos/Paint/1.mp4", "photos/Paint/2.jpg", "photos/Paint/3.jpg", "photos/Paint/4.jpg", "photos/Paint/5.jpg", "photos/Paint/6.jpg"]]
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

def previous_hyperloop_image():
    if 'hyperloop_image_index' not in st.session_state:
        st.session_state['hyperloop_image_index'] = 0
    
    hyperloop_images = experiences['loopMIT'][1]
    st.session_state['hyperloop_image_index'] = max(st.session_state['hyperloop_image_index'] - 1, 0)

def next_hyperloop_image():
    # Ensure 'hyperloop_image_index' is initialized
    if 'hyperloop_image_index' not in st.session_state:
       st.session_state['hyperloop_image_index'] = 0
    
    hyperloop_images = experiences['loopMIT'][1]
    st.session_state['hyperloop_image_index'] = min(st.session_state['hyperloop_image_index'] + 1, len(hyperloop_images) - 1)

# Display function for Hyperloop
def display_hyperloop():
    if 'hyperloop_image_index' not in st.session_state:
        st.session_state['hyperloop_image_index'] = 0
    hyperloop_description, hyperloop_images = experiences['loopMIT']
    st.markdown(hyperloop_description, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.button("Previous", key="prev_hyperloop", on_click=previous_hyperloop_image)
    with col2:
        st.button("Next", key="next_hyperloop", on_click=next_hyperloop_image)

    current_image = hyperloop_images[st.session_state['hyperloop_image_index']]
    st.image(current_image, use_column_width=True)

# Main display logic updated to include specific display functions
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'loopMIT':
        display_hyperloop()
        
# Check if the 'photo_image_index' is in the session state, otherwise initialize it
if 'photo_image_index' not in st.session_state:
    st.session_state['photo_image_index'] = 0

# Define navigation functions for Photography
def previous_photo_image():
    st.session_state['photo_image_index'] = (st.session_state['photo_image_index'] - 1) % len(experiences['Snaps'][1])

def next_photo_image():
    st.session_state['photo_image_index'] = (st.session_state['photo_image_index'] + 1) % len(experiences['Snaps'][1])

# Display function for the Photography section
def display_photography():
    selected_option = st.session_state.get('selected_option')
    if selected_option == 'Snaps':
        photo_description, photo_media = experiences[selected_option]
        st.markdown(photo_description, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous"):
                previous_photo_image()
        with col2:
            if st.button("Next"):
                next_photo_image()
        
        current_media = photo_media[st.session_state['photo_image_index']]
        if current_media.endswith('.MOV') or current_media.endswith('.mp4'):
            st.video(current_media)
        else:
            st.image(current_media, use_column_width=True)

# Main display logic
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Snaps':
        display_photography()
# Check if the 'photo_image_index' is in the session state, otherwise initialize it
if 'photo_image_index' not in st.session_state:
    st.session_state['photo_image_index'] = 0        
# Navigation functions for Tony Hawk
def previous_tony_hawk_image():
    tony_hawk_images = experiences['Tony Hawk'][1]
    st.session_state['tony_hawk_image_index'] = (st.session_state['tony_hawk_image_index'] - 1) % len(tony_hawk_images)

def next_tony_hawk_image():
    tony_hawk_images = experiences['Tony Hawk'][1]
    st.session_state['tony_hawk_image_index'] = (st.session_state['tony_hawk_image_index'] + 1) % len(tony_hawk_images)

if 'tony_hawk_image_index' not in st.session_state:
    st.session_state['tony_hawk_image_index'] = 0  # Initialize it with the first image index

# Display function for Tony Hawk
def display_tony_hawk():
    selected_option = st.session_state.get('selected_option')
    if selected_option == 'Tony Hawk':
        tony_hawk_description, tony_hawk_media = experiences[selected_option]
        st.markdown(tony_hawk_description, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous", key="prev_tony_hawk"):
                previous_tony_hawk_image()
        with col2:
            if st.button("Next", key="next_tony_hawk"):
                next_tony_hawk_image()
        
        current_media = tony_hawk_media[st.session_state['tony_hawk_image_index']]
        if current_media.endswith('.MOV') or current_media.endswith('.mp4'):
            st.video(current_media)
        else:
            st.image(current_media, use_column_width=True)

# Main display logic
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Tony Hawk':
         display_tony_hawk()

# Fireflies navigation functions
def previous_fireflies_image():
    fireflies_images = experiences['Fireflies'][1]
    st.session_state['fireflies_image_index'] = (st.session_state['fireflies_image_index'] - 1) % len(fireflies_images)

def next_fireflies_image():
    fireflies_images = experiences['Fireflies'][1]
    st.session_state['fireflies_image_index'] = (st.session_state['fireflies_image_index'] + 1) % len(fireflies_images)

if 'fireflies_image_index' not in st.session_state:
    st.session_state['fireflies_image_index'] = 0

# Display function for Fireflies
def display_fireflies():
    fireflies_description, fireflies_images = experiences['Fireflies']
    st.markdown(fireflies_description, unsafe_allow_html=True)

    # Create Previous and Next buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous", on_click=previous_fireflies_image):
            pass
    with col2:
        if st.button("Next", on_click=next_fireflies_image):
            pass

    # Display the current Fireflies image
    st.image(fireflies_images[st.session_state['fireflies_image_index']], use_column_width=True)

# Update the main display logic to include Fireflies
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Fireflies':
         display_fireflies()
         
# Navigation functions for Terrace
def previous_terrace_image():
    terrace_images = experiences['Terrace'][1]
    st.session_state['terrace_image_index'] = (st.session_state['terrace_image_index'] - 1) % len(terrace_images)

def next_terrace_image():
    terrace_images = experiences['Terrace'][1]
    st.session_state['terrace_image_index'] = (st.session_state['terrace_image_index'] + 1) % len(terrace_images)

if 'terrace_image_index' not in st.session_state:
    st.session_state['terrace_image_index'] = 0  # Initialize with the first image index

# Display function for Terrace
def display_terrace():
    terrace_description, terrace_images = experiences['Terrace']
    st.markdown(terrace_description, unsafe_allow_html=True)

    # Create Previous and Next buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous", on_click=previous_terrace_image):
            pass
    with col2:
        if st.button("Next", on_click=next_terrace_image):
            pass

    # Display the current Terrace image
    st.image(terrace_images[st.session_state['terrace_image_index']], use_column_width=True)

# Main display logic updated to include Terrace
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Terrace':
        display_terrace()
        
# Initialize 'paintings_image_index' in session state if not already present
if 'paintings_image_index' not in st.session_state:
    st.session_state['paintings_image_index'] = 0

# Navigation functions for Paintings
def previous_painting_image():
    painting_images = experiences['Paintings'][1]
    st.session_state['paintings_image_index'] = max(st.session_state['paintings_image_index'] - 1, 0)

def next_painting_image():
    painting_images = experiences['Paintings'][1]
    st.session_state['paintings_image_index'] = min(st.session_state['paintings_image_index'] + 1, len(painting_images) - 1)

# Display function for Paintings
def display_paintings():
    painting_description, painting_images = experiences['Paintings']
    st.markdown(painting_description, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.button("Previous", key="prev_paintings", on_click=previous_painting_image)
    with col2:
        st.button("Next", key="next_paintings", on_click=next_painting_image)

    # Handle different media types (images and videos)
    current_media = painting_images[st.session_state['paintings_image_index']]
    if current_media.endswith('.MOV') or current_media.endswith('.mp4'):
        st.video(current_media)
    else:
        st.image(current_media, use_column_width=True)

# Update your main display logic to include Paintings
selected_option = st.session_state.get('selected_option')
if selected_option:
    if selected_option == 'Paintings':
        display_paintings()
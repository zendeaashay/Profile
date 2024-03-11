import streamlit as st
import altair as alt
import openai


st.set_page_config(page_title="Welcome to my Page!", page_icon="🌟", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
# Enable Altair dark theme for charts
alt.themes.enable("dark")

# Define a function to toggle the visibility of the star rating
def toggle_rating():
    st.session_state.show_rating = not st.session_state.show_rating

# Initialize the session state variable
if 'show_rating' not in st.session_state:
    st.session_state.show_rating = True
    
# Custom CSS
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Toggle between 'About Me' and 'AshGPT'
page = st.radio("Choose a page:", ("About Me", "AshGPT"), horizontal=True)

if page == "About Me":
    # Your code for the 'About Me' section
    # ... (your existing code) ...
    st.title("Aashay Zende")
    st.markdown("""
    <div class="bio">
        <h3>Data Wizard | Adventurer | Photographer | Surfer</h3>
        <p>Hey there! I'm Aashay, a data wizard by day and an adventurous spirit by... 
        well, also by day (and sometimes night). Currently weaving my magic with numbers 
        and analytics at the prestigious D'Amore McKim School of Business, 
        Northeastern University, I'm on a quest to make sense of the world, one dataset at a time.</p>
        <p>Born and raised in the bustling city of Mumbai, India, I've always been a bit 
        of a nomad at heart, with my compass pointing towards icy mountain peaks and the 
        soothing waves of beaches. When I'm not surfing the waves or the web, 
        I love painting landscapes that capture the essence of my travels and framing 
        moments through the lens of my camera.</p>
        </div>
    """, unsafe_allow_html=True)
    st.image('image.jpeg', caption='Exploring the Himalayas with my furry friends!')

elif page == "AshGPT":

    st.title('AshGPT')
    st.title("Introducing AshGPT, your digital concierge to Aashay Zende's career narrative. Equipped to provide insights into his professional timeline and technical know-how, I stand ready to field your queries. From his analytical acumen to leadership qualities, ask about Aashay's professional journey or solicit assistance with a wide array of topics—be it solving a math problem, understanding scientific concepts, diving into history, or crafting a compelling email. Let's start the conversation.")
    openai.api_key = st.secrets["openai_api"]
    if "openai_model" not in st.session_state:
       st.session_state["openai_model"] = "gpt-3.5-turbo"
    
    if "messages" not in st.session_state:
       st.session_state.messages = []

    prompt_instruction = """You are an AI chatbox and your job is to tell users about an individual called Aashay Zende who has created you and you have to tell users about my resume and professional background. Following is Aashay Zende's information 'Aashay Zende has a rich educational and professional background, blending technical acumen with strategic business analysis. He pursued his Master of Science in Business Analytics from Northeastern University in Boston, Massachusetts, from September 2023 to December 2024, earning a CGPA of 3.2, and holds a Bachelor of Technology in Automobile Engineering from Manipal Institute of Technology in India, with a GPA of 7.2, completed between August 2018 and July 2022. His coursework spanned various subjects, including Data Analysis, Information Visuals and Dashboards, Marketing Analytics, Engineering Economics, Financial Management, and Numerical Simulation. Aashay also earned certifications through Coursera in Introduction to Business Analytics with R from the University of Illinois at Urbana-Champaign and in Foundations: Data Data Everywhere from Google​​.

Aashay's skill set is extensive, encompassing statistical techniques like SVM, regression models, decision tree, KNN, cluster analysis, NLP, K-means, and Naive Bayes. He is proficient in database programming and various tools, including Tableau, PowerBI, Python, SQL, R, MySQL, Google Analytics, and Microsoft Excel functions​​.

Professionally, Aashay was a full-time Business Analyst at Redseer Strategy Management Consulting from February to September 2022. There, he conducted a granular analysis of e-commerce models, enhanced operational efficiency by 18%, and was instrumental in developing a predictive analytics project and a PowerBI dashboard that increased client revenue by 40%. He played a key role in investment portfolio optimization, resulting in a 27% increase in portfolio performance on average, and led market analysis initiatives that reduced customer acquisition costs by 20%​​.

Aashay's experience as an Automobile Technical Advisor intern at Mahindra and Mahindra in June and July 2021 allowed him to gain insights into company operations, improving assembly guidelines and inventory management, which led to a 10% and 5% improvement in respective areas​​.

His tenure as Co-Head of the Vehicle Dynamics Department at LoopMIT from February 2019 to July 2021 was marked by his contribution to SpaceX's Hyperloop competition, where he led the design and development of the pod's suspension system and chassis. He established a mentoring program, utilized advanced engineering software for design and simulation, and managed cross-functional teams, successfully advancing the design to the competition's final round and securing significant sponsorship​​..I am a professional with a Master of Science in Business Analytics from Northeastern University and a Bachelor of Technology in Automobile Engineering from Manipal Institute of Technology. My experience includes a role as a Business Analyst at Redseer Strategy Management Consulting, where I spearheaded projects aimed at enhancing operational efficiency and designed an innovative PowerBI dashboard. I possess strong technical skills, particularly in statistical techniques, database programming, and proficiency in tools such as Tableau and Python.

In terms of self-reflection, I recognize my propensity to overthink and sometimes act impulsively. I am committed to improving my self-esteem and managing stress more adeptly. My key strengths are my independence, analytical thinking, dedication, and high emotional intelligence. I am well-organized, highly motivated, and have an innate passion for my work, with a natural knack for grasping the tasks at hand.

Looking ahead, I see myself continuing to grow and excel in my field, whether that be in the corporate sphere or other areas I'm passionate about, such as travel, literature, or the culinary world. My aim is to find a fulfilling balance between my professional and personal life, realizing my full potential while seizing opportunities without regret.

I believe that my unique combination of analytical prowess, a zeal for lifelong learning, and experience in both technical and business facets of analytics makes me a standout candidate. My proactive problem-solving abilities and adaptability to new challenges would be a valuable asset to your team.

My awareness of job openings stems from my active engagement with professional networks and online platforms, and my interest in your company's work drew me to this particular position. This job is a perfect match for my skills and ambitions, offering a chance to employ my analytics and problem-solving expertise to address tangible business problems, which is a pivotal step in my career development.

One of my most significant professional accomplishments to date was at Redseer Strategy Management Consulting, where our team developed a PowerBI dashboard that substantially improved our data visualization capabilities. This innovation led to an increase in revenue and reinforced our reputation for providing data-driven consultation services.

When faced with anger from a co-worker or customer, I concentrate on identifying the root cause and collaborating to find a solution. My approach is to communicate clearly and with empathy, prioritizing the maintenance of positive relationships.

My ideal job would be one where I can apply my business analytics skills to generate impactful insights and strategies for business expansion. This role would involve a blend of analytical challenges and creative problem-solving within a dynamic and supportive workplace.

I perform best in work environments that encourage collaboration, innovation, and lifelong learning, with a team and culture that appreciates individual efforts towards shared goals.

The toughest decision I made in the past six months was to seek new opportunities that more closely align with my long-term career aspirations, balancing potential risks and rewards and their implications for my professional advancement.

My leadership style revolves around leading by example, promoting open dialogue, and empowering team members to take responsibility for their tasks. I emphasize collaboration and support innovation and creative approaches to problem-solving.

When I disagree with a decision, I voice my reservations respectfully and offer constructive feedback, using data and rational arguments to support my views, striving for a consensus that aligns with our collective goals.

In the first three months on the job, you can expect me to become acclimated with the team and company culture swiftly, identify key areas for contribution, and start producing meaningful work. I intend to focus on building relationships and comprehending the overarching business objectives to align my efforts with them effectively.

Outside of work, my hobbies include traveling to experience new cultures, reading literature, experimenting with cooking, and engaging in outdoor activities. These pursuits provide me with a balanced perspective and inspire creativity in my professional life.

I am eager to learn more about the team's ongoing projects, the company's strategic priorities for the upcoming year, and how this role contributes to those goals. Additionally, I am curious about the company culture and the opportunities available for professional growth.


2 / 2

User
Aashay Zende - Resume.pdf
PDF
'."""

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
           st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
    # Prepend the prompt instruction to the user's input
        full_prompt = f"{prompt_instruction} {prompt}"
    
        st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
        with st.chat_message("user"):
           st.markdown(prompt)
    # Display assistant message in chat message container
        with st.chat_message("assistant"):
           message_placeholder = st.empty()
           full_response = ""
        # Simulate stream of response with milliseconds delay
           for response in openai.ChatCompletion.create(
              model=st.session_state["openai_model"],
              messages=[
                 {"role": "user", "content": full_prompt},  # Use full_prompt here
                 {"role": "assistant", "content": full_response}
              ],
              stream=True,
           ):
            # Get content in response
               full_response += response.choices[0].delta.get("content", "")
            # Add a blinking cursor to simulate typing
               message_placeholder.markdown(full_response + "▌")
           message_placeholder.markdown(full_response)
    # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

from streamlit_star_rating import st_star_rating

# Add a button to toggle the star rating visibility
st.button('Show/Hide', on_click=toggle_rating)

# Show the star rating if the toggle is set to show it
if st.session_state.show_rating:

    # Create a container for the star rating
  with st.container():
        st.write("Please rate your experience with this page:")
        stars = st_star_rating(label="", maxValue=5, defaultValue=5, key="rating", dark_theme=True)

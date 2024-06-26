import streamlit as st
import altair as alt
import openai
from streamlit_star_rating import st_star_rating





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
    
# Custom CSS
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    

def show_resume():
    st.title('My Resume')
    st.write("Here is my resume showcasing my experience and skills.")
    # Display the resume PDF
    pdf_viewer("ResumeWOnumber.pdf", width=800, height=1000)
    # Link to download resume
    resume_link = 'ResumeWOnumber.pdf'
    with open(resume_link, "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="ResumeWOnumber.pdf",
            mime="application/pdf"
        )   

# Toggle between 'About Me' and 'AshGPT'
page = st.radio("Explore my very own AshGPT next!", ("Welcome!", "AshGPT"), horizontal=True)

if page == "Welcome!":
    st.title("Aashay Zende")
    st.markdown("""
    <div class="bio">
        <h4>Data Analyst | Business Analyst | Datacamp SQL Associate Certified | PowerBI and Tableau Specialist | Portfolio Management | Strategy Consulting </h4>
        <p>I am a passionate Data and Business Analyst, pursuing a Master of Science in Business Analytics at Northeastern University. I am actively seeking opportunities in business or data analytics, where I can leverage my advanced skills in Data Analytics, Python, SQL, R, PowerBI, Tableau, MS Office, Management and more, in strategic consulting, marketing, and supply chain management projects, utilizing my analytical prowess to drive data-informed decision-making and strategic initiatives.
        
My portfolio is a testament to my multifaceted skills, from developing strategic marketing campaigns and investment portfolio optimization to spearheading groundbreaking projects like the transformative PowerBI dashboard that revolutionized data visualization and decision-making processes.

For recruiters looking to harness my blend of analytical rigor, strategic thinking, and dynamic leadership in the realms of business analysis, strategy consulting, marketing, supply chain management, and beyond, feel free to reach out. You can contact me at zende.a@northeastern.edu, or connect with me on LinkedIn.

Let's navigate the data-driven landscapes together and turn complex challenges into strategic opportunities. </p>
        </div>
    """, unsafe_allow_html=True)
    st.image('image.jpg', caption='Exploring the Himalayas with my furry friends!')
    
    from streamlit_pdf_viewer import pdf_viewer

   

    # Execute the function to display the resume
    show_resume()
    st.markdown("""
    <div class="bio">
        <p> I carved a niche for myself in the Indian E-Commerce landscape, as a  Business Analyst at Redseer Strategy Management Consulting, India's biggest homegrown consulting firm, enhancing operational efficiencies and driving key business decisions and strategies for all the biggest players in the market. You can find my analyses and work on the 'E-Commerce Consulting Insights' in the sidebar.

Grounded in my rigorous education from Northeastern University, where I'm pursuing a Master of Science in Business Analytics, and my foundational Bachelor's from Manipal Institute of Technology in Automobile Engineering, I bring a unique blend of analytical prowess and strategic insight to the table. My journey in data analytics is marked by a keen eye for detail and a relentless pursuit of excellence, evident from my roles at prestigious organizations like Redseer Strategy Management Consulting, where I've left a significant mark by enhancing operational efficiencies and influencing pivotal business decisions.

With a toolkit enriched by statistical techniques, and proficiency in tools such as Tableau, PowerBI, Python, and SQL, I navigate the complex terrain of data to uncover actionable insights. My contributions extend beyond the workplace, into academia and competitive realms like the SpaceX Hyperloop competition, where I led my team to design an innovative transportation concept.
I'm more than just numbers and data models; my spirit of adventure leads me to explore new horizons, pushing the boundaries of what's possible both professionally and personally.
</p>
        </div>
    """, unsafe_allow_html=True)
    
    import json
    from streamlit_timeline import timeline


    def show_timeline():
     st.title("My Professional Timeline")
        
    with open('timeline_data.json', "r") as f:
            timeline_data = json.load(f)

        
    timeline(timeline_data, height=800)
    show_timeline()
elif page == "AshGPT":
    st.markdown("""
    <div class="bio">
        <h1>AshGPT</h1>
        <h3>Your Digital Concierge</h3>
        <p>Introducing AshGPT, your digital concierge to Aashay's career narrative. Equipped to provide insights into his professional timeline and technical know-how, I stand ready to field your queries. From his analytical acumen to leadership qualities, ask about Aashay's professional journey or solicit assistance with a wide array of topics—be it solving a math problem, understanding scientific concepts, diving into history, or crafting a compelling email. Let's start the conversation.</p>
    </div>
    """, unsafe_allow_html=True)
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


Aashay Zende - Resume:'Aashay Zende
My Website |  zende.a@northeastern.edu | Boston, MA | LinkedIn‬‬‬‬‬ - https://www.linkedin.com/in/aashay-zende-3018209b/




EDUCATION
Northeastern University, Boston, MA                                                                                                                                          Sept 2023 – Dec 2024
•	Master of Science - Business Analytics, CGPA – 3.2
Courses: Foundations of Data Analysis, Data Wrangling, Information Visuals and Dashboards, Data Mining/Machine Learning, Business Information Design, Quality and Strategy, Marketing Analytics, Brand and Advertising Management

Manipal Institute of Technology, Manipal, India                                                                                                                   August 2018 – July 2022
•	Bachelor of Technology in Automobile Engineering, GPA – 7.2
Courses: Data Analysis, Engineering Economics and Financial Management, Electronics, Essentials of Management, Optimization Techniques, Engineering Mathematics, Numerical Simulation
•	Coursera Certified: Introduction to Business Analytics with R - University of Illinois at Urbana-Champaign, Grade Achieved: 85.95%
                                     Foundations: Data, Data, Everywhere – Google, Grade Achieved: 87.43%

SKILLS
•	Statistical Techniques: SVM, Regression models, Decision Tree, KNN , Cluster Analysis, NLP, K-Means, Naive Bayes
•	Database, Programming & Tools: Tableau, PowerBI, Python, SQL, R, MySQL, Google SQL, Google Analytics, Microsoft Excel functions

WORK AND INTERNSHIP EXPERIENCE
Redseer Strategy Management Consulting                                                                                                                                   Feb 2022 - Sept 2022
Business Analyst, Full-Time
•	Conducted a granular analysis of 12 distinct e-commerce models against the backdrop of India's dynamic retail landscape, leading to strategic solutions, and achieved an average of 18% boost in operational efficiency, during my tenure, for client companies including Amazon, Flipkart, Reliance and many more.
•	Pioneered a predictive analytics project that provided client companies with advanced monthly insights into critical KPIs including gross merchandise value (GMV), top-line metrics, returns, shipment split by 3PL and captive and other P & L parameters without prior input from them. Our team's acumen in forecasting critical financial parameters greatly impressed our clientele, fostering a reputation for excellence in strategic foresight.
•	My team developed a transformative PowerBI dashboard, leveraging extensive Excel datasets to create a groundbreaking tool that significantly enhanced our data visualization capabilities and decision-making processes. This innovative solution played a crucial role in revitalizing client strategies, contributing to a substantial 40% revenue increase over a 10-month period through the acquisition of new clients and the fortification of existing contracts, demonstrating the significant value of our data-driven consultation services.
•	Collaborated within a dedicated analytics team applying Python and R to distill complex data into strategic insights for investment portfolio optimization, culminating in refined investment strategies for investment firms like Warburg Pincus, with a subsequent 27% increase in portfolio performance on average.
•	Facilitated monthly strategic meetings with VPs and heads of strategy of client companies, presenting market analyses and market landscaping that influenced key growth initiatives and led to the implementation of 22 new strategies and model adaptations.
•	Spearheaded a rigorous e-commerce market analysis, employing advanced Excel functions and pivot tables to dissect expansive market survey data. This strategic evaluation unearthed pivotal insights, guiding our firm's marketing efforts to target high-value customer segments more effectively. The resultant tactics directly led to a 20% reduction in customer acquisition costs, while simultaneously optimizing marketing expenditures.
Mahindra and Mahindra                                                                                                                                                               June 2021 - July 2021
Automobile Technical Advisor, Summer Intern
•	Engaged closely with senior management and technical supervisors in a month-long deep dive into company operations, gaining insights into the end-to-end process flows and contributing to the streamlining of operations protocols.
•	Conducted a comprehensive subsystem analysis on the complete line of vehicles manufactured by Mahindra, utilizing both technical manuals and hands-on assessments, facilitating a 10% improvement in the subsystem assembly guidelines by identifying critical efficiency bottlenecks.
•	Performed a targeted analysis of the inventory management and supply logistics systems, identifying and recommending enhancements that led to a 5% reduction in inventory processing time during my internship tenure.

PROJECTS
LoopMIT, Manipal Institute of Technology                                                                                                                                  Feb 2019 - July 2021
Co-Head, Vehicle Dynamics Department
•	As part of a select team of 20 students, we contributed to LOOPMIT's participation in SpaceX's esteemed Hyperloop competition, presenting our innovative transportation concepts to industry leaders in Hawthorne, California.
•	Innovatively designed and meticulously developed the hyperloop pod’s suspension system and chassis, incorporating magnetic levitation technology to achieve minimal drag and friction in a vacuum tunnel, a design that successfully advanced to the final round of the competition.
•	Initiated and developed a comprehensive mentoring program for newcomers, enhancing their skills in research methodologies and analysis simulations, which also involved managing the department's budget and meticulously reporting on team progress.
•	Leveraged advanced engineering software, including Autodesk Fusion360 and SolidWorks, to intricately design the hyperloop pod and perform detailed motion analysis, which was critical in optimizing design efficiency and operational stability.
•	Directed the research and application of computational fluid and aero dynamic simulations, leading to a 16% reduction in aerodynamic drag, thus enhancing the pod's speed capabilities for the competition.
•	Managed cross-functional teams to synchronize the pod's mechanical, electrical, and software subsystems, ensuring seamless integration and functionality that exceeded competition benchmarks.
•	Strategically led fundraising initiatives, successfully securing $5,000 in monetary sponsorships, and procuring cutting-edge components from leading tech firms, which were instrumental in the advanced development of our hyperloop pod.
'
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

        

        
from streamlit_star_rating import st_star_rating
# Define a function to toggle the visibility of the star rating
def toggle_rating():
    st.session_state.show_rating = not st.session_state.show_rating

# Initialize the session state variable
if 'show_rating' not in st.session_state:
    st.session_state.show_rating = True

# Add a button to toggle the star rating visibility
st.button('Show/Hide', on_click=toggle_rating)

# Show the star rating if the toggle is set to show it
if st.session_state.show_rating:

    # Create a container for the star rating
  with st.container():
        st.write("Please rate your experience with this page:")
        stars = st_star_rating(label="", maxValue=5, defaultValue=5, key="rating", dark_theme=True)

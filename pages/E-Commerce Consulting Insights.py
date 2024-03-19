import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

def show_pdf():
    st.title('Consulting Analysis and Insights on the Indian E-Tailing Market')
    st.markdown("""
    <div class="bio">
        <p>Welcome to my in-depth exploration of India's e-commerce landscape, a pivotal area reshaping how consumers engage with retail in the digital age. My presentation, "eComm India: Navigating Growth in the Digital Marketplace," offers a comprehensive analysis of trends, challenges, and opportunities within India's booming online retail sector.

I delve into the resilience and continued growth of online retail in India, even as traditional retail bounces back to pre-pandemic levels. My data-rich slides provide insights into the remarkable trajectory of e-tailing, with projections showing a potential $70 billion Gross Merchandise Value (GMV) in 2022, marking a 35% year-over-year growth.

My analysis unpacks the drivers of e-tailing expansion, highlighting the significant role of increased internet penetration, the rise of smartphone usage, and the evolving profile of online shoppers. Particularly notable is the shift towards smaller cities contributing to the e-commerce boom, with a more diverse range of products being purchased online than ever before.

I address consumer preferences, emphasizing the importance of product variety, competitive pricing, and the convenience of online shopping experiences, including fast delivery and hassle-free returns. The presentation also sheds light on the challenges faced by consumers, particularly around product quality and the need for improved pre-purchase interactions.

My exploration goes beyond traditional e-commerce models to examine the emergence of new platforms that cater to specific consumer needs, such as quick commerce and social commerce. I provide an analysis of consumer awareness, adoption rates, and the unique value propositions of these new models.

My presentation is not just a snapshot of the current state of e-commerce in India but a forward-looking perspective on the trends shaping the future of retail in the digital age. It's designed for anyone keen to understand the dynamic e-commerce landscape in India, from industry professionals to investors, and from policymakers to the curious consumer. Join me on this insightful journey through the vibrant world of e-commerce in India. </p>
        </div>
    """, unsafe_allow_html=True)
    pdf_viewer("eComm India.pdf", width=700, height=487)


# Execute the function to display the resume
show_pdf()

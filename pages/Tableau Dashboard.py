import streamlit as st

# Page Configuration
st.set_page_config(page_title='Tableau Dashboard', layout='wide')

# Tableau Dashboard Embed Code as Markdown with Iframe
tableau_dashboard_markdown = """
<iframe src="https://public.tableau.com/views/AmzTableau/NetGMV?:showVizHome=no&:embed=true" width="1000" height="800"></iframe>
"""

# Render the Markdown with Iframe in Streamlit
st.markdown(tableau_dashboard_markdown, unsafe_allow_html=True)
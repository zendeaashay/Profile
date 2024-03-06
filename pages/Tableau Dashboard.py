import streamlit as st

# Set page config
st.set_page_config(page_title='Tableau Dashboard', layout='wide')

# Choice of dashboard
dashboard_choice = st.selectbox('Choose a Tableau Dashboard:',
                                ('Dashboard 1', 'Dashboard 2'))

# Tableau dashboards embed links
dashboards = {
    'Dashboard 1': 'https://public.tableau.com/views/Amazon_17097002192610/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link',
    'Dashboard 2': 'https://public.tableau.com/views/Amazon_17097002192610/Dashboard2?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link'
}

# Generate the iframe HTML for the selected dashboard
iframe_html = f'<iframe src="{dashboards[dashboard_choice]}" width="1000" height="800"></iframe>'

# Render the selected Tableau dashboard
st.markdown(iframe_html, unsafe_allow_html=True)
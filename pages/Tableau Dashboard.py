import streamlit as st
from streamlit_embedcode import embed_code

# Page Configuration
st.set_page_config(page_title='Tableau Dashboard', layout='wide')

# Your Tableau dashboard URL
tableau_dashboard_url = """

<div class='tableauPlaceholder' id='viz1709650280011' style='position: relative'>
    <noscript><a href='#'>
        <img alt='Amazon Net GMV across Time (USD$ Millions)' 
             src='https://public.tableau.com/static/images/Am/AmzTableau/NetGMV/1_rss.png' 
             style='border: none' />
    </a></noscript>
    <object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='AmzTableau/NetGMV' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Am/AmzTableau/NetGMV/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1709650280011');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height='887px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height='777px';} else { vizElement.style.width='100%';vizElement.style.height='527px';}
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Embed the Tableau Dashboard using the embed_code function
embed_code(tableau_dashboard_url, height=800)

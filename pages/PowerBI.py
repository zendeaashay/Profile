#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:09:02 2024

@author: aashayzende
"""

import streamlit as st
import pandas as pd



st.set_page_config(page_title="A PowerBI dashboard created by my group on the Happy Cow Company sales", page_icon="🌟", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Replace the old iframe code with the new one
st.markdown("""
    <iframe title="Happy Cow dashboard" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=e8de6e97-8e70-42ac-a8b1-14a041c9be78&autoAuth=true&ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7" frameborder="0" allowFullScreen="true"></iframe>
    """, unsafe_allow_html=True)
    
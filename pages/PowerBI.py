#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:09:02 2024

@author: aashayzende
"""

import streamlit as st
import pandas as pd



st.set_page_config(page_title="A PowerBI dasboard created by my group on the Happy Cow Company sales", page_icon="🌟", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
st.markdown("""
    <iframe width="600" height="606" src="https://app.powerbi.com/reportEmbed?reportId=e8de6e97-8e70-42ac-a8b1-14a041c9be78&autoAuth=true&ctid=a8eec281-aaa3-4dae-ac9b-9a398b9215e7" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    
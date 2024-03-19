#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:26:54 2024

@author: aashayzende
"""
import streamlit as st
import altair as alt
from streamlit_pdf_viewer import pdf_viewer
st.set_page_config(page_title="Amazon GMV Dashboard", page_icon="🌟", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown(hide_default_format, unsafe_allow_html=True)
# Enable Altair dark theme for charts
alt.themes.enable("dark")

st.markdown(""" <div class="bio">
    <h4>Amazon GMV Dashboard </h4>
    <p> Here's a look at a Tableau Dashboard created by me... </p>
        </div>
    """, unsafe_allow_html=True)
pdf_viewer("Amazon.pdf", width=800, height=1000)
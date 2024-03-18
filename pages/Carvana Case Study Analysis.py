#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 23:26:54 2024

@author: aashayzende
"""
import streamlit as st
import altair as alt
st.set_page_config(page_title="Introduction to Carvana Case Study:", page_icon="🌟", layout="wide")
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
    <h4>Introduction to Carvana Case Study: </h4>
    <p> In the realm of automotive retail, Carvana stands as a disruptive force, reshaping the traditional car-buying experience through innovative online platforms and streamlined processes. This case study delves into a comprehensive analysis of Carvana's dataset, aiming to uncover insights into key factors influencing the quality of vehicle purchases.

Through a series of analytical methodologies, ranging from exploratory data analysis to regression modeling, this study endeavors to unearth patterns, correlations, and predictive indicators associated with Carvana's 'IsBadBuy' variable. By examining various facets of the dataset, including car counts, popular makes, common sizes, average age, mileage, and geographical origins, we seek to provide a holistic understanding of the factors contributing to the quality of car purchases.

Moreover, the correlation analysis and regression modeling delve deeper into the relationships between 'IsBadBuy' and other continuous measures, shedding light on significant correlations and predictive insights. Through visualization techniques, we aim to elucidate the dynamic interplay between 'IsBadBuy' and multiple variables, exploring how these relationships evolve under different conditions, such as vehicle age and make.

Ultimately, armed with these analytical findings, we aim to offer actionable recommendations for Carvana, facilitating informed decision-making in identifying and mitigating potential risks associated with vehicle purchases. By leveraging the power of data-driven insights and visual tools, we endeavor to provide a roadmap for optimizing Carvana's operations and enhancing customer satisfaction in the ever-evolving automotive landscape. </p>
        </div>
    """, unsafe_allow_html=True)
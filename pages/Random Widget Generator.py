#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:09:55 2024

@author: aashayzende
"""
import streamlit as st
from streamlit_faker import get_streamlit_faker
st.header('Hey there!')
st.write('This page generates random titles, words, names, dropdown options and maps everytime you change the slider (seed) number')
st_faker = get_streamlit_faker()
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
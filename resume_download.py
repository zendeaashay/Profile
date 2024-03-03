#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:46:35 2024

@author: aashayzende
"""

import streamlit as st

st.title('Download My Resume')


resume_link = 'Aashay Zende - Resume.pdf'
with open(resume_link, "rb") as file:
    st.download_button(
        label="Download Resume",
        data=file,
        file_name="Aashay_Zende_Resume.pdf",
        mime="application/pdf"
    )
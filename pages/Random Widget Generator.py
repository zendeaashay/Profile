#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:09:55 2024

@author: aashayzende
"""
from streamlit_faker import get_streamlit_faker
faker = get_streamlit_faker(seed=seed)
st_faker.subheader()
st_faker.markdown()
st_faker.selectbox()
st_faker.slider()
st_faker.map()
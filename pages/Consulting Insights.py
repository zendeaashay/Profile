#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 13:15:12 2024

@author: aashayzende
"""

import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pandas as pd

# Load your DataFrame
df = pd.read_csv('your_data.csv')

# Generate the report
profile = ProfileReport(df, explorative=True)

# Render the report
st_profile_report(profile)
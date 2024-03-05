import json
import streamlit as st


def show_timeline():
    st.title("My Professional Timeline")
    
    with open('timeline_data.json', "r") as f:
        timeline_data = json.load(f)

    
    timeline(timeline_data, height=800)


show_timeline()
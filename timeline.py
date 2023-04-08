# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:47:20 2023

@author: admin
"""

from streamlit_timeline import timeline


# use full page width
# st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)
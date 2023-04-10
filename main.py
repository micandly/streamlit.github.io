import streamlit as st
# import numpy as np
import pandas as pd

# 菜单栏
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(layout="wide")

st.header("老子")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with st.sidebar:
    tabs = on_hover_tabs(tabName=['地图可视化', '知识图谱', '时间轴'], 
                          iconName=['a', 'b', 'c'], styles = {'navtab': {'background-color':'rgb(240, 242, 246)',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

TabName = ['地图可视化', '知识图谱', '时间轴']
while tabs in TabName:
    if tabs =='地图可视化':
        st.title("地图可视化")
        import map_pydeck
    elif tabs == '知识图谱':
        st.title("知识图谱")
        import graph  
    elif tabs == '时间轴':
        st.title("时间轴")
        import timeline
# from streamlit_option_menu import option_menu
# selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")






    

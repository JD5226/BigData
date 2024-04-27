import streamlit as st
import pandas as pd
import base64

# page_title
st.set_page_config(page_title='job select')
# header
st.header(':red[select] :green[ your] :blue[ job]')
# subheader
st.subheader('welcome！:smile:')
st.divider()  # Draws a horizontal rule
#search
st.text_input("input the company/job title",key="name")
st.session_state.name #connect text input
#button
button = st.button("submit")

###sidebar
##state
add_selectbox = st.sidebar.selectbox(
    'Select your state::sunglasses:',
    ("All","NY","NJ","AZ")
)
##skills
# list
options = ['Python', 'JAVA', 'C++']
#multiselect
selected_options = st.sidebar.multiselect(
    'Select your skills	:thumbsup: ',
    options,
    default=[]  # Set default selected options (an empty list means there are no default selected options)
)
##back ground
def sidebar_bg(side_bg):
 
   side_bg_ext = 'png'
 
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
 
#use
sidebar_bg('./pics/background.jpg')

###


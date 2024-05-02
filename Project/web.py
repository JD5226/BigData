import streamlit as st
import pandas as pd
import base64
from utils import load_skills, do_search, paginate_dataframe


# initialize data
df = pd.read_csv('./data/final.csv')

options = load_skills('./data/tag.json')[:1000] # don't load all otherwise the app will unresponse
states = [str(i) for i in df['state'].unique()]
#states = sorted([str(i) for i in df['state'].unique()])




# Initialize session state variables
if 'page_num' not in st.session_state:
    st.session_state['page_num'] = 1

page_size = 10





###################################
# page_title
st.set_page_config(page_title='job select')
# header
st.header(':red[select] :green[ your] :blue[ job]')
# subheader
st.subheader('welcome！:smile:')
st.divider()  # Draws a horizontal rule
#search
st.text_input("input the company",key="company")
st.text_input("input the company",key="title")
st.session_state.company #connect text input
st.session_state.title
###########################################



#button
if st.button("Submit"):
    result = do_search(df)
    st.session_state['result'] = result  # Store result in session state
    st.session_state['page_num'] = 1  # Reset to first page

    
if 'result' in st.session_state:
    paged_data = paginate_dataframe(st.session_state['result'], page_size, st.session_state['page_num'])
    # Display the current page of entries
    st.write(f"Displaying page {st.session_state['page_num']} of {len(st.session_state['result']) // page_size + (1 if len(st.session_state['result']) % page_size != 0 else 0)}")
    st.dataframe(paged_data)

    # Add navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        prev_button = st.button("Previous", key="prev")
    with col2:
        next_button = st.button("Next", key="next")

    if prev_button:
        if st.session_state['page_num'] > 1:
            st.session_state['page_num'] -= 1

    if next_button:
        if st.session_state['page_num'] * page_size < len(st.session_state['result']):
            st.session_state['page_num'] += 1

    

###sidebar
##state
add_selectbox = st.sidebar.selectbox(
    'Select your state::sunglasses:',
    states
)

##skills
# list
#options = ['Python', 'JAVA', 'C++'] # debug only
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


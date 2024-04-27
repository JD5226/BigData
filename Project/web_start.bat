chcp 65001
@echo off
call activate
call conda activate streamlit
streamlit run web.py
Pause
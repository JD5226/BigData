chcp 65001
@echo off
call activate
call conda activate bigdata
streamlit run web.py
Pause
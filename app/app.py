import streamlit as st
import pandas as pd
import os


geneder = ['boy','girl', 'prefer not to say']
if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
else:
    df = pd.DataFrame(
        [
        {"student name": "sharon", "score": 90, "gender": geneder[0]},
        {"student name": "dola", "score": 99, "gender": geneder[1]},
        {"student name": "pira", "score": 95, "gender": geneder[2]},
    ]
)
edited_df = st.experimental_data_editor(df, num_rows="dynamic")
st.bar_chart(edited_df)
st.line_chart(edited_df)
if st.button("save data"):
    pd.DataFrame(edited_df).to_csv("data.csv")
    st.success("saved")
    df = pd.read_csv("data.csv")

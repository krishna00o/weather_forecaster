import streamlit as st

st.header("Weather forecaster web")

place = st.text_input("Place")
days = st.slider("Choose days to forecast", min_value=1, max_value=5,
                 help="Slide to how many days to forecast")
option = st.selectbox("Select a Format: ", ("Temperature", "Sky"))

st.subheader(f"{option} for {days}days at {place}")
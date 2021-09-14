import streamlit as st

col3, col4 = st.columns(2)
col3.subheader("Computer Vision")
col3.markdown('Here, the input image is converted into black and white. This makes it super easy for computers to make a prediction on what the image contains. It basically compares the white pixels to the black pixels, to form a simplified version of the image')
col4.subheader("Visual")
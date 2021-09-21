import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from PIL import Image
import io
import os

# st.title('Image Captioning')
st.markdown("<h1 style='text-align: center; color: black;'>Image Captioning</h1>", unsafe_allow_html=True)


# fastapi endpoint
url = os.environ.get("BACKEND_URL",'http://localhost:5000')
endpoint = '/upload'

# st.write('''Caption for the uploaded image can be generated here.''') # description and instructions
st.markdown("<h2 style='text-align: center; color: black;'>Caption for the uploaded image can be generated here</h2>", unsafe_allow_html=True)

image = st.file_uploader('')  # image upload widget


def process(image, server_url):

    m = MultipartEncoder(
        fields={'file': ('filename', image, 'image/jpeg')}
        )

    r = requests.post(server_url,
                      data=m,
                      headers={'Content-Type': m.content_type},
                      timeout=5000)

    return r

if image is None:
        # st.error("Insert an image!")  # handle case with no image
        st.markdown("<h3 style='text-align: center; color: red;'>Insert an image!</h3>", unsafe_allow_html=True)

else:
        caption = process(image, url+endpoint)
        st.image([image], width=700)
        st.markdown(f"<h3 style='text-align: center; color: black;'>{caption.json().get('caption')}</h3>", unsafe_allow_html=True)


# col1, col2, col3 = st.columns(3)
# col1.text('')
# if col2.button('Get Caption'):
    
#     if image == None:
#         st.error("Insert an image!")  # handle case with no image
#     else:
#         caption = process(image, url+endpoint)
#         st.image([image], width=700)
#         # st.write(caption.json().get('caption'))  # output dyptich
#         st.markdown(f"<h3 style='text-align: center; color: black;'>{caption.json().get('caption')}</h3>", unsafe_allow_html=True)
        
import requests
import streamlit as st
import config

url = f'https://api.nasa.gov/planetary/apod?api_key={config.api_key}'

request = requests.get(url)
content = request.json()
try:
    title = content['title']
    image = content['url']
    description = content['explanation']
    image_copyright = content['copyright']
    st.header(title)
    st.image(image)
    st.text(f'\u00A9 Copyright: {image_copyright}')
    st.markdown("***")
    st.write(description)
    st.markdown("***")
except KeyError:
    title = content['title']
    image = content['url']
    description = content['explanation']
    st.header(title)
    st.image(image)
    st.markdown("***")
    st.write(description)
    st.markdown("***")



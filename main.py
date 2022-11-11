import requests
import streamlit as st

api_key = 'RfAkDInnC0UDEtgjnyxV600ftvkOlyr0gf8oQczQ'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = requests.get(url)
content = request.json()

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


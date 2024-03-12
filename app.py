import streamlit as st
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *
import warnings
import torch
import collections.abc
collections.Sized = collections.abc.Sized
from PIL import Image

st.title("Colorize_Photo :camera:")
st.markdown("## By [Johann Pineda | Add me on Linkedin | Open for work](https://www.linkedin.com/in/johannpineda/)")

# Create two columns at the bottom of your app
col1, col2 = st.columns(2)

# Display an image in each column
col1.image('black_white_example.jpg', caption='Black and White Image')
col2.image('color_image_exmaple.png.', caption='Colored Image')



# Set device
device.set(device=DeviceId.GPU0)

# Check if GPU is available
if not torch.cuda.is_available():
    st.write('GPU not available.')

# Ignore warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

# Load the pre-trained DeOldify model
colorizer = get_image_colorizer(artistic=True)

# Create a text input for the image URL
source_url = st.text_input('Enter the image URL')

# Create a slider for the render factor
render_factor = st.slider('Select the render factor', min_value=7, max_value=40, value=35)

# Create a checkbox for watermark
watermarked = st.checkbox('Watermark the image', value=True)



# If a URL is provided, colorize the image
if source_url:
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    # Convert the WindowsPath object to a string
    image_path_str = str(image_path)
    
    # Display the original image
    st.image(source_url, caption='Original Black and White Image', use_column_width=True)
    
    # Display the colorized image
    st.image(image_path_str, caption='Colorized Image', use_column_width=True)
    
    # Add a button to download the colorized image
    with open(image_path_str, 'rb') as f:
        btn = st.download_button(
            label='Download Colorized Image',
            data=f,
            file_name='colorized_image.png',
            mime='image/png'
        )
else:
    st.write('Please provide an image URL.')




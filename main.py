import streamlit as st
from PIL import Image
import requests
import base64
from io import BytesIO
from tensorflow.keras.models import load_model
from util import classify,set_background
import pandas as pd
import warnings
import tensorflow as tf

warnings.filterwarnings("ignore")


options = st.sidebar.radio("Navigation", ["Predict Material Image", "About"])

if options == "Predict Material Image":
    set_background('files/background.jpg')

    # Set title
    st.title('Garbage Classification')

    # Set header
    st.header('Please upload a material image or enter a URL')

    # Upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

    # URL input
    url = st.text_input('Enter the URL of an image:')

    # Load classifier
    model = load_model('./old_weights.h5')
    #model = tf.keras.models.load_model('./model/saved_model_format')    # after finishing training in kaggle notebook move the weights and run


    # Load class names
    with open('./files/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]

    # Display image and classify
    image = None

    if file is not None:
        # If an image is uploaded
        image = Image.open(file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_container_width=True)

    elif url:
        try:
            if url.startswith("data:image"):
                # If the URL is a base64-encoded image
                base64_data = url.split(",")[1]
                image_data = base64.b64decode(base64_data)
                image = Image.open(BytesIO(image_data)).convert('RGB')
            else:
                # If the URL is a normal web URL
                response = requests.get(url)
                response.raise_for_status()  # Raise an error if the URL is invalid
                image = Image.open(BytesIO(response.content)).convert('RGB')
            st.image(image, caption='Image from URL', use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")

    if image is not None:
        class_name, conf_score = classify(image, model, class_names)

        # Write classification
        st.write("## {}".format(class_name))
        st.write("### Score: {}%".format(int(conf_score * 1000) / 10))

    else:
        # Show an error message if no valid image is provided
        st.error("Please upload a valid image or enter a valid URL.")
elif options == "About":
    set_background('./files/background.jpg')

    # Set title
    st.title('About Team members')

    team_members = {
        "Name": ["Abdelrahman Tawfik", "Abdelrahman Safwat", "Abdelrahman Salah", "Omer Sabri", "Ahmed Ramadan",
                 "Mohamed Ahmed"],
        "ID": ["20210495", "20210510", "20210512", "20210592", "20210115", "20210731"],
        "Major": ["CS", "CS", "CS", "CS", "CS", "CS"]
    }

    # Create a DataFrame
    team_members_df = pd.DataFrame(team_members)

    st.table(team_members_df)


# material links :
#https://media.gettyimages.com/id/184941955/it/foto/per-il-riciclaggio-dei-rifiuti-di-cartone-isolato-su-bianco.jpg?s=612x612&w=gi&k=20&c=XmvHJkBKmCRnqv57DnsGyNO6XAUNBHXHm3emKlcDrBo=
#https://image.made-in-china.com/202f0j00TiJhOcMsySRZ/Wholesale-Rectangular-Metal-Cookie-Tin-Box.webp
#https://content.oppictures.com/Master_Images/Master_Variants/Variant_1500/187227.JPG
#https://cdn.thewirecutter.com/wp-content/media/2024/04/drinking-glass-2048px-7795.jpg?auto=webp&quality=75&width=



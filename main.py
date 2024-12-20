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


options = st.sidebar.radio("Navigation", ["Predict Material Image", "Metrics & Analysis"])

if options == "Predict Material Image":
    set_background('files/background.jpg')

 
    st.title('Garbage Classification')

 
    st.header('Please upload an image or enter a URL from the following categories:')


       
    st.markdown(
        """
       
        - Glass
        - Metal
        - Cardboard
        - Paper
        - Plastic
        - Trash
        """
    )

    
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

  
    url = st.text_input('Enter the URL of an image:')

    model = load_model('./files/new_weights(new_keras_version).h5')    # after finishing training in kaggle notebook move the weights and run


   
    with open('./files/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]

    
    image = None

    if file is not None:
        
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
                
                response = requests.get(url)
                response.raise_for_status() 
                image = Image.open(BytesIO(response.content)).convert('RGB')
            st.image(image, caption='Image from URL', use_column_width=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")

    if image :
        class_name, conf_score = classify(image, model, class_names)

        st.write("## {}".format(class_name))
        st.write("### Score: {}%".format(int(conf_score * 1000) / 10))

    elif image is None and url:
        st.error("Please upload a valid image or enter a valid URL.")

elif options == "Metrics & Analysis":
    set_background('./files/background.jpg')
    
    st.title('Model Performance Evaluation')
    
    
    st.markdown("---")  

    st.markdown("### Model Architecture")

    model_image1 = Image.open('./files/mobilenet_architecture.png') 
    model_image2 = Image.open('./files/mobilenet_architecture_2.jpg')
    
    col1, col2 = st.columns(2)

    with col1:
        st.image(model_image1, caption="MobileNetV2 Model Architecture 1", use_container_width=True)
    with col2:
        st.image(model_image2, caption="MobileNetV2 Model Architecture 2", use_container_width=True)

   
    st.markdown("---")  
    
    
    st.markdown("### Accuracy and Loss Curves")

    accuracy_curve = Image.open('./files/accuracy_curve.png')  
    # st.markdown("### Confusion Matrix")
    confusion_matrix_img = Image.open('./files/confusion_matrix.png')
   
    col1, col2 = st.columns(2)
    with col1:
        st.image(accuracy_curve, caption="Model Accuracy Curve", use_container_width=True)
    with col2:
        st.image(confusion_matrix_img, caption="Confusion Matrix", use_container_width=True)
    
    st.markdown("---")  
    
 
    st.markdown("""
    ### Model Performance Metrics:
    - **Precision**: 0.94
    - **Recall**: 0.94
    - **F1-Score**: 0.94
    """)

 
    st.write("Overall Accuracy: 0.94")
    st.write("Overall Loss: 0.23") 

    st.markdown("---")  
    
    st.markdown("[Kaggle Notebook for Training (click here)](https://www.kaggle.com/code/abdalrhmantwfik/keras-garbage-classification-95-accuracy)")



# material links :
#https://media.gettyimages.com/id/184941955/it/foto/per-il-riciclaggio-dei-rifiuti-di-cartone-isolato-su-bianco.jpg?s=612x612&w=gi&k=20&c=XmvHJkBKmCRnqv57DnsGyNO6XAUNBHXHm3emKlcDrBo=
#https://image.made-in-china.com/202f0j00TiJhOcMsySRZ/Wholesale-Rectangular-Metal-Cookie-Tin-Box.webp
#https://content.oppictures.com/Master_Images/Master_Variants/Variant_1500/187227.JPG
# Garbage Classification

![Demo Image](./files/demo_image.png)

## Overview
The **Garbage Classification** project aims to classify waste material images into predefined categories, such as Glass, Metal, Paper, and others. The project utilizes TensorFlow and Keras for building and training the classification model.

- Kaggle Notebook For Training : [Click here](https://www.kaggle.com/code/abdalrhmantwfik/keras-garbage-classification-95-accuracy)


## Deployment Options
<!--

### 1. **Running on Codespaces**
To quickly set up and run this project on GitHub Codespaces, follow the steps below:

#### Step 1: Set Up the Python Environment
After cloning the repository, set up the Python environment by running the following command:

```bash
source setup_env.sh
```
#### Step 2: Run the model
```bash
streamlit run main.py
```

-->

### 1. **Running the Application on GitHub Codespaces with Docker**

#### option 1: pull the image and run
```bash
docker login
```
then
```bash
docker pull abdotw/garbage_classification:v1.0
```
then
```bash
docker run -p 8000:8000 abdotw/garbage_classification:v1.0
```

#### option 2: build the image and run 
```bash
docker build -t garbage_classification .
```
then 
```bash
docker run -p 8000:8000 garbage_classification
```

### 2. **Running the Application Locally Without Docker (Using Conda)**
#### Step 1: Set Up the Python Environment
After cloning this repostitory: 
Create a new Conda environment with Python 3.10:
```bash
conda create --name env_name python=3.10
```
activate your environment
```bash
conda activate env_name
```
install pip using conda 
```bash
conda install pip
```
install packages
```bash
pip install -r requirements.txt
```

#### Step 2: Run the model
```bash
streamlit run main.py
```
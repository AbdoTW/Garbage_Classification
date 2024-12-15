# Garbage Classification

![Demo Image](./files/demo_image.png)

## Overview
The **Garbage Classification** project aims to classify waste material images into predefined categories, such as Glass, Metal, Paper, and others. The project utilizes TensorFlow and Keras for building and training the classification model.

## Deployment Options

### 1. **Running on Codespaces**
To quickly set up and run this project on GitHub Codespaces, follow the steps below:

#### Step 1: Set Up the Python Environment
After cloning the repository, set up the Python environment by running the following command:

```bash
bash setup_env.sh
```


### Step 2: Run the model
```bash
streamlit run main.py
```

### 2. **Running on Local Machine**
To run the project in your local environment, you can use Conda. Follow these steps:

### Step 1: Set Up the Python Environment
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
pip install numpy
pip install streamlit
pip install pillow
pip install keras
pip install tensorflow
```

### Step 2: Run the model
```bash
streamlit run main.py
```

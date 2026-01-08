# Handwritten Digit Recognition using MNIST

## Overview
This project implements a handwritten digit recognition system using a Convolutional Neural Network (CNN) trained on the MNIST dataset. A Streamlit web application is used to allow users to draw digits and receive real-time predictions.

## Technologies Used
- Python 3.10
- TensorFlow / Keras
- Streamlit
- MNIST Dataset
- NumPy, Pillow

## Project Structure
- `app.py` – Streamlit web application
- `mnist_digit_model.h5` – Trained CNN model
- `Handwritten_Digit_Recognition_MNIST.ipynb` – Model training notebook
- `requirements.txt` – Project dependencies

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

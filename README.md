# Handwritten Digit Recognition using MNIST

## Project Overview
This project implements a handwritten digit recognition system using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The trained model is deployed using Streamlit, allowing users to draw digits and receive real-time predictions.

## Technologies Used
- Python 3.10
- TensorFlow / Keras
- Streamlit
- MNIST Dataset
- NumPy, Pillow

## Project Structure
- `app.py` – Streamlit web application
- `mnist_digit_model.h5` – Trained CNN model
- `requirements.txt` – Python dependencies
- `colab_notebook/` – Model training notebook
- `screenshots/` – Output and UI screenshots

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

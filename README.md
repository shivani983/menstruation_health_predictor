# menstruation_health_predictor
ML model to predict your menstruation health
# Menstruation Health Predictor

This repository contains an ML model to predict your menstruation health based on various inputs. The app is built using Streamlit and utilizes a pre-trained model to generate a menses score based on user inputs.

## Features

- **User Inputs:**  
  - Number of Peaks  
  - Age  
  - Length of Cycle (days)  
  - Estimated Day of Ovulation  
  - Length of Luteal Phase (days)  
  - Length of Menses (days)  
  - Unusual Bleeding (Yes/No)  
  - Weight (kg)  
  - BMI  
  - Mean Length of Cycle (days)

- **Prediction:**  
  The app processes the input data and predicts a menses score. A score greater than 3 indicates a good score, while a score of 3 or below indicates the need to improve your physical and mental health, including focusing on your diet.

## Requirements

Ensure you have the following Python libraries installed:

- streamlit
- pandas
- numpy
- pickle (standard library)
- scikit-learn
- base64 (standard library)

You can install the required packages using pip:
```bash
pip install streamlit pandas numpy scikit-learn
git clone https://github.com/shivani983/menstruation_health_predictor.git
cd menstruation_health_predictor


streamlit run model.py

import streamlit as st 
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import base64

def load_model():
    with open("period_health_model.pkl","rb") as file:
        lr_model , la_encoder = pickle.load(file)
    return lr_model , la_encoder


def preprocessing(data, la_encoder):
    data['Unusual_Bleeding'] = la_encoder.transform(np.array(data["Unusual_Bleeding"]).reshape(-1))

    # data['Unusual Bleeding'] = la_encoder.transform(data["Unusual Bleeding"])
    df = pd.DataFrame(data)
    return df



def predict_data(data):
    lr_model,la_encoder = load_model()
    processed_data = preprocessing(data,la_encoder)
    prediction = lr_model.predict(processed_data)
    return prediction


def main():
    
    st.title("menstruation health predictor")
    st.write("please enter your data to check you period health in your mnstruation cycle")
    number_of_peak = st.number_input("Number of Peaks", min_value=0, max_value = 5, value=5)
    age = st.number_input("Age", min_value=0, step=1)
    length_of_cycle = st.number_input("Length of Cycle (days)", min_value=0, step=1)
    estimated_day_of_ovulation = st.number_input("Estimated Day of Ovulation", min_value=0, step=1)
    length_of_luteal_phase = st.number_input("Length of Luteal Phase (days)", min_value=0, step=1)
    length_of_menses = st.number_input("Length of Menses (days)", min_value=0, step=1)
    unusual_bleeding = st.selectbox("Unusual Bleeding", ["No", "Yes"])
    weight = st.number_input("Weight (kg)", min_value=0, step=1)
    bmi = st.number_input("BMI", min_value=0, value = 16)
    mean_length_of_cycle = st.number_input("Mean Length of Cycle (days)", min_value=0, step=1)
    

# Submit button
    if st.button("Submit"):
    # Store input values in a DataFrame
        data = {
            "number_of_peak": number_of_peak,
            "Age": age,
            "Length_of_cycle": length_of_cycle,
            "Estimated_day_of_ovulution": estimated_day_of_ovulation,
            "Length_of_Leutal_Phase": length_of_luteal_phase,
            "Length_of_menses": length_of_menses,
            "Unusual_Bleeding": unusual_bleeding,
            "Weight": weight,
            "BMI": bmi,
            "Mean_of_length_of_cycle": mean_length_of_cycle,
            


        }
        
        prediction = predict_data(data)

        if prediction > 3:
            st.success(f"Your menses score is {prediction}. This is a good score!")
        else:
            st.error(f"Your menses score is {prediction}. This is a bad score need to improve your physical and mental health and need to focus on your diet.")



        


if __name__ == "__main__":
    main()




    







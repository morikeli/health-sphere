from . import loader
import streamlit as st


def breast_cancer_detection_classifier(input_data):
    """ This is a function that classifies benign or malignant breast cancerous tissues. """

    prediction = loader.breast_cancer_model.predict(input_data)

    if prediction[0] == 0:
        return st.error('Diagnosis: Benign', icon='🌲')

    else:    
        return st.success('Diagnosis: Malignant!', icon='⚠️')


def diabetes_prediction_classifier(data):
    """ This is a function that classifies whether a patient is diabetic or non-diabetic. """

    data = np.asarray(data).reshape(1, -1)
    prediction = loader.diabetes_model.predict(data)

    if prediction[0] == 0:
        return st.success('Diagnosis: Non-diabetic', icon='🌲')
    
    else:
        return st.error('Diagnosis: Diabetic!', icon='💊')
    

def heart_disease_classifier(data):
    """ This function classifies whether a patient has a healthy or defective heart. """

    data = np.asarray(data).reshape(1, -1)
    prediction = loader.heart_disease_model.predict(data)

    if prediction[0] == 0:
        return st.success('Diagnosis: Patient has a healthy heart.', icon='🌲')
    
    else:
        return st.error('Diagnosis: Patient has a defective heart!', icon='🩺')
    

def parkinsons_disease_classifier(data):
    """ This function classifies whether a patient has Parkinson's disease or is healthy. """
    
    data = np.asarray(data).reshape(1, -1)
    prediction = loader.parkinsons_model.predict(data)

    if prediction[0] == 1:
        return st.error("Diagnosis: Parkinson's disease!", icon='🤒')
    
    else:
        return st.success('Diagnosis: Patient is healthy.', icon='🌲')
from utils.classifiers import (
    breast_cancer_detection_classifier,
    diabetes_prediction_classifier, 
    heart_disease_classifier, 
    parkinsons_disease_classifier
)
import streamlit as st

def index_page():
    st.set_page_config(
        page_title='Health sphere',
        page_icon=':gift_heart:',
        layout='wide',
    )


    st.title(':heart: :green[Health]-sphere')

    tabs = st.tabs([
        "Breast cancer prediction",
        "Diabetes prediction",
        "Heart disease prediction",
        "Parkinson's disease prediction",
    ])

    # breast cancer prediction tab
    with tabs[0]:
        tabs_col = st.columns([6, 6, 6], gap='medium')
        breast_cancer_tabs = st.tabs(['Mean', 'SE', 'Worst',])

        with breast_cancer_tabs[0]:
            if tabs_col[0]:
                inner_tabs = st.columns([6, 6])
                with inner_tabs[0]:
                    radius_mean = inner_tabs[0].text_input(label='Radius mean')
                    texture_mean = inner_tabs[0].text_input(label='Texture mean')
                    perimeter_mean = inner_tabs[0].text_input(label='Perimeter mean')
                    area_mean = inner_tabs[0].text_input(label='Area mean')
                    smoothness_mean = inner_tabs[0].text_input(label='Smoothness mean')
                
                with inner_tabs[1]:
                    compactness_mean = inner_tabs[1].text_input(label='Compactness mean')
                    concavity_mean = inner_tabs[1].text_input(label='Concavity mean')
                    concave_points_mean = inner_tabs[1].text_input(label='Concave points mean')
                    symmetry_mean = inner_tabs[1].text_input(label='Symmetry mean')
                    fractal_dimension_mean = inner_tabs[1].text_input(label='Fractal dimension mean')
        
        with breast_cancer_tabs[1]:
            if tabs_col[1]:
                inner_tabs = st.columns([6, 6])
                with inner_tabs[0]:
                    radius_se = inner_tabs[0].text_input(label='Radius SE')
                    texture_se = inner_tabs[0].text_input(label='Texture SE')
                    perimeter_se = inner_tabs[0].text_input(label='Perimeter SE')
                    area_se = inner_tabs[0].text_input(label='Area SE')
                    smoothness_se = inner_tabs[0].text_input(label='Smoothness SE')

                with inner_tabs[1]:   
                    compactness_se = inner_tabs[1].text_input(label='Compactness SE')
                    concavity_se = inner_tabs[1].text_input(label='Concavity SE')
                    concave_points_se = inner_tabs[1].text_input(label='Concave points SE')
                    symmetry_se = inner_tabs[1].text_input(label='Symmetry SE')
                    fractal_dimension_se = inner_tabs[1].text_input(label='Fractal dimension SE')
        
        with breast_cancer_tabs[2]:
            if tabs_col[2]:
                inner_tabs = st.columns([6, 6])
                with inner_tabs[0]:
                    radius_worst = inner_tabs[0].text_input(label='Radius worst')
                    texture_worst = inner_tabs[0].text_input(label='Texture worst')
                    perimeter_worst = inner_tabs[0].text_input(label='Perimeter worst')
                    area_worst = inner_tabs[0].text_input(label='Area worst')
                    smoothness_worst = inner_tabs[0].text_input(label='Smoothness worst')

            with inner_tabs[1]:
                compactness_worst = inner_tabs[1].text_input(label='Compactness worst')
                concavity_worst = inner_tabs[1].text_input(label='Concavity worst')
                concave_points_worst = inner_tabs[1].text_input(label='Concave points worst')
                symmetry_worst = inner_tabs[1].text_input(label='Symmetry worst')
                fractal_dimension_worst = inner_tabs[1].text_input(label='Fractal dimension worst')

        submit_button = st.button(label='Submit form')
        breast_cancer_dataset = (
            radius_mean,
            texture_mean,
            perimeter_mean,
            area_mean,
            smoothness_mean,
            compactness_mean,
            concavity_mean,
            concave_points_mean,
            symmetry_mean,
            fractal_dimension_mean,
            radius_se,
            texture_se,
            perimeter_se,
            area_se,
            smoothness_se,
            compactness_se,
            concavity_se,
            concave_points_se,
            symmetry_se,
            fractal_dimension_se,
            radius_worst,
            texture_worst,
            perimeter_worst,
            area_worst,
            smoothness_worst,
            compactness_worst,
            concavity_worst,
            concave_points_worst,
            symmetry_worst,
            fractal_dimension_worst,
        )

        if submit_button:
            with st.spinner():
                breast_cancer_detection_classifier(breast_cancer_dataset)


    # diabetes prediction tab
    with tabs[1]:
        tabs_col = st.columns([6, 6])

        with tabs_col[0]:
            diabetes_patients_age = st.number_input(label='Age',min_value=1, max_value=120,)
            diabetes_patitents_bp = st.number_input(label='Blood pressure', min_value=0, max_value=130)    # blood pressure
            diabetes_patients_bmi = st.text_input(label='Body Mass Index (BMI)')
            diabetes_pedigree_func = st.text_input(label='Diabetes pedigree function')

        with tabs_col[1]:
            diabetes_patients_glucose = st.number_input(label='Glucose', min_value=0, max_value=200)
            diabetes_patients_insulin = st.number_input(label='Insulin', min_value=0, max_value=1000)
            diabetes_patients_skin_thickness = st.number_input(label='Skin thickness', min_value=0, max_value=100)
            diabetes_patients_pregnancies = st.number_input(label='Total pregnancies', min_value=0, max_value=20)
        
        submit_button = st.button(label='Submit')
        diabetes_dataset = (
            diabetes_patients_age,
            diabetes_patitents_bp,
            diabetes_patients_bmi,
            diabetes_pedigree_func,
            diabetes_patients_glucose,
            diabetes_patients_insulin,
            diabetes_patients_skin_thickness,
            diabetes_patients_pregnancies
        )

        if submit_button:
            with st.spinner('Analyzing diagnosis'):
                diabetes_prediction_classifier(diabetes_dataset)

    # heart disease tab
    with tabs[2]:
        tabs_col = st.columns([6, 6, 6], gap='medium')
        
        with tabs_col[0]:
            patients_age = st.number_input(label='Age',min_value=10, max_value=120)
            patients_gender = st.selectbox(label='Gender', options=(None, 'Female', 'Male'), placeholder="Select patient's gender")
            patients_cp = st.number_input(label='CP',min_value=10, max_value=120)
            patients_trestbps = st.number_input(label='Trestbps',min_value=0)
        
        with tabs_col[1]:
            patients_chol = st.number_input(label='Cholestrol',min_value=0)
            patients_fbs = st.number_input(label='FBS',min_value=0)
            patients_restecg = st.number_input(label='Rest ECG',min_value=0)
            patients_thalach = st.number_input(label='Thalach',min_value=0)
        
        with tabs_col[2]:
            patients_exang = st.number_input(label='Exang',min_value=0)
            patients_oldpeak = st.text_input(label='Oldpeak')
            patients_slope = st.number_input(label='Slope',min_value=0)
            patients_ca = st.number_input(label='CA',min_value=0)
    
        patients_thal = st.number_input(label='Thal',min_value=0)

        submit_button = st.button(label='Submit data')

        if submit_button:
            pass


    # parkinson's disease
    with tabs[3]:
        inline_col = st.columns([6, 6, 6])
        extra_cols = st.columns([6, 6])

        with inline_col[0]:
            mdvp_freq = st.text_input(label='MDVP: Fo(Hz)', help='Average vocal fundamental frequency')
            mdvp_freq_high = st.text_input(label='MDVP: Fhi(Hz)', help='Maximum vocal fundamental frequency')
            mdvp_freq_low = st.text_input(label='MDVP: Flo(Hz)', help='Minimum vocal fundamental frequency')
            mdvp_jitter_perc = st.text_input(label='MDVP: Jitter(%)')
            mdvp_jitter_abs = st.text_input(label='MDVP: Jitter(Abs)')
            mdvp_rap = st.text_input(label='MDVP: (RAP)')
        
        with inline_col[1]:
            mdvp_ppq = st.text_input(label='MDVP: (PPQ)')
            jitter = st.text_input(label='Jitter')
            mdvp_shimmer = st.text_input(label='MDVP: (Shimmer)')
            mdvp_shimmer_db = st.text_input(label='MDVP Shimmer(dB)')
            mdvp_apq = st.text_input(label='MDVP: (APQ)')
            shimmer_dda = st.text_input(label='Shimmer (DDA)')
           
        with inline_col[2]:
            nhr = st.text_input(label='NHR')
            hnr = st.text_input(label='HNR')
            dfa = st.text_input(label='DFA')
            rpde = st.text_input(label='RPDE')
            d2 = st.text_input(label='D2')
            ppe = st.text_input(label='PPE')
            spread1 = st.text_input(label='Spread 1')

        spread2 = st.text_input(label='Spread 2')
        st.divider()
        submit_button = st.button(label='Submit', type='primary', use_container_width=True)
        parkisons_dataset = (
            mdvp_freq, 
            mdvp_freq_high, 
            mdvp_freq_low, 
            mdvp_jitter_perc, 
            mdvp_jitter_abs, 
            mdvp_rap,
            mdvp_ppq,
            jitter,
            mdvp_shimmer,
            mdvp_shimmer_db,
            mdvp_apq3,
            mdvp_apq5,
            mdvp_apq,
            shimmer_dda,
            nhr,
            hnr,
            rpde,
            dfa,
            spread1,
            spread2,
            d2,
            ppe,

        )

        if submit_button:
            with st.spinner('Analyszing diagnosis'):
                parkinsons_disease_classifier(parkisons_dataset)


if __name__ == '__main__':
    index_page()
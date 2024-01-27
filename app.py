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
        "Parkinson's prediction",
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






if __name__ == '__main__':
    index_page()
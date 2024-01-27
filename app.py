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

    with tabs[0]:
        tabs_col = st.columns([6, 6, 6], gap='medium')

        breast_cancer_tabs = st.tabs([
            'Mean',
            'SE',
            'Worst',
        ])

        with breast_cancer_tabs[0]:
            if tabs_col[0]:
                inner_tabs = st.columns([6, 6])
                
                with inner_tabs[0]:
                    
                    radius_mean = tabs_col[0].text_input(label='Radius mean')
                    texture_mean = tabs_col[0].text_input(label='Texture mean')
                    perimeter_mean = tabs_col[0].text_input(label='Perimeter mean')
                    area_mean = tabs_col[0].text_input(label='Area mean')
                    smoothness_mean = tabs_col[0].text_input(label='Smoothness mean')
                
                with inner_tabs[1]:
                    compactness_mean = tabs_col[0].text_input(label='Compactness mean')
                    concavity_mean = tabs_col[0].text_input(label='Concavity mean')
                    concave_points_mean = tabs_col[0].text_input(label='Concave points mean')
                    symmetry_mean = tabs_col[0].text_input(label='Symmetry mean')
                    fractal_dimension_mean = tabs_col[0].text_input(label='Fractal dimension mean')
        
        with breast_cancer_tabs[1]:
            with tabs_col[1]:
                radius_se = st.text_input(label='Radius SE')
                texture_se = st.text_input(label='Texture SE')
                perimeter_se = st.text_input(label='Perimeter SE')
                area_se = st.text_input(label='Area SE')
                smoothness_se = st.text_input(label='Smoothness SE')
                compactness_se = st.text_input(label='Compactness SE')
                concavity_se = st.text_input(label='Concavity SE')
                concave_points_se = st.text_input(label='Concave points SE')
                symmetry_se = st.text_input(label='Symmetry SE')
                fractal_dimension_se = st.text_input(label='Fractal dimension SE')
        
        with breast_cancer_tabs[2]:
            with tabs_col[2]:
                radius_worst = st.text_input(label='Radius worst')
                texture_worst = st.text_input(label='Texture worst')
                perimeter_worst = st.text_input(label='Perimeter worst')
                area_worst = st.text_input(label='Area worst')
                smoothness_worst = st.text_input(label='Smoothness worst')
                compactness_worst = st.text_input(label='Compactness worst')
                concavity_worst = st.text_input(label='Concavity worst')
                concave_points_worst = st.text_input(label='Concave points worst')
                symmetry_worst = st.text_input(label='Symmetry worst')
                fractal_dimension_worst = st.text_input(label='Fractal dimension worst')


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
            patients_oldpeak = st.number_input(label='Oldpeak',min_value=0)
            patients_slope = st.number_input(label='Slope',min_value=0)
            patients_ca = st.number_input(label='CA',min_value=0)
    
        patients_thal = st.number_input(label='Thal',min_value=0)






if __name__ == '__main__':
    index_page()
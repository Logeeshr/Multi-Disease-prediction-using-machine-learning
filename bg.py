
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('D:/New folder/streamlit/multiple/diabetes_model.sav','rb'))

heart_model = pickle.load(open('D:/New folder/streamlit/multiple/heart_model.sav','rb'))

breast_cancer_model = pickle.load(open('D:/New folder/streamlit/multiple/breast_cancer_model.sav','rb'))

parkinsons_model = pickle.load(open('D:/New folder/streamlit/multiple/parkinson_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Breast Cancer Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart-fill','person','bandaid'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    
    def add_bg_from_url():
      st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2014/11/12/19/25/diabetes-528678__340.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    
    
    # page title
    st.title('Diabetes Prediction',)
    add_bg_from_url() 
    
    
    # getting the input
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure level')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diabetes_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diabetes_prediction[0] == 1):
          diabetes_diagnosis = 'The person is Diabetic'
        else:
          diabetes_diagnosis = 'The person is not Diabetic'
        
    st.success(diabetes_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    
    def add_bg_from_url():
      st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.news-medical.net/image.axd?picture=2021%2F10%2Fshutterstock_1682046427-1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title('Heart Disease Prediction')
    add_bg_from_url() 
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (1-Male 2- Female)')
        
    with col3:
        cp = st.text_input('Chest Pain types(type-1,2,3,4')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar(1-True; 0-False)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(eg-0,1,2)')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina(1-yes,0-no)')
        
    with col1:
        oldpeak = st.text_input('ST depression ')
        
    with col2:
        slope = st.text_input('Slope of ST segment (eg-0,1,2)')
        
    with col3:
        ca = st.text_input('Major vessel colored by flourosopy(eg-0,1,2,3)')
        
    with col1:
        thal = st.text_input('Thalassemia (eg-0,1,2)')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        Heart_disease_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (Heart_disease_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    
    def add_bg_from_url():
      st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1097194912/photo/geriatric-doctor-or-geriatrician-concept-doctor-physician-hand-on-happy-elderly-senior.jpg?s=612x612&w=0&k=20&c=KXJEcMCB7_xczTEzKigrERPYn387vIQ0eudZ2GBQG7E=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title("Parkinson's Disease Prediction")
    add_bg_from_url()
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

    
    
# Breast cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    
    def add_bg_from_url():
      st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1598885159329-9377168ac375?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8Y2FuY2VyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title('Heart Disease Prediction')
    add_bg_from_url()
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        worstradius = st.text_input('Worst Radius')
    
    with col2:
        worstperimeter= st.text_input('Worst Perimeter')
        
    with col3:
        meanconcavepoints = st.text_input('Mean Concave points')
        
    with col1:
        worstconcavepoints = st.text_input('Worst Concave points')
        
    with col2:
        worstarea = st.text_input('Worst_area')
        
    with col3:
        meanperimeter = st.text_input('Mean Perimeter')
        
    with col1:
        meanconcavity= st.text_input('Mean Concavity')
        
    with col2:
        areaerror = st.text_input('Area error')
        
    with col3:
        meanarea = st.text_input('Mean area')
        
    with col1:
        worstconcavity = st.text_input('Worst concavity')

     
    # code for Prediction
    breast_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breast_disease_prediction = breast_cancer_model.predict([[worstradius, worstperimeter, meanconcavepoints , worstconcavepoints, worstarea, meanperimeter, meanconcavity, areaerror, meanarea, worstconcavity]])                          
        
        if (breast_disease_prediction[0] == 1):
         breast_diagnosis = 'The person is Malignant'
        else:
          breast_diagnosis = 'The person is benign'
        
    st.success(breast_diagnosis)
    


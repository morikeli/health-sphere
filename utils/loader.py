import pickle


# load the saved model
breast_cancer_model = pickle.load(open('utils/models/breast-cancer-model.sav', 'rb'))
diabetes_model = pickle.load(open('utils/models/diabetes-model.sav', 'rb'))
heart_disease_model = pickle.load(open('utils/models/heart-disease-model.sav', 'rb'))
parkinsons_model = pickle.load(open('utils/models/parkinsons-disease-predict.sav', 'rb'))

import pickle


# load the saved model
breast_cancer_model = pickle.load(open('breast-cancer-model.sav', 'rb'))
diabetes_model = pickle.load(open('diabetes-model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart-disease-model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons-disease-predict.sav', 'rb'))

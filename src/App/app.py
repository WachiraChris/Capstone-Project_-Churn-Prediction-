#import modules
import numpy as np
import gradio as gr
import joblib
import pandas as pd
import os


def load_model():
    cwd = os.getcwd()

    destination = os.path.join(cwd, "saved cap")

    Final_model_file_path = os.path.join(destination, "Final_model.joblib")
    preprocessor_file_path = os.path.join(destination, "preprocessor.joblib")
    

    Final_model = joblib.load(Final_model_file_path)
    preprocessor = joblib.load(preprocessor_file_path)
    

    return Final_model, preprocessor

Final_model, preprocessor = load_model()


#define prediction function
def make_prediction(REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE, ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO, ZONE1, ZONE2,MRG, REGULARITY, FREQ_TOP_PACK):
    #make a dataframe from input data
    input_data = pd.DataFrame({'REGION':[REGION], 
                               'TENURE':[TENURE], 
                               'MONTANT':[MONTANT], 
                               'FREQUENCE_RECH':[FREQUENCE_RECH], 
                               'REVENUE':[REVENUE],
                               'ARPU_SEGMENT':[ARPU_SEGMENT], 
                               'FREQUENCE':[FREQUENCE], 
                               'DATA_VOLUME':[DATA_VOLUME], 
                               'ON_NET':[ON_NET],
                               'ORANGE':[ORANGE], 
                               'TIGO':[TIGO], 
                               'ZONE1':[ZONE1], 
                               'ZONE2':[ZONE2],
                               'MRG':[MRG],
                               'REGULARITY':[REGULARITY], 
                               'FREQ_TOP_PACK':[FREQ_TOP_PACK]})
    
    transformer = preprocessor.transform(input_data)
   
    predt = Final_model.predict(transformer) 
    #return prediction
    if predt[0]==1:
        return "Customer will Churn" 
    return "Customer will not Churn"
    

#create the input components for gradio
REGION = gr.inputs.Dropdown(choices =['DAKAR', 'THIES', 'SAINT-LOUIS', 'LOUGA', 'KAOLACK', 'DIOURBEL', 'TAMBACOUNDA' 'KAFFRINE,KOLDA', 'FATICK', 'MATAM', 'ZIGUINCHOR', 'SEDHIOU', 'KEDOUGOU']) 
TENURE = gr.inputs.Dropdown(choices =['K > 24 month', 'I 18-21 month', 'H 15-18 month', 'G 12-15 month', 'J 21-24 month', 'F 9-12 month', 'E 6-9 month', 'D 3-6 month']) 
MONTANT = gr.inputs.Number()
FREQUENCE_RECH = gr.Number()
REVENUE = gr.Number()
ARPU_SEGMENT = gr.Number() 
FREQUENCE = gr.Number() 
DATA_VOLUME = gr.Number() 
ON_NET = gr.Number()
ORANGE = gr.Number()
TIGO = gr.Number()
ZONE1 = gr.Number() 
ZONE2 = gr.Number()
MRG = gr.inputs.Dropdown(choices =['NO'])    
REGULARITY = gr.Number()
FREQ_TOP_PACK = gr.Number()

output = gr.Textbox(label='Prediction')
#create the interface component

app = gr.Interface(fn =make_prediction,inputs =[REGION, 
                                                TENURE, 
                                                MONTANT, 
                                                FREQUENCE_RECH, 
                                                REVENUE, 
                                                ARPU_SEGMENT, 
                                                FREQUENCE, 
                                                DATA_VOLUME, 
                                                ON_NET, 
                                                ORANGE, 
                                                TIGO, 
                                                ZONE1, 
                                                ZONE2,
                                                MRG, 
                                                REGULARITY, 
                                                FREQ_TOP_PACK],
                                                 title ="Customer Churn Predictor", 
                                                  description="Enter the feilds Below and click the submit button to Make Your Prediction",
                                                 outputs = output)

app.launch(share = True, debug = True)
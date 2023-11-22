import json
import os
import warnings

import pandas as pd
from autogluon.tabular import TabularPredictor

from databases import *

warnings.filterwarnings("ignore")



def autogluon_classifier(code):
    predictor_class = TabularPredictor.load("AutogluonModels/deploy_class_classifier")
    
    predictor_efficiency = TabularPredictor.load("AutogluonModels/deploy_efficiency_classifier")
    

    predictions_efficiency = predictor_efficiency.predict(code)
    
    code['efficiency'] = predictions_efficiency[0]
    predictions_class = predictor_class.predict(code)
    
    code['complexity_class'] = predictions_class[0]
    
    
    
    # predictor_class.plot_ensemble_model(filename = "complexity_class_ensemble_model.png")# mostra pesos de cada modelo no emsemble
    # predictor_efficiency.plot_ensemble_model(filename = "efficiency_ensemble_model.png")# mostra pesos de cada modelo no emsemble
    
    # features_efficiency = predictor_efficiency.feature_importance(test_data) #aparentemente não muda muito
    # features_class = predictor_class.feature_importance(test_data) # aparentemente não muda muito
    # predictor_efficiency.leaderboard(test_data, silent=False) #extra_info = true
    # predictor_class.leaderboard(test_data, silent=False) #extra_info = true
    
    
    # results_efficiency = predictor_efficiency.fit_summary(show_plot=True) #descomentar 
    # results_class = predictor_class.fit_summary(show_plot=True) # descomentar
    
    
    csv_file = str(code['filename'])
    csv_file = csv_file.replace('.java', '.csv')
    # test_data.to_csv(csv_file, index=False)
    
    # Nome da pasta que você deseja criar
    folder_name = 'csv_files'

    # Cria a pasta se ela não existir
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # Cria o caminho completo para o arquivo CSV dentro da pasta
    csv_file_path = os.path.join(folder_name, csv_file)

    # Salva o DataFrame em um arquivo CSV dentro da pasta
    code.to_csv(csv_file_path, index=False)
    
    efficiency_prediction = predictions_efficiency[0]
    class_prediction = predictions_class[0]
    result = {'Efficiency': efficiency_prediction, 'Complexity class': class_prediction}
    result_json = json.dumps(result)
    return result_json




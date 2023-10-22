import json
import os

import pandas as pd
from autogluon.tabular import TabularPredictor

from databases import *


def autogluon_classifier(code_csv):
    custom_metrics = ['accuracy', 'precision', 'f1', 'recall']
    verbosity=4 # More training log. TESTAR NO TREINAMENTO, AQUI NÃO É RELEVANTE
    # eval_metrics = ['accuracy', 'precision', 'f1', 'recall'] TESTAR NO TREINAMENTO
    test_data = code_csv
    predictor_class = TabularPredictor.load("deploy_class_classifier")
    predictor_efficiency = TabularPredictor.load("deploy_efficiency_classifier")

    # predictor_class = TabularPredictor.load("AutogluonModels/ag-class_training", require_py_version_match=False)
    predictions_efficiency = predictor_efficiency.predict(test_data)
    test_data['efficiency'] = predictions_efficiency[0]
    predictions_class = predictor_class.predict(test_data)
    test_data['complexity_class'] = predictions_class[0]
    
    
    
    # predictor_class.plot_ensemble_model(filename = "complexity_class_ensemble_model.png")# mostra pesos de cada modelo no emsemble
    # predictor_efficiency.plot_ensemble_model(filename = "efficiency_ensemble_model.png")# mostra pesos de cada modelo no emsemble
    
    # features_efficiency = predictor_efficiency.feature_importance(test_data) #aparentemente não muda muito
    # features_class = predictor_class.feature_importance(test_data) # aparentemente não muda muito
    # predictor_efficiency.leaderboard(test_data, silent=False) #extra_info = true
    # predictor_class.leaderboard(test_data, silent=False) #extra_info = true
    
    # predictor_efficiency.evaluate(test_data)
    # predictor_class.evaluate(test_data)
    
    # results_efficiency = predictor_efficiency.fit_summary(show_plot=True) #descomentar 
    # results_class = predictor_class.fit_summary(show_plot=True) # descomentar
    
    # melhor_modelo1 = predictor_class.get_model_best()
    # print(melhor_modelo1)
    # melhor_modelo2 = predictor_efficiency.get_model_best()
    # print(melhor_modelo2)
    
    csv_file = str(test_data['filename'])
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
    test_data.to_csv(csv_file_path, index=False)
    
    efficiency_prediction = predictions_efficiency[0]
    class_prediction = predictions_class[0]
    result = {'Efficiency': efficiency_prediction, 'Complexity class': class_prediction}
    result_json = json.dumps(result)
    return result_json




import pandas as pd
from autogluon.tabular import TabularPredictor

# Caminho relativo para o arquivo CSV
path_crawleds = 'databases/crawleds.csv'    
path_merged = 'databases/mergeds.csv'

train_data = pd.read_csv(path_merged)
train_data_efficiency = train_data.drop(['complexity_class'], axis=1)
train_data_class = train_data

predictor = TabularPredictor(label='efficiency').fit(train_data_efficiency, presets=['medium_quality', 'optimize_for_deployment'])
predictor = TabularPredictor(label='complexity_class').fit(train_data_class, presets=['medium_quality', 'optimize_for_deployment'])

# Ensemble indices: [3]
# Ensemble weights: 
# [0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Saving AutogluonModels/ag-20230908_152733/models/WeightedEnsemble_L2/utils/oof.pkl
# Saving AutogluonModels/ag-20230908_152733/models/WeightedEnsemble_L2/model.pkl
#         0.8838   = Validation score   (accuracy)
#0.7758 class segundo
# Ensemble indices: [0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 6, 0, 8]
# Ensemble weights: 
# [0.77777778 0.         0.         0.         0.         0.
#  0.05555556 0.         0.11111111 0.05555556 0.        ]


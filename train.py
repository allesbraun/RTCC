import pandas as pd
from autogluon.tabular import TabularPredictor

# Caminho relativo para o arquivo CSV
path_crawleds = 'databases/crawled_datasets.csv'    
path_merged = 'databases/merged_datasets.csv'

train_data = pd.read_csv(path_crawleds)
train_data_efficiency = train_data.drop(['complexity_class'], axis=1)
train_data_class = train_data
# train_data_both = train_data.drop(['complexity'], axis=1) 

# custom_metrics_class = {'accuracy', 'precision', 'f1', 'recall'}
# custom_metrics_efficiency = {'accuracy', 'precision', 'f1', 'recall', 'roc_auc'}  

# predictor = TabularPredictor(label='complexity_class', eval_metric = custom_metrics_class ).fit(train_data_class,verbosity  = 4, presets=['best_quality'])
# predictor = TabularPredictor(label='efficiency', eval_metric = custom_metrics_efficiency ).fit(train_data_efficiency,verbosity  = 4, presets=['best_quality'])
predictor = TabularPredictor(label='efficiency').fit(train_data_efficiency, presets=['best_quality'])
predictor = TabularPredictor(label='complexity_class').fit(train_data_class, presets=['best_quality'])
# predictor = TabularPredictor(label=['complexity_class', 'efficiency']).fit(train_data_both,verbosity  = 4, presets=['best_quality'])

#0.6909   = Validation score   (accuracy) #class primeiro
#0.9922 efficiency segundo

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


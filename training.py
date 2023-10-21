import pandas as pd
from autogluon.tabular import TabularPredictor

# Caminho relativo para o arquivo CSV
path_crawleds = 'databases/crawled_datasets.csv'
path_paper = 'databases/paper_database.csv'

x_test = pd.read_csv(path_crawleds)

test_data = pd.read_csv(path_paper)
test_data_efficiency = test_data.drop(['complexity', 'complexity_class'], axis=1)
test_data_class = test_data.drop(['complexity'], axis=1)

predictor_efficiency = TabularPredictor.load("AutogluonModels/fixed_crawleds_best_efficiency")
predictor_efficiency.plot_ensemble_model()
predictor_class = TabularPredictor.load("AutogluonModels/fixed_crawleds_best_class")
predictor_class.plot_ensemble_model()

# predictions_efficiency = predictor_efficiency.predict(test_data_efficiency)
# predictions_class = predictor_class.predict(test_data_class)

results_efficiency = predictor_efficiency.evaluate(test_data_efficiency)
print(results_efficiency)
results_class = predictor_class.evaluate(test_data_class)
print(results_class)

from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, f1_score, precision_score,
                             recall_score)

#function to calculate the metrics of the models
# def metrics(y_test, y_pred):
#     accuracy = accuracy_score(y_test, y_pred)
#     precision = precision_score(y_test, y_pred, average='weighted', zero_division=1)
#     recall = recall_score(y_test, y_pred, average='weighted', zero_division=1)
#     f1 = f1_score(y_test, y_pred, average='weighted', zero_division=1)

#     print('Model accuracy score: {0:0.4f}'.format(accuracy))
#     print('Model precision score: {0:0.4f}'.format(precision))
#     print('Model recall score: {0:0.4f}'.format(recall))
#     print('Model F1 score: {0:0.4f}'.format(f1))
 
# print(x_test['complexity_class'].unique())
# y_pred = predictor_class.predict(x_test.drop(['complexity_class'], axis=1))
# y_test = x_test['complexity_class']
# metrics(y_test, y_pred)
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))

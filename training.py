import pandas as pd
from autogluon.tabular import TabularPredictor

# Caminho relativo para o arquivo CSV
path_crawled = 'databases/crawled_database.csv'
path_paper = 'databases/paper_database.csv'

train_crawled = pd.read_csv(path_crawled)
train_crawled_efficiency = train_crawled.drop(
    ['complexity', 'complexity_class'], axis=1)
train_crawled_class = train_crawled.drop(['complexity'], axis=1)

# predictor_efficiency = TabularPredictor(label='efficiency').fit(
#     train_crawled_efficiency, presets=['best_quality'])
# predictor_class = TabularPredictor(label='complexity_class').fit(
#     train_crawled_class, presets=['best_quality'])

test_data = pd.read_csv(path_paper)
test_data_efficiency = test_data.drop(
    ['complexity', 'complexity_class'], axis=1)
test_data_class = test_data.drop(['complexity'], axis=1)

predictor_efficiency = TabularPredictor.load(
    "AutogluonModels/crawled_efficiency")
predictor_class = TabularPredictor.load("AutogluonModels/crawled_class")

# predictions_efficiency = predictor_efficiency.predict(test_data_efficiency)
# predictions_class = predictor_class.predict(test_data_class)

results_efficiency = predictor_efficiency.evaluate(test_data_efficiency)
print(results_efficiency)
results_class = predictor_class.evaluate(test_data_class)
print(results_class)

# print(predictions_efficiency)
# print(predictions_class)

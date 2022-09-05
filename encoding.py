import numpy as np
import pandas as pd

#get train data
train_data_path ='train_data_evaluation_part_2.csv'
train = pd.read_csv(train_data_path, index_col=0)

#get test data
test_data_path ='test_data_evaluation_part2.csv'
test = pd.read_csv(test_data_path, index_col=0)

#combine dataset to preprocess
combined = train.append(test)
combined.reset_index(inplace=True)

combined.head()
combined.drop(['ID','index'], inplace=True, axis=1)




def encoding(x):
    combined.Nationality.value_counts().to_dict()
    combined_frequency_map = combined.Nationality.value_counts().to_dict()
    combined.Nationality = combined.Nationality.map(combined_frequency_map)
    return combined_frequency_map.get(x)

print(encoding('FRA'))

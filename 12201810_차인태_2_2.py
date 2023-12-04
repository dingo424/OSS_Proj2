import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

def sort_dataset(dataset_df):
	#TODO: Implement this function
	return dataset_df.sort_values(by='p_year')

def split_dataset(dataset_df):	
	#TODO: Implement this function
	label = dataset_df['salary'] * 0.001
	dataset_df = dataset_df.drop('salary', axis=1)
	return dataset_df[:1718], dataset_df[1718:], label[:1718], label[1718:]

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	return dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 
                    'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	dt_rgs = DecisionTreeRegressor()
	dt_rgs.fit(X_train, Y_train)
	return dt_rgs.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	rf_rgs = RandomForestRegressor()
	rf_rgs.fit(X_train, Y_train)
	return rf_rgs.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	svm_rgs = SVR()
	svm_rgs.fit(X_train, Y_train)
	return svm_rgs.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	return np.sqrt(np.mean((predictions - labels)**2))

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
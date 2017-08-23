# -*- coding: utf-8 -*-
"""
Data provider.

This module provides classes for loading datasets and choosing which house data 
version to be loaded

"""

import os
import numpy as np
import pandas as pd

	
def load_house(which_house=1):
	file_nr = 'House_'+str(which_house)+'.csv'
	path_data = os.path.join('D:', 'refit', 'Processed_Data_CSV', file_nr)
	data_raw = pd.read_csv(path_data, parse_dates=['Time'], index_col='Time')
	drop_cols = ['Unix','Appliance1', 'Appliance2', 'Appliance3','Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']
	data_raw = data_raw.drop(drop_cols,axis=1)
	return data_raw
		
def load_aggregate(which_house=1):
	file_nr = 'House_'+str(which_house)+'.csv'
	path_data = os.path.join('D:', 'refit', 'Processed_Data_CSV', file_nr)
	data_raw = pd.read_csv(path_data, parse_dates=['Time'], index_col='Time')
	drop_cols = ['Unix','Appliance1', 'Appliance2', 'Appliance3','Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']
	data_raw = data_raw.drop(drop_cols, axis=1)
	data = pd.DataFrame()
	data['Aggregate'] = data_raw.Aggregate.resample('H').apply(custom_resampler)
	return data


def load_appliances(which_house=1):
	file_nr = 'House_'+str(which_house)+'.csv'
	path_data = os.path.join('D:', 'refit', 'Processed_Data_CSV', file_nr)
	data_raw = pd.read_csv(path_data, parse_dates=['Time'], index_col='Time')
	data_raw['Appliances'] = data_raw[['Appliance1', 'Appliance2', 'Appliance3','Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']].sum(axis=1)
	drop_cols = ['Unix','Appliance1', 'Appliance2', 'Appliance3','Appliance4', 'Appliance5', 'Appliance6', 'Appliance7', 'Appliance8', 'Appliance9']
	data_raw = data_raw.drop(drop_cols, axis=1)
	data = pd.DataFrame()
	data['Aggregate'] = data_raw.Aggregate.resample('H').apply(custom_resampler)
	data['Appliances'] = data_raw.Appliances.resample('H').apply(custom_resampler)
	return data
	
	
def custom_resampler(array):
	return array.mean()/1000
	

	
	
	
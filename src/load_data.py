#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:43:52 2021

@author: francisalvarez
"""

import pandas as pd
import os




fp_housing_hi = '/Users/francisalvarez/Documents/Code/python/housing_price/data/raw_data/County_Top_Teri.csv'
fp_housing_lo = '/Users/francisalvarez/Documents/Code/python/housing_price/data/raw_data/County_Bottom_Teir.csv'
fp_shp_county = '/Users/francisalvarez/Documents/Code/python/housing_price/data/raw_data/CA_Counties/CA_Counties_TIGER2016.shp'


house_hi = pd.read_csv(fp_housing_hi)
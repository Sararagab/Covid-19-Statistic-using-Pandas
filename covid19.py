#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')

dataNorway = data[data["Country"] == "Norway"]
dataNorway["Date"] = pd.to_datetime(dataNorway["Date"])

plt.close("all")

plt.figure(num="Covid 19 statistics for Norway")
plt.plot(dataNorway["Date"], dataNorway["Confirmed"], marker='.', label='Confirmed')
plt.plot(dataNorway["Date"], dataNorway["Recovered"], marker='.', label='Recovered')
plt.plot(dataNorway["Date"], dataNorway["Deaths"], marker='.', label='Deaths')
plt.grid()
plt.legend()

dataNorway["New_cases"] = dataNorway["Confirmed"].diff()
dataNorway["New_cases_avg"] = dataNorway["New_cases"].rolling(window=7).mean()
plt.figure(num="New cases Norway")
plt.plot(dataNorway["Date"], dataNorway["New_cases"], marker='.', label='New cases')
plt.plot(dataNorway["Date"], dataNorway["New_cases_avg"], marker='.', label='New cases average 7 days')
plt.grid()
plt.legend()

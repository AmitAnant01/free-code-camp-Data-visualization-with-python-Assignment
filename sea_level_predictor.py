import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_pred = np.arange(df['Year'].min(), 2051)
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, color='red')

    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    x_pred_2000 = np.arange(2000, 2051)
    y_pred_2000 = res_2000.slope * x_pred_2000 + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, color='green')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_predictor.png')
    return plt.gca()
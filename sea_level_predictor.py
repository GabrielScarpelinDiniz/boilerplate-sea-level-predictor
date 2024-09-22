import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    
    plt.legend()

    x_values = np.arange(1880, 2051, 1)

    # Create first line of best fit
    first_linear_regression = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    y_values = first_linear_regression.intercept + first_linear_regression.slope * x_values
    plt.plot(x_values, y_values, color='r',label='Model 1880')

    # Create second line of best fit
    x_values = np.arange(2000, 2051, 1)
    df_2000 = df[df['Year'] >= 2000]

    second_linear_regression = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    y_values = second_linear_regression.intercept + second_linear_regression.slope * x_values
    plt.plot(x_values, y_values, color='g', label='Model 2000')




    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, color = 'blue')

    # Create first line of best fit
    regression = linregress(x, y)
    prediction_x = pd.Series(range(int(df['Year'].min()), 2051))
    prediction_y = regression.slope * prediction_x + regression.intercept
    plt.plot(prediction_x, prediction_y, color = 'red', label = 'Before')

    # Create second line of best fit
    df_now = df[df['Year'] >= 2000]
    regression_now = linregress(df_now['Year'], df_now['CSIRO Adjusted Sea Level'])
    prediction_x_now = pd.Series(range(2000, 2051))
    prediction_y_now = regression_now.slope * prediction_x_now + regression_now.intercept
    plt.plot(prediction_x_now, prediction_y_now, color = 'green', label = 'Now')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
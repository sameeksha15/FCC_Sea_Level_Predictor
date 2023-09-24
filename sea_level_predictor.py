import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  
  # Create scatter plot
  plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
  
  # Create first line of best fit
  l1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x1 = range(1880, 2051)
  y1 = x1*l1.slope + l1.intercept
  plt.plot(x1, y1)
  
  # Create second line of best fit
  df_temp = df[df['Year'] >= 2000]

  l2 = linregress(df_temp['Year'], df_temp['CSIRO Adjusted Sea Level'])
  x2 = np.arange(2000, 2051, 1)
  y2 = l2.slope*x2 + l2.intercept
  plt.plot(x2, y2)
  
  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('img/sea_level_plot.png')
  return plt.gca()

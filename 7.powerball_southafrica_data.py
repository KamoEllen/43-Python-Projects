import pandas as pd
import matplotlib.pyplot as plt

#will post url , from kaggle
data = pd.read_csv('/home/kamogelo/Downloads/archive (5)/POWERBALL.csv', usecols=['Draw No', 'Draw Date', 'Ball 1', 'Ball 2', 'Ball 3', 'Ball 4', 'Ball 5'])

data['Draw Date'] = pd.to_datetime(data['Draw Date'])

data.set_index('Draw No', inplace=True)

# Create a new column 'Total' which is the sum of all five balls
data['Total'] = data['Ball 1'] + data['Ball 2'] + data['Ball 3'] + data['Ball 4'] + data['Ball 5']

# Plot the Total numbers over time
plt.plot(data['Draw Date'], data['Total'])
plt.title('Powerball Total Numbers over Time')
plt.xlabel('Draw Date')
plt.ylabel('Total')
plt.show()

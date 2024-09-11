import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\varun\\Downloads\\ames.csv')
plt.scatter(data["SalePrice"], data["Lot.Area"])
plt.show()

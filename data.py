import seaborn as sns
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer

# Load the dataset (add parentheses)
data = load_breast_cancer()  

# Print available keys
print(data.keys())  

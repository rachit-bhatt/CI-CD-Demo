#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[2]:


# Load a built-in dataset from seaborn
data = sns.load_dataset('tips')  # You can replace 'tips' with any other dataset name

# Display the first few rows of the dataset
data


# In[3]:


# Assume 'total_bill' is the independent variable and 'tip' is the dependent variable
X = data[['total_bill']]  # Feature
y = data['tip']           # Target


# In[4]:


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[5]:


# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)


# In[6]:


# Evaluate the model
print("Coefficients:", model.coef_)
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("Coefficient of determination (R^2):", r2_score(y_test, y_pred))


# In[7]:


# Plotting the results
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Linear Regression: Total Bill vs Tip')
plt.show()


#!/usr/bin/env python
# coding: utf-8

# **APPLICATION OF 4 MOMENTS ON DATA**
# 

# ### Question 1
# 
# It is said that normal distributions are 'normal' because they can be found everywhere in Nature. Do some research and present at least 3 different examples of where normal distributions can be found in nature. For each example, do the following:
# - Explain the distribution briefly
# - Explain what variables are part of the system and why they are random or can be considered random enough for a Gaussian distribution
# - Determine whether the distribution can be modeled as a Gaussian distribution without any further manipulation (ie. a Log-Gaussian distribution)
# 
# Total Marks: 12

# #### Solution

# 1. The height of Adults
# - the distribution of different heights of adults follow a normal distribution with different frequencies of height values in a givin population
# - The variables for this system are height, genetic factors and environmental factors which can produce enough variability for a Gaussian distribution. 
# - The data provides slight deviations from a normal distribution  because of factors such as population demographics but the overall pattern can align with a Gaussian distribution.
# 
# 2. IQ scores 
# - IQ scores across a population are standardizes and well distributed which would follow a normal distribution
# - Variables of this system would include IQ score which are determined through statistical normalization and various test, because of this they can be random enought to be approximated using a Gaussian distribution.
# 
# 3. Brightness of Stars
# - The distribution of brightness of stars viewed from earth, where a large population of them can follow a normal distribution
# - The variable would be the brightness of the star, which can be influences by other variables such as distance from eath and intrinsic luminosity.  Considering observational uncertainties also, their variability can be justified as a random variables
# - Because of variables influencing the brightness of the star the central limit theorem would suggest that the brightness of stars would converge to a gaussian distribution

# ### Question 2
# 
# Use the dataset called A6_DataDistribution.txt. There are 150 values within this dataset. Please do the following:
# 
# 1. Plot a detailed and labelled frequency histogram of this data. Make sure you provide reasoning behind the number of bins chosen. [4 marks]
# 2. What kind of distribution is this? What kind of variable is "x": discrete or continuous? [1 mark]
# 3. Report the four main moments of the distribution. Make sure you print each output separately. What can you tell from the values of skewness and kurtosis? [3 marks]
# 4. Are there any outliers in this distribution? If so, how many and why? If not, defend your conclusion. Find the relative standing for each outlier, assuming we only want values to lie within two standard deviations of the mean. [4 marks]
# 5. Assuming your answer to #4 is yes, remove the outliers (in any way you wish; automated or manual) and plot another frequency histogram of the data. Report the four main moments of the distribution again. Have they changed? Explain why they did or did not change after you removed the outliers [4 marks]
# 6. Standardize your data using your updated dataset from #5 and plot the histogram again. Determine the values for the 1st, 2nd and 3rd quartiles of your standardized distribution. [2 marks]
# 
# Total Marks: 18

# #### Solution

# In[10]:


# Part 1 - Plot a Frequency Histogram of Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, skew, kurtosis, describe, zscore

data = np.loadtxt("A6_DataDistribution.txt")
fig, axis = plt.subplots(1,1,figsize=(12,6))
axis.hist(data, bins=22, width=1.9, density=True, alpha=1, color="black") 

plt.xlabel("X Values")
plt.ylabel("Frequency")
plt.title("Frequency Histogram of Data") 
plt.show()


# # Part 2 - Description of Distribution
# The variable X is continuous becase it has decimal point values and a normal distribution
# 

# In[7]:


# Part 3 - Four Main Moments of Distribution

print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Skew:", skew(data))
print("Kurtosis:", kurtosis(data)+3)

# the skewness is postive and thus the distribution is skewed to the right 
# the kurtosis is also positive so the distribution is Leptokurtic


# In[24]:


# Part 4 - Outliers


stdev = np.std(data)
newdata = []
outliers= []
for x in data:
    z_score = (x-np.mean(data))/stdev
        
    if z_score > 2 or z_score < -2:
        outliers.append(x)
        print(x, "is an outlier and has a z-score of", z_score)
        
    else:
        newdata.append(x)
        
newdata = np.array(newdata)
 


# In[28]:


# Part 5 - Remove Outliers

cleanfig, cleanaxis = plt.subplots(1,1,figsize=(12,6))
cleanaxis.hist(newdata, bins=15, width=1, density=True, alpha=1, color="grey")
plt.xlabel("X Values")
plt.ylabel("Frequency")
plt.title("Frequency Histogram of Data")
plt.show() 

print("Mean:", np.mean(newdata))
print("Variance:", np.var(newdata))
print("Skew:", skew(newdata))
print("Kurtosis:", kurtosis(newdata)+3)

#skewness is -ve which means it is skewed to the left where the outliers are on the right
#The kurtosis remains +ve, but smaller magnitudes (as it has no outliers)


# In[35]:


# Part 6 - Standardize the Distribution

standardfig, standardaxis = plt.subplots(1,1,figsize=(12,6))
standarddata = zscore(newdata) # [1 mark] for standardizing data
standardaxis.hist(standarddata, bins=15, width=0.35, density=True, alpha=1, color="beige")

plt.xlabel("X Values")
plt.ylabel("Probability")
plt.title("Standardized Distribution of Data")
plt.show()

qrt1 = np.mean(standarddata) + np.std(standarddata)*norm.ppf(0.25)
qrt2 = np.mean(standarddata) + np.std(standarddata)*norm.ppf(0.50)
qrt3 = np.mean(standarddata) + np.std(standarddata)*norm.ppf(0.75)
print("1st Quartile is:", qrt1)
print("2nd Quartile is:", qrt2)
print("3rd Quartile is:", qrt3)


# ### Question 3
# 
# We're going to explore the Maxwell-Boltzmann distribution for particle speeds in a homogeneous solution of oxygen (16 atomic mass units). Work on the following questions below:
# 1. Define a Python function to calculate the speed given a velocity, mass and temperature. Be sure to define the Boltzmann constant as well. [3 marks]
# 2. For T = 100, 200, 400, 800 K, plot the Maxwell-Boltzmann speed distribution from speeds of 0 to 2000. Make sure you determine (or pick) a value for mass $m$. What can you conclude from these curves? [6 marks]
# 3. You are given a dataset of 2000 velocity magnitudes in 3D spherical coordinates (r, phi, theta). Use the dataset called A6_MaxwellBoltzmann.txt and create a function that will return the original speed (magnitude), as well as the x, y, and z components of the speed. You should return 4 values. Note that the dataset does not include phi and theta; you will have to create random angles for each velocity. Use the `np.random.uniform` function to help with this. [4 marks]
# 4. Generate a histogram for your dataset's x, y or z component **only**, by calling your function from #3. Be sure to label everything. What do you notice about this that's unique? [3 marks]
# 5. Now, generate a histogram for your speed and find the moments of your distribution. Comment on the skewness and kurtosis. Which of the Maxwell-Boltzmann distributions does your dataset match the most in terms of temperature? [4 marks]
# 
# Total Marks: 20 marks

# #### Solution

# In[46]:


# Part 1 - Python Function
import numpy as np
import matplotlib.pyplot as plt

# Defining Boltzman's distribution for speeds
def mb_speed(vel,m,T):
    kB = 1.38e-23 
    return (m/(2*np.pi*kB*T))**1.5 * 4*np.pi * vel**2 * np.exp(-m*vel**2/(2*kB*T))


# In[64]:


# Part 2 - Plot MB Speed Distribution

#Distribution of T-values
fig_temp, ax_temp = plt.subplots()
vel = np.arange(0,2000,10)
m_ox = 2.6772032e-26 
for T in [100,200,400,800]: 
         pv = mb_speed(vel,m_ox,T)
         ax_temp.plot(vel,pv,label = "T=" + str(T) + "K")
            
ax_temp.legend(loc = "best")
ax_temp.set_xlabel("Velocity [m/s]")
ax_temp.set_ylabel("Probability Density Function of Speed")
plt.show()

# the temperature increases aswell as the average velocity increases (peak becomes less sharp)


# In[69]:


# Part 3 - Spherical to Cartesian Coordinates

def velocity_components(n):
    speed = np.loadtxt("A6_MaxwellBoltzmann.txt")
 
    phi = np.random.uniform(0,2*np.pi,n) 
    theta = np.arccos(np.random.uniform(-1,1,n)) 
 
    vx = speed*np.sin(theta)*np.cos(phi)
    vy = speed*np.sin(theta)*np.sin(phi)
    vz = speed*np.cos(theta)
    return speed, vx, vy, vz


# In[72]:


# Part 4 - Histogram for z Component

speed, vx, vy, vz = velocity_components(2000) 

vz_fig, vz_axis = plt.subplots(1,1)
vz_axis.hist(vz, bins=25, width=60, density=True, alpha=1, color="grey")
vz_axis.set_xlabel("Z-Component of Velocity")

print("Mean:", np.mean(vz))
print("Variance:", np.var(vz))
print("Skew:", skew(vz)) 
# Skew is -ve, so it is skewed to the left
print("Kurtosis:", kurtosis(vz)+3) 
# Kurtosis is positive so it is leptokurtic


# In[73]:


# Part 5 - Moments and Comparison of Speed

speed_fig, speed_axis = plt.subplots(1,1)
speed_axis.hist(speed, bins=25, width=35, density=True, alpha=1, color="royalblue")
speed_axis.set_xlabel("Speed (m/s)")

print("Mean:", np.mean(speed))
print("Variance:", np.var(speed))
print("Skew:", skew(speed)) 
# Skew is +ve, so it is skewed to the right
print("Kurtosis:", kurtosis(speed)+3) 
# Kurtosis is +ve, this implies that is has long tails and is leptokurtic

# the peak is around 450m/s which mataches best with T=100k (peak at 350m/s)
# the temperature will fall between 100k and 200k


# In[ ]:





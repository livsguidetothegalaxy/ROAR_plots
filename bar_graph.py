import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'RFI':20, 'Noise':15, 'Known Pulsars':30,
        'Candidates':35}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Catagories")
plt.ylabel("Number of plots")
plt.title("Labeling of Prepfold and Single Pulse Plots")
plt.show()

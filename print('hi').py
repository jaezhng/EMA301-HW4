from tabulate import tabulate
import pandas as pd
import numpy as np
intens = 10
t = 1
#setting up basic datatable
props = ['Index of Refraction, n', 'Absorption Coefficient (m^-1)', 'Thickness (m)']
a = [
    ["1", "1.489", "1.333", "1.460","1.489","1"],
    ["0", "0.132", "0.097", "0.132","0.132","0"],
    ["0", "0.02", "0.03", "0.025","0.02","0"]
]
df = pd.DataFrame(a, index=props, columns= ['Air','PMMA', 'Water', 'New Polymer','PMMA','Air'])
print(df)
#checks indexing system
value = df.iloc[0,0]
print(value)
float(df.iloc[0,0]) + float(df.iloc[0,1])
#runs a loop to calculate transmitted light between each medium interface
while t < 6:
    R = ((float(df.iloc[0,t]) - float(df.iloc[0,t-1]))/(float(df.iloc[0,t]) + float(df.iloc[0,t-1])))
    R2 = R**2
    print(R2)
    intens = float(intens) * (1-R2) * np.exp(float(df.iloc[1,t])*float(df.iloc[2,t])*-1)
    print(intens)
    t = t + 1

print("Final Transmitted Light Intensity (W/m^2):")
print(intens)
from tabulate import tabulate
import pandas as pd
import numpy as np
intens = 10
t = 1
props = ['Index of Refraction, n', 'Absorption Coefficient (m^-1)', 'Thickness (m)']
a = [
    ["1", "1.489", "1.333", "1.460","1.489","1"],
    ["0", "0.132", "0.097", "0.132","0.132","0"],
    ["0", "0.02", "0.03", "0.025","0.02","0"]
]
df = pd.DataFrame(a, index=props, columns= ['Air','PMMA', 'Water', 'New Polymer','PMMA','Air'])
print(df)
value = df.iloc[0,0]
print(value)
float(df.iloc[0,0]) + float(df.iloc[0,1])
#g = df['Air']
#b = df['PMMA']
#c = df['Water']
#f = df['New Polymer']
#print(g[props[1]])
#g1 = int(g[props[1]])
#g2 = int(g[props[0]])
#result = g2 + g1
#print(result)
#t represents number of trials
while t < 6:
    R = ((float(df.iloc[0,t]) - float(df.iloc[0,t-1]))/(float(df.iloc[0,t]) + float(df.iloc[0,t-1])))
    R2 = R**2
    print(R2)
    intens = float(intens) * (1-R2)**2 * np.exp(float(df.iloc[1,t])*float(df.iloc[2,t])*-1)
    print(intens)
    t = t + 1

print("Final Transmitted Light Intensity (W/m^2):")
print(intens)
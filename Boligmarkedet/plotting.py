import bolig
import matplotlib.pyplot as plt
import pandas as pd
filename = "../Data/Kvadratmeterpris" + ".csv"
df = pd.read_csv(filename, sep=";")

ax = plt.gca()
cities = ["STAVANGER", "OSLO", "BERGEN", "TRONDHEIM", "TROMSØ"]
for city in cities:
    df.plot(x='DATO', y=city, ax=ax)

plt.show()

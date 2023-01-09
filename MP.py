
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import CSV file as DataFrame

s = pd.read_csv('data_0301.csv')
print(s)
x = s["X"].to_list()
y = s["Y"].to_list()


print(x)
print(y)

plt.plot(x,y)
plt.xlabel("...X...")
plt.ylabel("...Y...")
plt.title("Mat grafic")


plt.plot(s["Y"],s["X"])
plt.xlim(0,0.7)
plt.ylim(0,2.6)
plt.savefig("im.jpg")


x_np = np.array(x)
y_np = np.array(y)

print(np.std(x_np))
print(np.std(y_np))

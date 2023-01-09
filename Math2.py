
import matplotlib.pyplot as plt
import numpy as np

labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

x = labels
y = july16_2007
y2 = july16_2020
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("date")
plt.ylabel("%")
plt.title("currency")
plt.grid()
plt.legend(labels=labels)

plt.plot(["Y"],["X"])
plt.savefig("im2.jpg")

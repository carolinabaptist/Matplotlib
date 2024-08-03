import matplotlib.pyplot as plt
import pandas as pd
#Write a Python program to draw a line with suitable label in the x axis, y axis 
# and a title.

"""
x = range(1, 50)
y = [value * 3 for value in x]
plt.plot(x, y)
plt.title("Draw a line")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
"""

#Write a Python program to draw a line using given axis values with suitable 
#label in the x axis , y axis and a title.

"""
x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
"""
#Write a Python program to draw a line using given axis values taken from 
# a text file, with suitable label in the x axis, y axis and a title.

"""
with open("test.txt") as f:
    data = f.read()
data = data.split('\n') #['1 2', '2 4', '3 1']
x = [int(el.split(' ')[0]) for el in data]
y = [int(el.split(' ')[1]) for el in data]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
"""

#Write a Python program to draw line charts of the financial data 
# of Alphabet Inc. between October 3, 2016 to October 7, 2016.

"""
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()
"""

#Write a Python program to plot two or more lines on same 
# plot with suitable legends of each line.

"""
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x1, y1, label='Line 1')
plt.plot(x2, y2, label='Line 2')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()
"""

#Write a Python program to plot two or more lines with 
#legends, different widths and colors.

"""
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x1, y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x2, y2, color='red', linewidth=5,label='line1-width-3')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()
"""

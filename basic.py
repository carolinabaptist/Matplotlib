import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl
import datetime as DT
from matplotlib.dates import date2num
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

# 7 Write a  Python program to plot two or more lines with different styles.

"""
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x1, y1, color='blue', linewidth=3, label = 'line1-dotted',linestyle='dotted')
plt.plot(x2, y2, color='red', linewidth=5, label = 'line2-dashed', linestyle='dashed')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()
"""

#8 Write a Python program to plot two or more lines and set the line markers.

"""
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x1, y1, color='blue', linewidth=3, label = 'line1-dotted',linestyle='dotted', marker='o', markerfacecolor='blue', markersize=8)
plt.plot(x2, y2, color='red', linewidth=5, label = 'line2-dashed', linestyle='dashed')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()
"""

"""
x = [1,4,5,6,7]
y = [2,6,3,6,3] 
plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')
plt.show()
"""

#9 Write a Python program to display the current axis limits values and set new axis values.

"""
x = range(1, 50)
y = [value * 3 for value in x]
plt.plot(x, y, color='blue', linewidth = 3)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line')
# shows the current axis limits values
print(plt.axis()) 
# set new axes limits
plt.axis([0, 100, 0, 200]) 
plt.show()
"""

#10. Write a Python program to plot quantities which have an x and y position.
#used pylab to make this scatter plot

"""
x1 = [2, 3, 5, 6, 8]
y1 = [1, 5, 10, 18, 20]

x2 = [3, 4, 6, 7, 9]
y2 = [2, 6, 11, 20, 22]

#blue stars and red circles
pl.plot(x1, y1,'b*', x2, y2, 'ro')
pl.show()
"""

#11. Write a  Python program to plot several lines with different format styles in one command using arrays.

"""
#from 0 to 5 with 0.2 pace
t = np.arange(0., 5., 0.2)
# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()
"""

#12. Write a Python program to create multiple types of charts (a simple curve and plot some quantities) on a single set of axes.
"""
#convert a string representing a date and/or time into a datetime object
data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

#convert date objects to floating point numbers.
x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

#blanc paper to draw the graph
fig = plt.figure()
#represent a individual graph on figure
graph = fig.add_subplot(111)
graph.plot(x,y,'r-o')
#tick position
graph.set_xticks(x)
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )
plt.show()
"""

#13 Write a Python program to display the grid and draw line charts of the closing value 
# of Alphabet Inc. between October 3, 2016 
# to October 7, 2016. Customized the grid lines 
# with linestyle -, width .5. and color blue.

"""
data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()
graph = fig.add_subplot(111)
graph.plot(x,y,'r-o')
graph.set_xticks(x)
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing stock value of Alphabet Inc.') 
plt.grid(linestyle='-', linewidth='0.5', color='blue')
plt.show()
"""

#14. Write a  Python program to display the grid and draw line charts of the
#closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. 
#Customized the grid lines with rendering with a larger grid (major grid) and 
# a smaller grid (minor grid).Turn on the grid but turn off ticks.

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()
graph = fig.add_subplot(111)
graph.plot(x,y,'r-o')
graph.set_xticks(x)
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )
plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing stock value of Alphabet Inc.') 
plt.minorticks_on()
plt.show()

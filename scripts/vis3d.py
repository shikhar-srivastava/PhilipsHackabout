import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

def make_3d(df):
    if len(df.columns)!=4:
        raise Exception('Not 3d')
        return None
    xs = df[df.columns[1]]
    ys = df[df.columns[2]]
    zs = df[df.columns[3]]
    return (xs,ys,zs)

df=pd.read_csv('../preprocessed/amlodipine.csv')

print "Compare in 3d Edematous and Normal points"
print
print "Choose any 3 numbers u fag.."
print 40*"-"
for i in range(len(df.columns)-1):
    print i+1, df.columns[i+1]
while True:
    x=int(input('X-axis: '))
    y=int(input('Y-axis: '))
    z=int(input('z-axis: '))
    print "Confirm?"
    for i in [x,y,z]:
        print i, df.columns[i]
    if raw_input('y/n') =='y':
        sublist = [df.columns[x],df.columns[y],df.columns[z]]
        plot3=df[df.Groups!=2][['Groups']+sublist]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x1,y1,z1=make_3d(plot3[plot3.Groups==1])
        x2,y2,y3=make_3d(plot3[plot3.Groups==3])
        norm=ax.scatter(x1,y1,z1,c='b')
        edem=ax.scatter(x2,y2,y3,c='r')
        ax.legend([norm,edem],['Normal','Edema'])
        ax.set_xlabel(plot3.columns[1])
        ax.set_ylabel(plot3.columns[2])
        ax.set_zlabel(plot3.columns[3])
        ax.legend(['Normal','Edema'])
        plt.show()
    else:
        continue

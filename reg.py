import math
import time
import pandas as pd
import threading
import matplotlib.pyplot as plt
import numpy
theta0 = 0
theta1 = 0
l = 0.3
df = pd.read_csv("house.csv")
def data():
        global x
        global y
        x = df['SqFt']
        y = df['Price']

def repair():
       global theta0
       global theta1
       global l
       i = 0
       sum = 0
       for i in range(x.size):
               sum = sum + ((theta0 + (theta1*x[i])) - y[i])
       sum1 = sum/x.size;
       sum = 0
       i = 0
       for i in range(x.size):
               sum = sum + (((theta0+(theta1*x[i]))-y[i]) * x[i])
       sum = sum/x.size; 
       if abs(l*sum) > 1:  
              theta0 = int(theta0 - (l*sum1))
              theta1 = int(theta1 - (l*sum))
              return 1
       return 2


def the():
        while True:
             print(theta0)
             print(theta1)


def run():
     i = 0
     try:
        threading.Thread(target=the).start()
     except:
         print("error stating thread")
     while True:
            r = repair()
            if r==2:
                break;
     print(theta0+(theta1*1000))


data()
run()
 

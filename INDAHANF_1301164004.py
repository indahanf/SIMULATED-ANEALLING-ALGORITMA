import random
import math

def fungsi(x,y):
 return -(math.fabs(math.sin(x)*math.cos(y)*math.exp(math.fabs(1-(math.sqrt(math.pow(x,2)+(math.pow(y,2)))/math.pi)))))

def fungsi2(a,b,c):
 return (math.exp(-(a-b)/c)) #acc probability

def main():
 T = 10
 T_min = 0.0000001
 alfa = 0.99999 #agar perulangan lebih banyak sehingga didapat nilai minimum terbaik

 x = random.uniform(-10, 10)
 y = random.uniform(-10, 10)
 solution = fungsi(x,y)
 while (T > T_min):
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    new = fungsi(x,y)

    if (new < solution):
        solution = new
    elif (fungsi2(new,solution,T)> random.uniform(0,1)):
        solution = new
    T = T * alfa
  #metode menurunkan suhu
 print("nilai x: ",x)
 print("nilai y: ",y)
 print("nilai minimum: ",solution)

main()
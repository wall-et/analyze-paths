import pandas as pd
from IPython.core.display import HTML



with open('titles.csv') as f:
   with open('data.csv','w') as g:
       countgood=0
       error=0
       for line in f:
           x=line.split(',')
           if len(x)==14:
               countgood+=1
               for i in range(len(x)):
                   if i<13:
                       g.write(x[i]+',')
                   else:
                       g.write(x[i])
           else:
               error+=1
with open('data.csv') as file:
    print(len(file.readlines()))
# print(titles.lines)
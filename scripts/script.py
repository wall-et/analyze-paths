import pandas as pd
from IPython.core.display import HTML
css = open('style-table.css').read() + open('style-notebook.css').read()
HTML('<style>{}</style>'.format(css))
num = 0
c = 0
with open('oddetect.csv') as file:
      with open('odd.csv', 'w') as w:
         for line in file.readlines():
            # count = sum(line.count(", ") for word in line)
            l = line.split(',')
            if len(l) == 14:
               for i in range(len(l)):
                  if i < 13:
                     w.write(l[i] + ',')
                  else:
                     w.write(l[i])
               num += 1
            else:
               c += 1

print("invalid: ",c)
print("v:", num)




import time
from itertools import cycle
l=[
    ("\ngreen",2),("yellow",0.5),("red",2)
]
c=cycle(l)
while True:
    a,b=next(c)
    print(a)
    time.sleep(b)
    

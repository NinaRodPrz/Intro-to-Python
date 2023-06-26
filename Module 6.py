import sys
from datetime import datetime 
from datetime import date 
from datetime import date 

def main():
     dt = datetime.now ()
     time_string = dt.strftime("%X")
     """https://strftime.org"""
     for line in sys.stdin:
          data = line.strip() .split("\t")
          if len(data) == 6:
               _date, _time, store, item, cost, payment = data 
               print ("{dt} \t{time_string}\t{store}\t{item}\t{cost}\t{payment}")
main()

from datetime import timedelta 
print (datetime.now()-timedelta(seconds=60))
print (datetime.now()+timedelta(days=730))

d = timedelta(days=100, seconds=36000, minutes=780000000)
print (d.days, d.seconds, d.microseconds)

datetime_object = datetime.now ()

def feetinchdate ():
     f = input ("Feet:")
     i = input ("Inches:")
     return str(f + "'" + i + "\"")

print (datetime_object, feetinchdate ())



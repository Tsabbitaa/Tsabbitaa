# -*- coding: utf-8 -*-
"""tugasloop_TsabitaAsySyahidah_SI11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uXVFd0Cnad5cIst8NoyuxzsJ14YDIjYf
"""

print("\nTugas Loop")
def main():
  fileName=input("what file are the numbers in?")
  infile=open(fileName,'r')
  sum=0.0
  count=0
  for line in infile:
    print(float (line))
    sum=sum+float(line)
    count=count+1
  print("\nThe average of the number is",sum/count)
  print("\nBanyak data",count)
  print("\nJumlah seluruh data",sum)
main()
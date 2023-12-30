# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:08:45 2023

@author: aditya
"""

import art
print(art.logo)
first_num=input("Whats the first number?:")
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
is_end=False
while is_end==False:

  for i in operations:
    print(i)
  task=input("Pick an operation:")
  second_num=input("Whats the next number?:")
  
  function=operations[task]
  result=function(float(first_num),float(second_num))
  
  print(f"{first_num} {task} {second_num} = {result}")
  choice=input(f"press 'y to continue with {result} or press'n' to exit")
  if choice == "y":
    first_num=result
    is_end=False
  else:
    is_end=True

  
  


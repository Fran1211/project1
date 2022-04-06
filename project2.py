# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 18:39:32 2022

@author: Francisco Lovera
"""
import math

num_people = int(input("How many people will be attending?"))
num_hotdogs = int(input("How many hotdogs per person?"))

hotdog_package = 10
buns_package = 8 

total_hotdogs = num_people * num_hotdogs

hotdog_needed = total_hotdogs / hotdog_package
buns_needed = total_hotdogs / buns_package

hotdogs_leftover = (math.ceil(hotdog_needed) * hotdog_package) - total_hotdogs
buns_leftover = (math.ceil(buns_needed) * buns_package) - total_hotdogs

print("The minimum number of hotdog packages required are ", math.ceil(hotdog_needed))
print("The minimum number of hotdog bun packages needed are ", math.ceil( buns_needed))
print("The number of hotdogs left over will be ", hotdogs_leftover)
print("The number of hotdog buns leftover will be ", buns_leftover)


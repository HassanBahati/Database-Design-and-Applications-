#Import csv library for opening and reading csv 
import csv

from cs50 import SQL #we are going to use this file to execute SQL queries 

open('tuesday.db', 'w').close()

db = SQL("sqlite:///tuesday.db")


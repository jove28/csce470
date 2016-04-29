from flask import render_template, flash, redirect
from app import app
import sys
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                            title='HOME_PAGE')


def getKey(item):
  return item[8]
  
@app.route('/results', methods=['POST'])
def results():
    mainDictionary = []
    inputFile = open(os.path.join("app/static", 'Database.txt'), "r")
    for line in inputFile:
        word = line.rstrip().split(',')
    mainDictionary.append(word)
    inputFile.close()
    
    sortedClasses = []
    classes = [
        ['CSCE-470', 'FALL 2013', 'CAVERLEE J', '34', '22', '7', '2', '1', '3.303', '0', '0', '0', '0', '0', ''],
        ['CSCE-470', 'FALL 2014', 'CAVERLEE J', '23', '27', '13', '2', '0', '3.092', '0', '0', '0', '1', '0', ''],
        ['CSCE-489', 'SPRING 2013', 'CAVERLEE J', '15', '6', '2', '0', '1', '3.417', '1', '0', '0', '1', '0', ''],
        ['CSCE-670', 'SPRING 2013', 'CAVERLEE J', '35', '23', '2', '0', '0', '3.550', '0', '0', '0', '0', '0', ''],
        ['CSCE-438', 'SPRING 2014', 'CAVERLEE J', '34', '24', '1', '0', '1', '3.500', '0', '0', '0', '0', '0', ''],
        ['CSCE-670', 'SPRING 2014', 'CAVERLEE J', '34', '22', '1', '1', '0', '3.534', '0', '0', '0', '0', '0', '']
        ]
        
    classes2 = [
        ['CSCE-313', 'FALL 2015', 'BETTATI R', '0', '7', '2', '1', '1', '2.364', '2', '0', '0', '6', '0', ''],
        ['CSCE-313', 'FALL 2015', 'BETTATI R', '4', '4', '2', '0', '1', '2.909', '1', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2015', 'BETTATI R', '6', '4', '3', '1', '3', '2.529', '2', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2013', 'BETTATI R', '5', '12', '5', '4', '2', '2.500', '0', '0', '0', '2', '0', ''],
        ['CSCE-313', 'SPRING 2013', 'BETTATI R', '4', '15', '5', '0', '3', '2.630', '0', '0', '0', '3', '0', ''],
        ['CSCE-313', 'SPRING 2013', 'BETTATI R', '4', '8', '9', '1', '4', '2.269', '0', '0', '0', '6', '0', ''],
        ['CSCE-313', 'SPRING 2013', 'BETTATI R', '10', '9', '3', '6', '3', '2.548', '0', '0', '0', '2', '0', ''],
        ['CSCE-313', 'SPRING 2014', 'BETTATI R', '3', '9', '3', '5', '5', '2.000', '0', '0', '0', '4', '0', ''],
        ['CSCE-313', 'SPRING 2014', 'BETTATI R', '7', '10', '3', '2', '3', '2.640', '0', '0', '0', '5', '0', ''],
        ['CSCE-313', 'SPRING 2014', 'BETTATI R', '7', '11', '3', '3', '3', '2.593', '0', '0', '0', '4', '0', ''],
        ['CSCE-313', 'SPRING 2014', 'BETTATI R', '9', '11', '2', '0', '4', '2.808', '0', '0', '0', '6', '0', ''],
        ['CSCE-313', 'SUMMER 2014', 'BETTATI R', '8', '12', '4', '1', '1', '2.962', '0', '0', '0', '2', '0', ''],
        ['CSCE-313', 'SUMMER 2015', 'BETTATI R', '7', '8', '8', '1', '0', '2.875', '0', '0', '0', '5', '0', ''],
        ['CSCE-313', 'SPRING 2014', 'GU G', '12', '3', '0', '0', '1', '3.562', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'GU G', '5', '2', '1', '0', '0', '3.500', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2013', 'HASSANZADEH A', '12', '6', '6', '4', '0', '2.929', '0', '0', '0', '3', '0', ''],
        ['CSCE-313', 'FALL 2013', 'HASSANZADEH A', '14', '5', '1', '2', '0', '3.409', '1', '0', '0', '5', '0', ''],
        ['CSCE-313', 'FALL 2013', 'HASSANZADEH A', '14', '9', '5', '1', '0', '3.241', '1', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2013', 'HASSANZADEH A', '7', '10', '3', '4', '1', '2.720', '0', '0', '0', '4', '0', ''],
        ['CSCE-313', 'SPRING 2013', 'LOGUINOV D', '5', '2', '0', '0', '0', '3.714', '0', '0', '0', '1', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'SONG D', '3', '7', '6', '3', '2', '2.286', '0', '0', '0', '3', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'SONG D', '5', '5', '3', '0', '2', '2.733', '0', '0', '0', '2', '0', ''],
        ['CSCE-313', 'FALL 2014', 'TYAGI A', '0', '4', '5', '1', '3', '1.769', '2', '0', '0', '1', '0', ''],
        ['CSCE-313', 'FALL 2014', 'TYAGI A', '4', '11', '4', '1', '1', '2.762', '2', '0', '0', '1', '0', ''],
        ['CSCE-313', 'FALL 2014', 'TYAGI A', '9', '2', '1', '0', '2', '3.143', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2014', 'TYAGI A', '12', '16', '1', '0', '1', '3.267', '2', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2014', 'TYAGI A', '10', '10', '3', '1', '4', '2.750', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2015', 'TYAGI A', '12', '10', '1', '0', '0', '3.478', '0', '0', '0', '2', '0', ''],
        ['CSCE-313', 'FALL 2015', 'TYAGI A', '13', '14', '5', '1', '0', '3.182', '1', '0', '0', '0', '0', ''],
        ['CSCE-313', 'FALL 2015', 'TYAGI A', '19', '10', '2', '0', '0', '3.548', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'TYAGI A', '16', '2', '0', '0', '0', '3.889', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'TYAGI A', '14', '4', '0', '0', '0', '3.778', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'TYAGI A', '15', '9', '2', '0', '0', '3.500', '0', '0', '0', '0', '0', ''],
        ['CSCE-313', 'SPRING 2015', 'TYAGI A', '17', '6', '2', '0', '0', '3.600', '1', '0', '0', '0', '0', '']
    ]
        
    sortedClasses = sorted(classes2,key = getKey)
        

    return render_template("results.html",
                            title = "Results_page",
                            sortedClasses = sortedClasses)
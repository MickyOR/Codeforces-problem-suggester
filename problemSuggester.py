import requests
import json
from problemGetter import getProblems
from utils import buildRequest
from userProblems import getGroupSolvedProblems

url = 'https://codeforces.com/api/'

ignoredProblemNames = [
  'Подкрутка II',
  'Подкрутка I'
]

# Handles should be a list of strings
# Tags should be a list of strings separated by semicolons
# Ratings should be a list of integers
def suggestProblems(handles, tags, ratings, count = 10):
  tagString = ''
  for tag in tags:
    tagString += tag + ';'
  tags = tagString[:-1]
  solvedProblems = getGroupSolvedProblems(handles)
  method = 'problemset.problems'
  options = {
    'tags': tagString
  }
  unsolvedProblems = []
  problems = getProblems(url, method, options, ratings)
  for problem in problems:
    if 'name' not in problem or 'contestId' not in problem or 'index' not in problem: 
      continue
    if problem['name'] in ignoredProblemNames:
      continue
    if problem['name'] not in solvedProblems:
      unsolvedProblems.append([str(problem['contestId'])+problem['index'], problem['name']])
      print(problem)
    if len(unsolvedProblems) == count:
      break
  return unsolvedProblems
  

handles = ['MickyOr', 'jnava1612', 'Anghelo', 'OPF10']
tags = ['']
ratings = [1100, 1200, 1300, 1400, 1500]
count = 3
problems = suggestProblems(handles, tags, ratings, count)
for problem in problems:
  print(problem)
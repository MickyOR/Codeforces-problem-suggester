import requests
import json
from utils import buildRequest

def getProblems(url, method, options, ratings):
  x = requests.get(buildRequest(url, method, options))
  problems = []
  for problem in x.json()['result']['problems']:
    if ratings == None:
      problems.append(problem)
    elif 'rating' in problem and problem['rating'] in ratings:
      problems.append(problem)
  return problems
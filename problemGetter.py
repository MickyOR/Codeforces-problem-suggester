import requests_async as requests
import json
from utils import buildRequest

async def getProblems(url, method, options, ratings):
  print(f'Getting list of problems')
  x = await requests.get(buildRequest(url, method, options))
  problems = []
  for problem in x.json()['result']['problems']:
    if ratings == None:
      problems.append(problem)
    elif 'rating' in problem and problem['rating'] in ratings:
      problems.append(problem)
  print(f'Done.')
  return problems
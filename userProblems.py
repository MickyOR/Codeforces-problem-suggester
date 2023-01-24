import requests_async as requests
import json
from problemGetter import getProblems
from utils import buildRequest

url = 'https://codeforces.com/api/'

async def getUserSolvedProblems(handle):
  method = 'user.status'
  options = {
    'handle': handle
  }
  print(f'Getting solved problems for {handle}')
  x = await requests.get(buildRequest(url, method, options))
  solvedProblems = set()
  for submission in x.json()['result']:
    if 'verdict' in submission and submission['verdict'] == 'OK' and 'problem' in submission and 'name' in submission['problem']:
      solvedProblems.add(submission['problem']['name'])
  print(f'Done.')
  return solvedProblems

async def getGroupSolvedProblems(handles):
  solvedProblems = set()
  for handle in handles:
    solvedProblems = solvedProblems | await getUserSolvedProblems(handle)
  return solvedProblems
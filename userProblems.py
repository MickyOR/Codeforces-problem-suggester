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
  x = await requests.get(buildRequest(url, method, options))
  solvedProblems = []
  for submission in x.json()['result']:
    if 'verdict' in submission and submission['verdict'] == 'OK' and 'problem' in submission and 'name' in submission['problem']:
      solvedProblems.append(submission['problem']['name'])
  return solvedProblems

async def getGroupSolvedProblems(handles):
  solvedProblems = []
  for handle in handles:
    solvedProblems += await getUserSolvedProblems(handle)
  return solvedProblems
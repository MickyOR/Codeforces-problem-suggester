import requests
import json
from problemGetter import getProblems
from utils import buildRequest

url = 'https://codeforces.com/api/'

method = 'user.status'

options = {
  'handle': 'MickyOr'
}

x = requests.get(buildRequest(url, method, options))

solvedProblems = []
for submission in x.json()['result']:
  if 'verdict' in submission and submission['verdict'] == 'OK' and 'problem' in submission and 'name' in submission['problem']:
    solvedProblems.append(submission['problem']['name'])

f = open("userStatus.json", "w")
f.write(str(solvedProblems))
f.close()

def getSolvedProblems(handle):
  method = 'user.status'
  options = {
    'handle': handle
  }
  x = requests.get(buildRequest(url, method, options))
  solvedProblems = []
  for submission in x.json()['result']:
    if 'verdict' in submission and submission['verdict'] == 'OK' and 'problem' in submission and 'name' in submission['problem']:
      solvedProblems.append(submission['problem']['name'])
  f = open("userStatus.json", "w")
  f.write(str(solvedProblems))
  f.close()
  return solvedProblems
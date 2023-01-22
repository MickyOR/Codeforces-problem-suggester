def buildRequest(url, method, options):
  return url + method + '?' + '&'.join([f'{k}={v}' for k, v in options.items()])
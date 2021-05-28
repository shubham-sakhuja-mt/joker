import os
import json
import socket
import datetime
import web
import urllib.request

# Endpoints
class health:
  def GET(self):
    return ''

class hello:
  def GET(self):
    return json.dumps({
      'msg': 'Hello from ' + HOST + ', request /joke and I will reply with a joke',
      'date': str(datetime.datetime.now())
    })

class joke:
  def GET(self):
    resp = {
      'host': HOST,
      'date': str(datetime.datetime.now())
    }
    print('getting joke from writer')
    failed = False
    try:
      joke_resp = urllib.request.urlopen('http://writer')
      if joke_resp.getcode() != 200:
        failed = True
    except Exception as e:
      resp['error'] = str(e)
      failed = True

    if failed:
      print('could not retrieve joke')
      return json.dumps(resp)
    
    resp.update(json.loads(joke_resp.read()))
    return json.dumps(resp)


if __name__ == '__main__':

  JOKES_LIST = []
  HOST = socket.gethostname()

  ### map uris to classes
  urls = (
    '/', 'hello',
    '/joke', 'joke',
    '/health', 'health',
  )
  app = web.application(urls, globals())

  ### start http server
  web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 80))

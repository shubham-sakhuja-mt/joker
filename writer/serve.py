import os
import json
import socket
import datetime
import web
import random

def load_jokes():
  global JOKES_LIST
  JOKES_LIST = json.load(open('jokes.json'))
  random.shuffle(JOKES_LIST)


# Endpoints
class health:
  def GET(self):
    return ''

class joke:
  def GET(self):
    if not JOKES_LIST:
      load_jokes()
    joke = JOKES_LIST.pop()
    return json.dumps({
      'joke': joke,
      'writer': HOST
    })

if __name__ == '__main__':

  JOKES_LIST = []
  HOST = socket.gethostname()

  ### map uris to classes
  urls = (
    '/', 'joke',
    '/health', 'health',
  )
  app = web.application(urls, globals())

  ### start http server
  web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 80))

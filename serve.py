#!/usr/bin/python -u

import os
import json
import web


def load_jokes():
  global JOKES_LIST
  JOKES_LIST = json.load(open('jokes.json'))


class health:

  def GET(self):
    return ''


class joke:

  def GET(self):
    if not JOKES_LIST:
      load_jokes()
    joke = JOKES_LIST.pop()
    if DEBUG:
      print('returning joke: ' + joke)
    return joke


if __name__ == '__main__':

  JOKES_LIST = []
  DEBUG = os.environ.get('DEBUG', False)

  ### map uris to classes
  urls = (
    '/health', 'health',
    '/joke', 'joke',
  )
  app = web.application(urls, globals())

  ### start http server
  web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 80))

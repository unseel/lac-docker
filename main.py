from flask import Flask, request
from LAC import LAC
from gevent.pywsgi import WSGIServer
import os
import logging

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
seg = LAC(mode='seg')

host = os.getenv("LAC_HOST", "0.0.0.0")
port = os.getenv("LAC_PORT", "5000")

@app.route("/seg", methods=["GET"])
def lac_seg():
  text = request.args.get("text")
  if not text:
    return {
      "data": []
    }

  result = seg.run(text)
  return {
    "data": result
  }

if __name__ == "__main__":
  app_server = WSGIServer((host, int(port)), app, log=app.logger)
  app_server.serve_forever()
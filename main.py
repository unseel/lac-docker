from flask import Flask, request
from LAC import LAC
from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)
seg = LAC(mode='seg')

host = os.getenv("LAC_HOST")
port = os.getenv("LAC_PORT")


@app.route("/lac/seg", methods=["GET"])
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
  app_server = WSGIServer((host, int(port)), app)
  app_server.serve_forever()
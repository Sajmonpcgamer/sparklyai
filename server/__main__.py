import flask, json
from os import getcwd

def rSCTE(txt:str):
  txt = txt.replace("ľ", "l")
  txt = txt.replace("ĺ", "l")
  txt = txt.replace("š", "s")
  txt = txt.replace("č", "c")
  txt = txt.replace("ť", "t")
  txt = txt.replace("ž", "z")
  txt = txt.replace("ý", "y")
  txt = txt.replace("á", "a")
  txt = txt.replace("í", "i")
  txt = txt.replace("é", "e")
  txt = txt.replace("ä", "a")
  txt = txt.replace("ň", "n")
  txt = txt.replace("ô", "o")
  txt = txt.replace("ú", "u")
  return txt

app = flask.Flask(__name__)

@app.route("/")
def main():
  txt = str(flask.request.args.get("txt")).lower().replace(" ", "_")
  txt = rSCTE(txt)
  if txt == "" or txt == None:
    return "error"
  f = open(getcwd() + "\\q.json", "r")
  data = json.load(f)
  f.close()
  try:
    a = str(data[txt])
    return a
  except KeyError:
    if flask.request.args.get("lang") == "sk":
      return "Neviem čo hovoríš."
    else:
      return "I don't know what are you talking about."
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False, port=80)

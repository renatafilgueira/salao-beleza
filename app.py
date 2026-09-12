from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")

@app.route("/mensagem.html")
def mensagem():
    return send_from_directory(".", "mensagem.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
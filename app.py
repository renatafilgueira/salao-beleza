from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")


@app.route("/mensagem")
def mensagem():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Uma mensagem para você</title>
    </head>

    <body style="
        margin: 0;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-family: Arial, sans-serif;
        background: linear-gradient(135deg, #fff5f8, #fce1eb);
    ">

        <div style="
            width: 90%;
            max-width: 550px;
            padding: 45px 30px;
            background: white;
            border-radius: 25px;
            box-shadow: 0 10px 35px rgba(125, 48, 79, 0.15);
        ">

            <h1 style="color: #c2185b;">
                🌹 Uma mensagem para você
            </h1>

            <p style="
                font-size: 18px;
                line-height: 1.7;
                color: #5e243b;
            ">
                Que este espaço possa trazer um pouco de beleza,
                carinho e inspiração para o seu dia. 💕
            </p>

            <p style="
                font-size: 18px;
                line-height: 1.7;
                color: #5e243b;
            ">
                Obrigada por visitar a Bella Rosa!
            </p>
            <p style="
    font-size: 18px;
    line-height: 1.7;
    color: #5e243b;
">
    Beijos, com carinho
</p>

<p style="
    font-size: 18px;
    line-height: 1.7;
    color: #c2185b;
    font-weight: bold;
">
    Renata 💗
</p>

            <a href="/" style="
                display: inline-block;
                margin-top: 25px;
                padding: 13px 25px;
                background: #c85c82;
                color: white;
                text-decoration: none;
                border-radius: 30px;
                font-weight: bold;
            ">
                Voltar para o início
            </a>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
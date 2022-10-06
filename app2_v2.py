import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('AC3.html')


@app.route('/api/jogador', methods=['POST'])
def say_name5():

    json = request.get_json()
    nome = json['nome'].upper()
    time = json['time'].upper()
    combo = json['combo'].upper()
    return jsonify(nome=nome,time=time, value=combo)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


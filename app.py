from flask import *
import pandas as pd
import os
from carro import Carro

app = Flask(__name__)


def gerar_planilha(c1: Carro, carros):
    df = pd.DataFrame()
    df['Modelo'] = [c1.nome for c1 in carros]
    df['Cor'] = [c1.cor for c1 in carros]
    df.to_excel('Carro.xlsx', index=False)  # Salva o DataFrame como um arquivo CSV temporário


@app.route('/')
def hello_world():
    # Apagar o arquivo após encerrar a sessão do navegador
    os.remove('Carro.xlsx')
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download_df():
    nome = request.form['nome_arq']
    if nome is None or nome == '':
        nome = 'default'
    arquivo = send_file('Carro.xlsx', as_attachment=True, download_name=f'{nome}.xlsx')
    return arquivo


@app.route('/dados', methods=['GET', 'POST'])
def donwload():
    carros = []
    modelo = request.form['modelo']
    cor = request.form['cor']
    c1 = Carro(modelo, cor)
    carros.append(c1)
    gerar_planilha(c1, carros)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

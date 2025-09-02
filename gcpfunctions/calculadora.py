import functions_framework
from flask import jsonify


@functions_framework.http
def calculadora(request):
    request_json = request.get_json(silent=True)
    request_args = request.args
    print(f"request_args: {request_args}")

    try:
        operacao = request_args.get('operacao')
        numero1 = request_args.get('numero1')
        numero2 = request_args.get('numero2')
        if not operacao or not numero1 or not numero2:
            raise ValueError(f"Parâmetro inválido. Esperados parametros operacao, numero1 e numero2.")

        if operacao == "soma":
            resposta = float(numero1) + float(numero2)
        else:
            raise ValueError(f"Parametro operacao incorreto: [{operacao}].")

        ret = {"mensagem": f"Segue o resultado da {operacao} entre [{numero1}] e [{numero2}]: [{resposta}].",
               "resposta": resposta,
               "autor": "Pedrinho",
               "versao": 1.0}

        return jsonify(ret), 200

    except Exception as err:
        return jsonify({"message": str(err)}), 400
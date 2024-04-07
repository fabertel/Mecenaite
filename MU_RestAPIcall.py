from flask import Flask, request, jsonify

#http://127.0.0.1:5000/somma?num1=10&num2=20

app = Flask(__name__)

@app.route('/somma', methods=['GET'])
def somma():
    # Ottieni i numeri dalla query string
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    
    # Esegui la somma
    risultato = num1 + num2
    
    # Ritorna il risultato come JSON
    return jsonify({'risultato': risultato})

if __name__ == '__main__':
    app.run(debug=True)

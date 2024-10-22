from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo desde Kubernetes v1.1 con modulo para estrezar!'

@app.route('/load')
def load():
    # Generar carga CPU
    start_time = time.time()
    while time.time() - start_time < 30:  # Mantener la carga durante 30 segundos
        x = sum(i ** 2 for i in range(10000))
    return 'Carga generada'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
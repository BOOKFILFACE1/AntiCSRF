from flask import Flask, render_template, request
from itsdangerous import TimestampSigner

app = Flask(__name__)
signer = TimestampSigner(secret_key='secret')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        # Genere un token sincronizador e inclúyalo en el formulario
        token = signer.sign(b'synchronizer-token')
        return render_template('form.html', token=token.decode())
    elif request.method == 'POST':
        # Validar el token del sincronizador
        try:
            signer.unsign(request.form['token'], max_age=60)
        except:
            return 'Invalid synchronizer token', 400
        # Procesar los datos del formulario
        return 'Form data processed successfully'

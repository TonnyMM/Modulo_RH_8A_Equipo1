from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template('comunes/login.html')

@app.route('/recopilarDatosLogin',methods=['post'])
def validarUsuario():
    return render_template('comunes/index.html')


if __name__ == '__main__':
    app.run(debug=True)


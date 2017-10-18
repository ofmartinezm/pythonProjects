import json
from flask import Flask,request,render_template, url_for, redirect



app=Flask(__name__)


"""@app.route("/hola")
def hello(usuario="invitado"):
    nombre= request.args.get('nombre', usuario)
    return "Hola {}".format(nombre)"""

@app.route("/")
def hello(nombre="invitado"):
    return "Hola {}".format(nombre)

@app.route("/chao")
def chao():
    return "Chao Mundo Python es lo mejor"

@app.route("/index/")	
def hola_mundo(nombre="Invitado"):
	try:
		data=json.loads(request.cookies.get('data'))
	except TypeError:
		data={}
	else:
		nombre=data.get('nombre')
		
	contexto={'nombre':nombre}
	return render_template("index.html",**contexto)

	
"""@app.route("/suma")
def suma(num1=0, num2=0):
    num1=request.args.get('num1', num1)
    num2 = request.args.get('num2', num2)
    resultado=int(num1)+int(num2)
    return "{} mas {} es igual a{}".format(num1,num2,resultado)"""

@app.route("/suma/<float:num1>/<int:num2>")
@app.route("/suma/<int:num1>/<float:num2>")
@app.route("/suma/<float:num1>/<float:num2>")
@app.route("/suma/<int:num1>/<int:num2>")
def suma(num1=0, num2=0):
    contexto={'num1':num1,'num2':num2}
    return render_template("suma.html",**contexto)

@app.route("/contacto/")
def contacto():
	return render_template("contacto.html")	
	
@app.route("/enviar", methods=['POST'])
def enviar():
	response= redirect(url_for('hola_mundo'))
	response.set_cookie('data',json.dumps(dict(request.form.items())))
	return response	
	
	
	
if __name__ =="__main__":
    app.run(debug=True)
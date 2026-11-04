import random


from flask import Flask

 
app = Flask(__name__)

cartas = ["Cristiano Ronaldo", "Neymar", "Messi",]
 
@app.route("/")
def index():
    return '''
        <h1>Bem-vindo ao Trunfo de Futebol!</h1>
        <p>Abra um pacotinho e descubra a sua carta.</p>
        <a href="/pacotinho">Abrir pacotinho</a>
    '''

@app.route("/pacotinho")
def pacotinho():
    carta = random.choice(cartas)
    return f'''
        <h1>Sua carta sorteada é: {carta}</h1>
        <p>Atualize a página para abrir outro pacotinho!</p>
        <a href="/">Voltar</a>
    '''









 
app.run(debug=True)

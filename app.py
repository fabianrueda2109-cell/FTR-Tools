from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return '''
    <h1>FTR TOOLS</h1>
    <p>Tu caja de herramientas</p>
    <a href="/calculadora">Calculadora</a>
    '''


@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():

    if request.method == "POST":

        numero1 = float(request.form["numero1"])
        numero2 = float(request.form["numero2"])
        operacion = request.form["operacion"]

        if operacion == "sumar":
            resultado = numero1 + numero2

        elif operacion == "restar":
            resultado = numero1 - numero2

        elif operacion == "multiplicar":
            resultado = numero1 * numero2

        elif operacion == "dividir":

            if numero2 == 0:
                return '''
                <h1>FTR TOOLS</h1>
                <h2>Error</h2>
                <p>No se puede dividir entre 0.</p>
                <a href="/calculadora">Volver</a>
                '''

            resultado = numero1 / numero2

        return f'''
        <h1>Calculadora FTR</h1>
        <p>{numero1} {operacion} {numero2} = {resultado}</p>
        <a href="/calculadora">Volver a calcular</a>
        '''

    return '''
    <h1>Calculadora FTR</h1>
    <p>Introduce dos números:</p>

    <form method="POST">

        <input
            type="number"
            name="numero1"
            placeholder="Número 1"
            step="any"
            required
        >

        <br><br>

        <input
            type="number"
            name="numero2"
            placeholder="Número 2"
            step="any"
            required
        >

        <br><br>

        <button name="operacion" value="sumar">Sumar</button>
        <button name="operacion" value="restar">Restar</button>
        <button name="operacion" value="multiplicar">Multiplicar</button>
        <button name="operacion" value="dividir">Dividir</button>

    </form>

    <br>

    <a href="/">Volver a FTR Tools</a>
    '''


if __name__ == "__main__":
    app.run(debug=True)
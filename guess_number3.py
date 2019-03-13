from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def zgadywanka():
    form = """
    <form action="/" method='POST'>
    <label>Pomyśl liczbę od 0 do 1000, a ja zgadnę ją w max. 10 krokach<br>
    {}
        <input type="hidden" name="guess" value = "{}"></input>
        <input type="hidden" name="min" value = "{}"></input>
        <input type="hidden" name="max" value = "{}"></input>
        <button type="submit" name = "answer" value = "mniej">Mniej</button> <button type="submit" name = "answer" value = "więcej">Więcej</button> <button type="submit" name = "answer" value = "trafiłeś">Trafiłeś</button>
    </form>
    """
    if request.method == "GET":
        min = 1
        max = 1000
        guess = int((max - min) / 2 + min)
        return form.format("Zgaduję: " + str(guess), guess, min, max)
    else:
        answer = request.form['answer']
        min = int(request.form['min'])
        max = int(request.form['max'])
        guess = int(request.form['guess'])
        for i in range(11):
            if min - 1 == max or max + 1 == min:
                return "Nie oszukuj!"
            elif answer == "mniej":
                max = guess - 1
                guess = int((max - min) / 2 + min)
                return form.format("Zgaduję: " + str(guess), guess, min, max)

            elif answer == "więcej":
                min = guess + 1
                guess = int((max - min) / 2 + min)
                return form.format("Zgaduję: " + str(guess), guess, min, max)

            elif answer == "trafiłeś":
                return "Wygrałem!"


app.run(debug = True)


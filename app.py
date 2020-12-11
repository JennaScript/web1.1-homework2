from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'flavor' : request.args.get('flavor'),
        'toppings' : request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?<br/>
        <input type="text" name="color"><br/>
        What is your favorite animal?<br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
        </form>
        """
        
@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_input_color = request.args.get('color')
    user_input_animal = request.args.get('animal')
    user_input_city = request.args.get('city')
    return f"Wow, I didn't know {user_input_color} {user_input_animal}s lived in {user_input_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results", method="POST">
        Please enter your secret message: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
        </form>
    """

@app.route('/message_results', methods=['POST'])
def sort_letters(secret_message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(secret_message)))    
    print (f("Here is your secret message! <br/>{{sort_letters}}"))

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of two operands and chosen operator."""
    context = {
        'operand1' : int(request.args.get('operand1')),
        'operand2' : int(request.args.get('operand2')),
        'operation' : request.args.get('operation'),
    }
    return render_template('calculator_results.html', **context)

if __name__ == '__main__':
    app.run()

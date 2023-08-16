
from flask import Flask, render_template, request
import requests
from models.pokemon import Pokemon


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        nome_pokemon = request.form["nome"]
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}")
        
        if response.status_code == 200:
            data = response.json()
            pokemon = Pokemon(
                name=data['name'],
                hp=data['stats'][0]['base_stat'],
                attack=data['stats'][1]['base_stat'],
                defense=data['stats'][2]['base_stat'],
                special_attack=data['stats'][3]['base_stat'],
                special_defense=data['stats'][4]['base_stat'],
                speed=data['stats'][5]['base_stat'],
                photo=data['sprites']['front_default']
            )
            
            return render_template('index.html', pokemon=pokemon)
        else:
            return render_template('index.html', error="Pokémon não encontrado")
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
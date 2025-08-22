from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime
import json

app = Flask(__name__)

# Configuração da API (OpenWeatherMap gratuita)
API_KEY = os.environ.get('WEATHER_API_KEY', 'demo_key')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Cache simples em memória
weather_cache = {}

def get_weather_data(city):
    """Busca dados do clima para uma cidade"""
    try:
        # Verificar cache (válido por 10 minutos)
        now = datetime.now()
        cache_key = city.lower()
        
        if cache_key in weather_cache:
            cached_data, cache_time = weather_cache[cache_key]
            if (now - cache_time).seconds < 600:  # 10 minutos
                cached_data['from_cache'] = True
                return cached_data
        
        # Fazer requisição para API real
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Formatar dados
            weather_info = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon'],
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'from_cache': False
            }
            
            # Salvar no cache
            weather_cache[cache_key] = (weather_info, now)
            return weather_info
        else:
            return {'error': 'Cidade não encontrada'}
            
    except requests.RequestException:
        return {'error': 'Erro de conexão com a API'}
    except Exception as e:
        return {'error': f'Erro interno: {str(e)}'}

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/weather/<city>')
def weather_city(city):
    """Endpoint para buscar clima de uma cidade específica"""
    weather_data = get_weather_data(city)
    return jsonify(weather_data)

@app.route('/api/weather', methods=['POST'])
def api_weather():
    """API endpoint para buscar clima"""
    data = request.get_json()
    if not data or 'city' not in data:
        return jsonify({'error': 'Campo "city" é obrigatório'}), 400
    
    weather_data = get_weather_data(data['city'])
    return jsonify(weather_data)

@app.route('/health')
def health_check():
    """Health check para monitoramento"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'cache_size': len(weather_cache),
        'version': '1.0.0'
    })

@app.route('/status')
def status():
    """Status da aplicação"""
    return jsonify({
        'app': 'Weather App DevOps',
        'version': '1.0.0',
        'status': 'running',
        'cached_cities': list(weather_cache.keys()),
        'uptime': 'Sistema ativo'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint não encontrado'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
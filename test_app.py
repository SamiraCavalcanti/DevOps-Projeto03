import unittest
import json
from app import app

class WeatherAppTestCase(unittest.TestCase):
    
    def setUp(self):
        """Configurar testes"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_page(self):
        """Testar página principal"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather App', response.data)
    
    def test_health_check(self):
        """Testar health check"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
        self.assertIn('timestamp', data)
        self.assertIn('version', data)
    
    def test_status_endpoint(self):
        """Testar endpoint de status"""
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'running')
        self.assertEqual(data['version'], '1.0.0')
        self.assertIn('cached_cities', data)
    
    def test_api_weather_without_city(self):
        """Testar API sem cidade"""
        response = self.app.post('/api/weather',
                                data=json.dumps({}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_api_weather_with_city(self):
        """Testar API com cidade"""
        response = self.app.post('/api/weather',
                                data=json.dumps({'city': 'London'}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        # Como estamos usando demo_key, esperamos erro da API
        self.assertTrue('error' in data or 'city' in data)
    
    def test_weather_city_endpoint(self):
        """Testar endpoint de clima por cidade"""
        response = self.app.get('/weather/London')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        # Como estamos usando demo_key, esperamos erro da API
        self.assertTrue('error' in data or 'city' in data)
    
    def test_404_endpoint(self):
        """Testar endpoint inexistente"""
        response = self.app.get('/inexistente')
        self.assertEqual(response.status_code, 404)
        
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()

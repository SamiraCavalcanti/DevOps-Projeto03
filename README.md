# 🌤️ Weather App DevOps

Uma aplicação web completa de clima desenvolvida em Flask para demonstrar um pipeline completo de CI/CD.

## 🚀 **Funcionalidades**

### **🌍 Aplicação Web:**
- **Busca de clima** por cidade
- **Interface bonita** e responsiva  
- **Cache inteligente** (10 minutos)
- **Múltiplos endpoints** REST API
- **Monitoramento** com health checks

### **📡 API Endpoints:**
- `GET /` - Interface web principal
- `GET /weather/{cidade}` - Buscar clima por cidade
- `POST /api/weather` - API REST para busca
- `GET /health` - Health check para monitoramento
- `GET /status` - Status da aplicação

### **⚙️ Pipeline DevOps:**
- **CI/CD completo** com GitHub Actions
- **Testes automatizados** (unitários + integração)
- **Build Docker** automático
- **Deploy automático** no Render
- **Monitoramento** e logs

## 🛠️ **Tecnologias**

### **Backend:**
- **Python 3.9** + **Flask**
- **OpenWeatherMap API** (clima)
- **Requests** (HTTP client)
- **Cache em memória**

### **Frontend:**
- **HTML5** + **CSS3** + **JavaScript**
- **Design responsivo**
- **Gradientes e animações**

### **DevOps:**
- **Docker** (containerização)
- **GitHub Actions** (CI/CD)
- **Docker Hub** (registry)
- **Render** (deploy)

## 📦 **Estrutura do Projeto**

```
📁 DevOps-projeto03/
├── 🐳 Dockerfile                    # Container da aplicação
├── 📋 requirements.txt              # Dependências Python
├── 🐍 app.py                       # Aplicação Flask principal
├── 🧪 test_app.py                  # Testes unitários
├── 📁 templates/
│   └── 🌐 index.html               # Interface web
├── 📁 .github/workflows/
│   └── ⚙️ ci-cd.yml                # Pipeline CI/CD
├── 🚫 .dockerignore                # Arquivos ignorados Docker
├── 📖 DEPLOY-RENDER.md             # Instruções deploy
├── 📄 LICENSE                      # Licença do projeto
└── 📄 README.md                    # Esta documentação
```

## 🔧 **Como executar localmente**

### **1. Clonar repositório:**
```bash
git clone https://github.com/SamiraCavalcanti/DevOps-Projeto03.git
cd DevOps-projeto03
```

### **2. Instalar dependências:**
```bash
pip install -r requirements.txt
```

### **3. Executar aplicação:**
```bash
python app.py
```

### **4. Acessar:**
- **App:** http://localhost:5000
- **Health:** http://localhost:5000/health
- **Status:** http://localhost:5000/status

## 🐳 **Docker**

### **Build:**
```bash
docker build -t weather-app .
```

### **Run:**
```bash
docker run -p 5000:5000 weather-app
```

## 🧪 **Testes**

### **Executar testes:**
```bash
python test_app.py
```

### **Testes inclusos:**
- ✅ Importação da aplicação
- ✅ Endpoints básicos
- ✅ Health checks
- ✅ API endpoints
- ✅ Tratamento de erros

## 🌐 **Deploy**

### **Automático:**
- **Push** para `main` → **GitHub Actions** → **Build Docker** → **Docker Hub** → **Deploy Render**

### **Manual no Render:**
1. Conectar repositório GitHub
2. Configurar Runtime: Docker
3. Registry: Docker Hub
4. Image: `samiracavalcanti/devops-projeto03:latest`

## 📊 **Monitoramento**

### **Health Checks:**
- `GET /health` - Status da aplicação
- `GET /status` - Informações detalhadas

### **Logs:**
- Cache de cidades consultadas
- Timestamps de requisições
- Origem dos dados (cache/API)

## 🔑 **Configuração da API**

Para usar a API real do OpenWeatherMap:

1. **Obter chave:** https://openweathermap.org/api
2. **Configurar variável:** `WEATHER_API_KEY=sua_chave_aqui`

**Nota:** Funciona sem chave (modo demo) para testes.

## 🎯 **Exemplo de Uso**

### **Interface Web:**
1. Acesse a aplicação
2. Digite nome da cidade
3. Veja clima em tempo real

### **API REST:**
```bash
# Buscar clima de São Paulo
curl http://localhost:5000/weather/São%20Paulo

# Via POST
curl -X POST http://localhost:5000/api/weather \
  -H "Content-Type: application/json" \
  -d '{"city": "Rio de Janeiro"}'
```

## 📈 **Pipeline CI/CD**

### **Continuous Integration:**
- ✅ Testes automáticos
- ✅ Validação de código
- ✅ Build Docker
- ✅ Verificação de dependências

### **Continuous Deployment:**
- 🚀 Deploy automático
- 🐳 Containerização
- 📦 Registry (Docker Hub)
- 🌐 Produção (Render)

### **Fluxo completo:**
```
git push → GitHub Actions → Testes → Build Docker → Push Docker Hub → Deploy Render → App Online
```

## 🎉 **Demonstração**

**App ao vivo:** https://devops-projeto03.onrender.com

---

**🚀 Projeto DevOps completo - Do código à produção!**

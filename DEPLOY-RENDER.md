# Deploy no Render - Instruções Passo a Passo

## 🚀 Como conectar ao Render (GRATUITO)

### 1. **Criar conta no Render**
- Acesse: https://render.com/
- Clique **"Get Started for Free"**
- **Login com GitHub** (recomendado)

### 2. **Conectar repositório**
- No dashboard do Render, clique **"New +"**
- Escolha **"Web Service"**
- **Connect GitHub** → Encontre `DevOps-Projeto03`
- Clique **"Connect"**

### 3. **Configurações REAIS que aparecem no Render**
```
Name: devops-projeto03
Runtime: Python 3
Region: Oregon (US West) 
Branch: main
Root Directory: (deixe vazio)
Build Command: pip install -r requirements.txt
Start Command: python app.py
Instance Type: Free
```

### 4. **Campos importantes**
- **Plan**: Starter (Free)
- **Auto-Deploy**: ✅ Yes
- **Advanced**: 
  - Port: (automático - detecta 5000)
  - Health Check Path: /

### 5. **Alternativa: Deploy com Docker**
Se quiser usar a imagem Docker do pipeline:
```
Environment: Docker
Docker Command: (deixe vazio - usa o Dockerfile)
ou
Registry: Docker Hub
Image: samiracavalcanti/devops-projeto03:latest
```

### 6. **Finalizar**
- Clique **"Create Web Service"**
- ⏳ Aguarde o primeiro deploy (2-3 minutos)
- 🎉 Render gerará uma URL: `https://devops-projeto03.onrender.com`

## ✅ **Após conectar:**
- ✅ **Auto-deploy**: A cada push na branch `main`
- ✅ **URL automática**: HTTPS incluído
- ✅ **Logs**: Monitoramento em tempo real
- ✅ **Zero configuração**: Tudo automático

## � **Fluxo completo:**
```
git push → GitHub Actions → Docker Hub → Render → App Online
```

**Pronto!** Seu pipeline CI/CD estará 100% funcional! 🎉

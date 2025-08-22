# GitHub Actions Setup

Este diretório contém os workflows do GitHub Actions para CI/CD.

## Estrutura

```
.github/
└── workflows/
    └── ci-cd.yml    # Pipeline principal de CI/CD
```

## Configuração necessária

### 1. Secrets do GitHub
Para que o workflow funcione completamente, você precisa configurar os seguintes secrets no GitHub:

1. Vá para: **Settings** → **Secrets and variables** → **Actions**
2. Adicione os secrets:
   - `DOCKER_USERNAME`: Seu username do Docker Hub
   - `DOCKER_PASSWORD`: Seu token/password do Docker Hub

### 2. O que o workflow faz

**CI (Continuous Integration):**
- ✅ Testa o código Python
- ✅ Verifica se as dependências instalam corretamente
- ✅ Valida se a aplicação importa sem erros

**CD (Continuous Deployment):**
- 🐳 Constrói a imagem Docker
- 📤 Faz push para o Docker Hub
- 🏷️ Cria tags automáticas
- 💾 Usa cache para builds mais rápidas

### 3. Triggers
O workflow executa quando:
- Há push na branch `main`
- Há pull request para a branch `main`

### 4. Próximos passos
- Adicionar testes unitários reais
- Configurar deploy para produção
- Adicionar notificações (Slack, email, etc.)

# Etapa 1: Construção do projeto Vue.js com Vite
FROM node:18 AS builder

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências e instala os pacotes
COPY package.json package-lock.json ./
RUN npm install

# Copia o restante do projeto para o container
COPY . .

# Gera os arquivos otimizados de produção
RUN npm run build

# Etapa 2: Servindo a aplicação com Nginx
FROM nginx:1.23-alpine

# Remove configuração padrão do Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Copia a configuração customizada do Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copia os arquivos buildados pelo Vite para o diretório do Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Expõe a porta 80 para acesso ao frontend
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]

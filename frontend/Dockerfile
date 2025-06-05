# Використовуємо легкий Node.js
FROM node:14-alpine

WORKDIR /usr/src/app

# Копіюємо package.json (і package-lock.json, якщо є)
COPY package.json package-lock.json* ./

# Встановлюємо залежності (в даному випадку тільки express)
RUN npm install

# Копіюємо директорію public і server.js
COPY public ./public
COPY server.js ./

EXPOSE 3000

CMD ["node", "server.js"]

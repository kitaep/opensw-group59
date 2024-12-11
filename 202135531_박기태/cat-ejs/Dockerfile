FROM node:latest

WORKDIR /app

COPY . .

RUN npm install

# Create user and set permissions
RUN useradd -m web \
    && chmod -R 755 /app \
    && find /app -type f -exec chmod 755 {} \; \
    && chown -R root:web /app

USER web

CMD ["node", "app.js"]

FROM node:18-alpine
WORKDIR /app

# Copy package files first
COPY package.json package-lock.json* ./

# Try different registry or no registry (use default)
RUN npm config set registry https://registry.npmjs.org/ && \
    npm install --fetch-timeout=600000 --fetch-retries=10 --prefer-offline

# Copy the rest of the code
COPY . .

# Build the application
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
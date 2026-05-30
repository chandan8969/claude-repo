# Multi-stage Build for Astro Portfolio

# Stage 1: Build
FROM node:24-alpine AS build
WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm install

# Copy source and build
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
# Copy build artifacts from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom Nginx config
COPY infrastructure/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

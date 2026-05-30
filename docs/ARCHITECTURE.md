# 🏗 Architecture Documentation

This document outlines the technical architecture of the Technical Portfolio Showcase.

## 🌐 System Overview

The project uses a decoupled architecture consisting of a static frontend, a lightweight API backend, and a containerized infrastructure for consistent deployment.

### High-Level Architecture
`User` $\rightarrow$ `DNS/Domain` $\rightarrow$ `Nginx Reverse Proxy` $\rightarrow$ { `Astro Frontend (Static)` , `FastAPI Backend (API)` }

## 🛠 Component Breakdown

### 1. Frontend (Astro)
- **Role:** Handles content delivery, routing, and UI rendering.
- **Design Philosophy:** Static Site Generation (SSG) for maximum performance and SEO.
- **Styling:** Utility-first CSS via Tailwind for rapid, responsive UI development.
- **Content:** Markdown-based project collections for easy content management.

### 2. Backend (FastAPI)
- **Role:** Manages dynamic requests, contact form submissions, and portfolio analytics.
- **Design Philosophy:** Asynchronous Python (ASGI) for high concurrency and low latency.
- **API Design:** RESTful endpoints with automatic OpenAPI (Swagger) documentation.

### 3. Infrastructure (Docker & Nginx)
- **Nginx:** Acts as the entry point, handling SSL termination and routing requests to the correct container.
- **Multi-Stage Builds:** Dockerfiles are optimized to separate the build environment from the runtime environment, reducing image size.
- **Orchestration:** `docker-compose` is used to manage the lifecycle of the frontend and backend services as a single unit.

## 📊 Data Flow

### Request Lifecycle
1. **Static Request:** A user requests a project page $\rightarrow$ Nginx serves the pre-rendered HTML from the Astro container.
2. **Dynamic Request:** A user submits a contact form $\rightarrow$ Nginx forwards the request to the FastAPI container $\rightarrow$ Backend processes the email/log $\rightarrow$ Returns success response.

## 🛡 Security & Performance
- **Static Assets:** Served as immutable files for maximum cacheability.
- **CORS:** Configured in FastAPI to allow only authorized frontend origins.
- **Container Isolation:** Each service runs in its own isolated environment, reducing the attack surface.

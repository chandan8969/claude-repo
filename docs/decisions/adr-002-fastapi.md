# ADR 002: Choice of Backend Framework

**Date**: 2026-05-19
**Status**: Accepted

## Context
Phase 2 requires a backend to handle dynamic interactions: a contact form and project view tracking. The solution needs to be lightweight, easy to containerize, and consistent with the user's skill set (Java/Python).

## Decision
We will use **FastAPI (Python)** for the backend.

## Consequences
- **Pros**:
    - **Skill Showcase**: Highlights the user's Python proficiency.
    - **Performance**: Extremely high performance and asynchronous capabilities.
    - **Developer Experience**: Automatic OpenAPI/Swagger documentation.
    - **Simplicity**: Minimal boilerplate for a small set of API endpoints.
- **Cons**:
    - Introduces a second language (Python) into the project's runtime environment (Node.js for frontend).
    - Requires a separate Docker image and container.

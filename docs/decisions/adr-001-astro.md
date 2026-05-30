# ADR 001: Choice of Frontend Framework

**Date**: 2026-05-19
**Status**: Accepted

## Context
We need a professional portfolio website to showcase GitHub projects. The requirements include high performance, easy content management (projects), and a clear path to future backend integration.

## Decision
We will use **Astro** with **Tailwind CSS** and **TypeScript**.

## Consequences
- **Pros**:
    - Extremely fast initial load (zero-JS by default).
    - First-class Markdown/MDX support for project content.
    - Easy transition to Server-Side Rendering (SSR) in Phase 2.
    - Tailwind CSS allows for rapid, consistent UI development.
- **Cons**:
    - Slightly different mental model than pure React/Vue (Islands architecture).
    - New build tool for those unfamiliar with Astro.

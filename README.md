# APP

Este repositorio contiene diferentes proyectos y pruebas automatizadas.

## Carpetas principales
- **PLAYWRIGHT/** → pruebas automatizadas con Playwright.
- **cypress/** → pruebas automatizadas con Cypress.
- **api-testing/** → pruebas de APIs.
- **bots/** → scripts de automatización adicionales (ejemplo: bot de ofertas de empleo).

## Cómo ejecutar las pruebas de Playwright
Dentro de la carpeta `PLAYWRIGHT/` encontrarás un README específico con instrucciones detalladas.

Ejemplo rápido:
```bash
npx playwright test tests/example-domain.spec.ts --project=chromium --headed

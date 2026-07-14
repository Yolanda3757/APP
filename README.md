# Pruebas con Playwright

Este proyecto contiene pruebas automatizadas usando [Playwright](https://playwright.dev/).

## Archivos de prueba
- `tests/example.spec.ts`: prueba de ejemplo incluida por defecto (sobre la página oficial de Playwright).
- `tests/example-domain.spec.ts`: prueba personalizada que navega a `example.com` y hace clic en **Learn more**.

## Cómo ejecutar las pruebas
Ejecutar todas las pruebas:
```bash
npx playwright test

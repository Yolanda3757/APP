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

🤖 Bot de Búsqueda de Vacantes Laborales (`botqa_excel.py`)

Este proyecto incluye una herramienta de automatización y web scraping desarrollada en **Python** con **Selenium** y **Pandas**. El bot realiza búsquedas automáticas de ofertas de empleo orientadas al perfil de aseguramiento de calidad (QA / Pruebas de Software) en el portal *El Empleo*, procesa la información relevante y genera un reporte descargable en Excel.

📊 Datos extraídos en el Excel
El archivo Excel generado recopila automáticamente las siguientes columnas por cada oferta encontrada:

- Cargo:/ Título o puesto de la vacante (ej. *Analista de pruebas*, *QA Tester funcional*, *Automatizador de pruebas*).
- Empresa / Moneda:** Información asociada a la vacante o entidad publicadora.
- **Enlace:/** URL directa a la publicación para postularse rápidamente.
* **Fecha:** Antigüedad de la publicación de la oferta (ej. *Hoy*, *Hace 3 días*, *Hace 1 semana*).
* **Fuente:** Dirección de origen del portal web.

---

### 🚀 Cómo ejecutar la herramienta

1. **Instalar dependencias necesarias:**
   ```bash
   pip install selenium pandas openpyxl

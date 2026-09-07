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
```

## 🤖 Bot de Búsqueda de Vacantes Laborales (`botqa_excel.py`)

Este proyecto incluye una herramienta de automatización y web scraping desarrollada en Python con Selenium y Pandas.
El bot realiza búsquedas automáticas de ofertas de empleo orientadas al perfil de aseguramiento de calidad (QA / Pruebas de Software) en el portal "El Empleo", procesa la información relevante y genera un reporte descargable en Excel.

## 📊 Datos extraídos en el Excel
El archivo Excel generado recopila automáticamente las siguientes columnas por cada oferta encontrada:

- Cargo:Título o puesto de la vacante (ej. "Analista de pruebas", "QA Tester funcional", "Automatizador de pruebas").
- Empresa:Información asociada a la vacante o entidad publicadora.
- Enlace: URL directa a la publicación para postularse rápidamente.
-Fecha: Antigüedad de la publicación de la oferta (ej. "Hoy", "Hace 3 días", "Hace 1 semana").
-Fuente:Dirección de origen del portal web.

## 🚀 Cómo ejecutar la herramienta

1. Instalar dependencias necesarias:
   ```bash
   pip install selenium pandas openpyxl
-📂 Evidencia de ejecución y resultado

A continuación, se adjuntan capturas de pantalla que muestran el resultado de la ejecución del bot:

## 1. Archivo generado en la carpeta local
En esta imagen se observa cómo el archivo `BotQA-Excel.xlsx` se guarda automáticamente en la carpeta del proyecto tras finalizar el scraping, junto con los scripts de Python.

<img width="921" height="290" alt="image" src="https://github.com/user-attachments/assets/ff9a0fbf-8896-4c71-89b4-b74f512c92ef" />


## 2. Estructura del Excel generado
Esta captura muestra la estructura interna del archivo Excel, detallando las columnas de Cargo, Empresa, Enlace, Fecha y Fuente con los datos extraídos de las vacantes encontradas.

<img width="921" height="364" alt="image" src="https://github.com/user-attachments/assets/2d7e2d39-5e26-4958-9197-afe23f322f69" />

## 📈 Generación de Gráficas Estadísticas (`graficas.py`)

El proyecto incluye un script adicional encargado de realizar un análisis visual de los datos recopilados por el bot.

## ⚠️ Requisito previo obligatorio
Para poder ejecutar la generación de gráficas, debe existir previamente el archivo Excel (`BotQA-Excel.xlsx`) generado por el script `botqa_excel.py`. Si el archivo no está presente en la carpeta, el script no podrá procesar los datos ni construir las métricas.

## 📊 Funcionalidad de las gráficas
El script `graficas.py` lee el reporte generado y procesa la información para representar de forma visual:
-Distribución de tipos de cargo según el perfil de QA/Pruebas.
-Frecuencia y antigüedad de la publicación de las ofertas.

## 🚀 Cómo generar las gráficas
1. Asegúrese de haber ejecutado primero el bot:
   ```powershell
   python botqa_excel.py


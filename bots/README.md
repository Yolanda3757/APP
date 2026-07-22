# Bot de Ofertas de Empleo

Este bot consulta ofertas en **elempleo.com** y genera un archivo Excel con los resultados.  
Además, incluye un script para visualizar gráficas de las ofertas.

## 📂 Archivos principales
- **botqa_excel.py** → realiza el scraping de ofertas y genera el Excel con los datos.
- **graficas.py** → lee el Excel y crea gráficas de distribución (por empresa, fecha y fuente).

## ⚙️ Instalación de dependencias
Antes de ejecutar los scripts, instala las librerías necesarias:
```bash
pip install pandas matplotlib seaborn openpyxl playwright


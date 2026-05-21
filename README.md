# 🚖 Análisis de Demanda y Movilidad de Taxis en NYC
### 🎓 Seminario de Ciencia de los Datos — Proyecto Final
**Institución Universitaria Pascual Bravo** **Facultad de Ingeniería** **Medellín, 2026**

---

## 👥 Integrantes
* **Eyder Fabian Leiton**
* **María Alejandra Arango**
* **Manuela Martínez**
* **Manuela Cardona**

**Docente:** Wilson Andrés Ramírez Rios  

---

## 🎯 Delimitación del Problema y Reducción de Alcance
Para cumplir con las directrices metodológicas de la asignatura y evitar un enfoque sobredimensionado (*"contexto magno"*), el equipo ha realizado una **reducción de alcance** estructurada. El proyecto se delimita formalmente bajo los siguientes parámetros:

* **Línea de Trabajo Principal:** Transporte y Logística.
* **Temática General:** Demanda de Taxis y Movilidad Urbana.
* **Subtema / Alcance Acotado:** Estudio de los factores espacio-temporales y la distribución del costo del servicio para la predicción analítica de la tarifa base (`fare`) mediante modelamiento supervisado de regresión.

---

## 📊 Estructura del Repositorio y Entregables

El proyecto se desarrolla siguiendo rigurosamente el ciclo de vida de la metodología **CRISP-DM** (*CRoss Industry Standard Process for Data Mining*), dividido en los siguientes hitos de entrega:

### 📑 Entregable 1: Análisis Exploratorio y Tratamiento de Datos
* **Código Fuente:** [Entregable1_Taxis.ipynb](./Entregable1_Taxis.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Leiton1214/NYC-Taxi-Demand-Analysis/blob/main/Entregable1_Taxis.ipynb)
* **Reporte Escrito (Normas APA):** [Entregable1_Taxis_APA.docx](./Entregable1_Taxis_APA.docx)
* **Fases CRISP-DM Cubiertas:** Comprensión de los Datos y Preparación de los Datos (Limpieza inicial).
* **Hitos Estadísticos Alcanzados:**
  * **Análisis Descriptivo:** Exploración de variables clave (`fare`, `distance`, `total`, `passengers`).
  * **Pruebas de Normalidad:** Aplicación de gráficos Q-Q Plots y contraste analítico mediante el **Test de Shapiro-Wilk** (muestreo controlado $n=5000$). Se concluyó que las variables numéricas presentan sesgo positivo y no paramétrico ($p \ll 0.05$).
  * **Análisis de Datos Ausentes:** Identificación de nulos concentrados en variables geográficas de destino (`dropoff_zone`, `dropoff_borough`). La **Prueba de Rachas (Runs Test)** determinó un patrón no aleatorio, clasificando la ausencia bajo el mecanismo **MAR** (*Missing At Random*).
  * **Tratamiento de Outliers:** Implementación de la técnica de **Capping (Winsorización)** utilizando los límites estadísticos estrictos del Rango Intercuartílico ($Q3 + 1.5 \times IQR$) en las variables económicas para no perder registros válidos.
  * **Diseño de Imputación:** Introducción controlada de un 15% de nulos artificiales sobre la variable `fare`. Se contrastó la imputación simple (Media) frente a la avanzada (**Regresión Lineal**, $R^2 = 0.87$), demostrando que el modelamiento supervisado preserva óptimamente la variabilidad del negocio.

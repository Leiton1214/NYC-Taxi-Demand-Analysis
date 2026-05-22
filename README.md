# 🚖 NYC Taxi Demand Analysis — Demanda de Taxis y Movilidad Urbana
### Seminario de Ciencia de los Datos
**Tema 18: Demanda de Taxis / Movilidad Urbana**  
**Dataset:** NYC Yellow Taxi — `seaborn.load_dataset('taxis')`

[![Abrir E1 en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Leiton1214/NYC-Taxi-Demand-Analysis/blob/main/Entregable1_DemandaTaxis.ipynb)
[![Abrir E2 en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Leiton1214/NYC-Taxi-Demand-Analysis/blob/main/Entregable2_DemandaTaxis.ipynb)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nyc-taxi-demand-analysis.streamlit.app)
🔗 **[https://nyc-taxi-demand-analysis.streamlit.app](https://nyc-taxi-demand-analysis.streamlit.app)**

---

## 📋 Descripción del Proyecto

Este repositorio contiene el proyecto final del curso **Seminario de Ciencia de los Datos**, desarrollado en dos entregas bajo la metodología **CRISP-DM** (Cross Industry Standard Process for Data Mining).

El caso de estudio analiza la **demanda de taxis y la movilidad urbana en la ciudad de Nueva York**, utilizando el dataset NYC Yellow Taxi. El dataset presenta retos representativos de un problema real de ciencia de datos: alta dimensionalidad, valores nulos en variables geográficas de destino y outliers significativos en variables económicas como la tarifa y la distancia recorrida.

El proyecto cubre el ciclo completo de un análisis de datos: desde la carga y limpieza del dataset, pasando por la reducción de dimensionalidad y la selección de características, hasta el entrenamiento, comparación y despliegue de modelos supervisados de clasificación.

---

## 🗂️ Estructura del Repositorio

```
📦 NYC-Taxi-Demand-Analysis/
│
├── 📓 Entregable1_DemandaTaxis.ipynb       # Cuadernillo Entregable 1 (Colab)
├── 📄 Entregable1_DemandaTaxis_APA.docx    # Informe APA Entregable 1
│
├── 📓 Entregable2_DemandaTaxis.ipynb       # Cuadernillo Entregable 2 (Colab)
├── 📄 Entregable2_DemandaTaxis_APA.docx    # Informe APA Entregable 2
│
├── 🐍 app.py                               # App de despliegue (Streamlit)
├── 📋 requirements.txt                     # Dependencias del proyecto
└── 📖 README.md                            # Este archivo
```

---

## 📊 Dataset

| Atributo | Detalle |
|----------|---------|
| **Nombre** | NYC Yellow Taxi (`taxis`) |
| **Fuente** | Seaborn — `sns.load_dataset('taxis')` |
| **Registros** | 6,433 filas |
| **Variables** | 14 columnas (numéricas, categóricas y temporales) |
| **Problemas de calidad** | Nulos en `dropoff_zone` y `dropoff_borough`; outliers en `fare`, `distance` y `total` |

### Variables del Dataset

| Variable | Tipo | Descripción | Observación |
|----------|------|-------------|-------------|
| `pickup` | datetime | Fecha y hora de recogida | — |
| `dropoff` | datetime | Fecha y hora de llegada | — |
| `passengers` | int | Número de pasajeros | — |
| `distance` | float | Distancia del viaje (millas) | ⚠️ Outliers |
| `fare` | float | Tarifa base (USD) | ⚠️ Outliers |
| `tip` | float | Propina (USD) | ⚠️ Outliers |
| `tolls` | float | Peajes (USD) | — |
| `total` | float | Monto total (USD) | ⚠️ Outliers |
| `color` | str | Color del taxi (yellow / green) | — |
| `payment` | str | Método de pago | — |
| `pickup_zone` | str | Zona de recogida | — |
| `dropoff_zone` | str | Zona de destino | ⚠️ Nulos |
| `pickup_borough` | str | Municipio de recogida | — |
| `dropoff_borough` | str | Municipio de destino | ⚠️ Nulos |

---

## 📦 Entregable No. 1 — Análisis Exploratorio y Tratamiento de Datos

> **Fecha de entrega:** 24 de mayo de 2025 · **Peso:** 30%

### Tópicos

| # | Tópico | Técnicas Aplicadas |
|---|--------|--------------------|
| **I** | Análisis Descriptivo y de Calidad | Estadísticos descriptivos, diccionario de variables, coeficiente de variación, asimetría y curtosis |
| **II** | Evaluación de la Calidad | Histogramas con KDE, Q-Q Plots, Prueba de Shapiro-Wilk (α = 0.05) |
| **III** | Detección y Tratamiento de Ausentes | Librería `missingno`, Prueba de Rachas (implementación manual) |
| **IV** | Tratamiento de Outliers | Boxplots, Método IQR, Capping / Winsorización con comparativa antes-después |
| **V** | Imputación Comparativa | Imputación Simple (Media) vs. Imputación por Regresión Lineal, cálculo de MAE |

### 🔍 Principales Hallazgos

- **Normalidad:** Ninguna variable numérica sigue distribución normal (Shapiro-Wilk, p < 0.05 en todas). Las distribuciones presentan asimetría positiva, especialmente en `fare`, `distance` y `tip`.
- **Datos ausentes:** Las variables `dropoff_zone` y `dropoff_borough` presentan ~3% de nulos. La Prueba de Rachas indica un patrón no completamente aleatorio (MAR), posiblemente asociado a rutas o condiciones operativas específicas.
- **Outliers:** Se detectaron outliers significativos en `fare` (5.5%), `distance` (4.8%) y `total` (5.1%) mediante el método IQR. Se optó por **Capping (Winsorización)** para preservar el volumen de datos, dado que muchos valores extremos corresponden a viajes legítimos hacia aeropuertos.
- **Imputación:** La **Regresión Lineal** superó a la imputación por media en precisión (MAE ≈ 1.12 vs. 2.34), aprovechando la relación entre `fare` y `distance`.

---

## 📦 Entregable No. 2 — Reducción de Dimensionalidad y Conclusiones

> **Fecha de entrega:** 29 de mayo de 2025 · **Peso:** 20%

### Tópicos

| # | Tópico | Técnicas Aplicadas |
|---|--------|--------------------|
| **I–V** | Preprocesamiento consolidado | Pipeline completo del Entregable 1 |
| **VI** | PCA + Correlación de Pearson | Matriz de correlación, Scree Plot, Biplot, Loadings |
| **VII** | Selección de Características | Método de filtro F-Score ANOVA (`SelectKBest`) |
| **VIII** | Implementación de Modelos | Regresión Logística + Árbol de Decisión, CV-5, métricas completas |
| **IX** | Conclusiones y Reflexiones | Impacto del preprocesamiento en el rendimiento de los modelos |

### Variable Objetivo
`tip_alto` — variable binaria: **1** si la propina supera la mediana de `tip`, **0** en caso contrario.

### Top 5 Características Seleccionadas (F-Score ANOVA)

| Ranking | Variable | Interpretación |
|---------|----------|----------------|
| 1° | `payment_enc` | Método de pago: principal predictor de propina |
| 2° | `fare` | Tarifa base correlacionada con el monto de propina |
| 3° | `total` | Monto total refleja el nivel de gasto del pasajero |
| 4° | `distance` | Viajes más largos tienden a generar mayor propina |
| 5° | `dropoff_borough_enc` | Zona de destino influye en el comportamiento del pasajero |

### Comparativa de Modelos

| Modelo | Accuracy Test | CV-5 |
|--------|:---:|:---:|
| Regresión Logística | Ver Notebook | Ver Notebook |
| Árbol de Decisión (max_depth=5) | Ver Notebook | Ver Notebook |

---

## 🚀 Despliegue — Valor Adicional

La aplicación interactiva permite predecir en tiempo real si un viaje generará propina alta o baja, con ambos modelos disponibles para comparación.

### ▶️ Probar la App Online
🔗 **[https://leiton1214-nyc-taxi-demand-analysis.streamlit.app](https://leiton1214-nyc-taxi-demand-analysis.streamlit.app)**

### ▶️ Ejecutar Localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/Leiton1214/NYC-Taxi-Demand-Analysis.git
cd NYC-Taxi-Demand-Analysis

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la app
streamlit run app.py
```

---

## ⚙️ Requisitos e Instalación

### Ejecutar los Notebooks en Google Colab (recomendado)

1. Haz clic en el badge **"Abrir en Colab"** de cada entregable al inicio de este README
2. Ejecuta la primera celda de instalación:
```python
!pip install seaborn scipy missingno --quiet
```
3. Ejecuta las celdas en orden de arriba hacia abajo

### Ejecutar en Local

```bash
git clone https://github.com/Leiton1214/NYC-Taxi-Demand-Analysis.git
cd NYC-Taxi-Demand-Analysis
pip install -r requirements.txt
jupyter notebook
```

### Dependencias

```
pandas
numpy
matplotlib
seaborn
scipy
missingno
scikit-learn
streamlit
```

---

## 👥 Integrantes del Grupo

| Nombre |
|--------|
| Maria Alejandra Arango |
| Manuela Martinez |
| Manuela Cardona |
| Alex Gomez |
| Eyder Fabian Leiton |

---

## 👨‍🏫 Información del Curso

| Campo | Detalle |
|-------|---------|
| **Curso** | Seminario de Ciencia de los Datos |
| **Docente** | Wilson Andres Ramirez Rios |
| **Metodología** | CRISP-DM |
| **Repositorio** | [github.com/Leiton1214/NYC-Taxi-Demand-Analysis](https://github.com/Leiton1214/NYC-Taxi-Demand-Analysis) |

---

## 📚 Referencias

- Bishop, C. M. (2006). *Pattern recognition and machine learning*. Springer.
- Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Jolliffe, I. T. (2002). *Principal component analysis* (2nd ed.). Springer.
- Pedregosa, F. et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- Shapiro, S. S., & Wilk, M. B. (1965). An analysis of variance test for normality. *Biometrika, 52*(3-4), 591–611.
- Streamlit Inc. (2023). *Streamlit: The fastest way to build data apps*. https://streamlit.io
- Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley.
- van Buuren, S. (2018). *Flexible imputation of missing data* (2nd ed.). Chapman and Hall/CRC.
- Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021

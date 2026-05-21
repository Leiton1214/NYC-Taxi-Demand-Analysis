# 🚖 Entregable No. 1 — Análisis Exploratorio y Tratamiento de Datos
### Seminario de Ciencia de los Datos
**Tema 18: Demanda de Taxis / Movilidad Urbana**
**Dataset:** NYC Yellow Taxi — `seaborn.load_dataset('taxis')`

---

## 📋 Descripción del Proyecto

Este repositorio contiene el primer entregable del proyecto final del curso **Seminario de Ciencia de los Datos**, correspondiente a la fase de **Análisis Exploratorio y Tratamiento de Datos** bajo la metodología **CRISP-DM**.

El caso de estudio analiza la demanda de taxis y movilidad urbana en la ciudad de Nueva York, utilizando el dataset NYC Yellow Taxi. Este dataset presenta los retos propios de un problema real de ciencia de datos: alta dimensionalidad, valores nulos en variables geográficas de destino y outliers significativos en variables económicas como la tarifa y la distancia recorrida.

---

## 🗂️ Estructura del Repositorio

```
📦 Entregable_1_DemandaTaxis/
├── 📓 Entregable1_DemandaTaxis.ipynb     # Cuadernillo principal (Google Colab)
├── 📄 Entregable1_DemandaTaxis_APA.docx  # Informe escrito en normas APA
└── 📖 README.md                          # Este archivo
```

---

## 🧪 Contenido del Notebook

El cuadernillo está organizado en 5 tópicos según los lineamientos del curso:

| # | Tópico | Técnicas Aplicadas |
|---|--------|--------------------|
| **I** | Análisis Descriptivo y de Calidad | Estadísticos descriptivos, diccionario de variables, coeficiente de variación, asimetría y curtosis |
| **II** | Evaluación de la Calidad | Histogramas con KDE, Q-Q Plots, Prueba de Shapiro-Wilk (α = 0.05) |
| **III** | Detección y Tratamiento de Ausentes | Librería `missingno`, Prueba de Rachas (implementación manual) |
| **IV** | Tratamiento de Outliers | Boxplots, Método IQR, Capping / Winsorización con comparativa antes-después |
| **V** | Imputación Comparativa | Imputación Simple (Media) vs. Imputación por Regresión Lineal, cálculo de MAE |

---

## 📊 Dataset

| Atributo | Detalle |
|----------|---------|
| **Nombre** | NYC Yellow Taxi (`taxis`) |
| **Fuente** | Seaborn — `sns.load_dataset('taxis')` |
| **Registros** | 6,433 filas |
| **Variables** | 14 columnas (numéricas, categóricas y temporales) |
| **Problemas de calidad** | Nulos en `dropoff_zone` y `dropoff_borough`; outliers en `fare`, `distance` y `total` |

### Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `pickup` | datetime | Fecha y hora de recogida |
| `dropoff` | datetime | Fecha y hora de llegada |
| `passengers` | int | Número de pasajeros |
| `distance` | float | Distancia del viaje (millas) |
| `fare` | float | Tarifa base (USD) |
| `tip` | float | Propina (USD) |
| `total` | float | Monto total (USD) |
| `color` | str | Color del taxi (yellow / green) |
| `payment` | str | Método de pago |
| `dropoff_zone` | str | Zona de destino ⚠️ *contiene nulos* |
| `dropoff_borough` | str | Municipio de destino ⚠️ *contiene nulos* |

---

## ⚙️ Requisitos e Instalación

### Ejecutar en Google Colab (recomendado)

1. Abre [Google Colab](https://colab.research.google.com/)
2. Ve a **Archivo → Subir notebook** y carga `Entregable1_DemandaTaxis.ipynb`
3. Ejecuta la primera celda de instalación:

```python
!pip install seaborn scipy missingno --quiet
```

4. Ejecuta las celdas en orden de arriba hacia abajo.

### Ejecutar en local

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

# Instalar dependencias
pip install pandas numpy matplotlib seaborn scipy missingno scikit-learn

# Abrir el notebook
jupyter notebook Entregable1_DemandaTaxis.ipynb
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
```

---

## 🔍 Principales Hallazgos

- **Normalidad:** Ninguna variable numérica sigue distribución normal (Shapiro-Wilk, p < 0.05 en todas). Las distribuciones presentan asimetría positiva, especialmente en `fare`, `distance` y `tip`.

- **Datos ausentes:** Las variables `dropoff_zone` y `dropoff_borough` presentan ~3% de nulos. La Prueba de Rachas indica un patrón no completamente aleatorio (MAR), posiblemente asociado a rutas o condiciones operativas específicas.

- **Outliers:** Se detectaron outliers significativos en `fare` (5.5%), `distance` (4.8%) y `total` (5.1%) mediante el método IQR. Se optó por **Capping (Winsorización)** para preservar el volumen de datos, dado que muchos valores extremos corresponden a viajes legítimos hacia aeropuertos.

- **Imputación:** La **Regresión Lineal** superó a la imputación por media en precisión (MAE ≈ 1.12 vs. 2.34), aprovechando la relación entre `fare` y `distance`.

---

## 📁 Entregables

| Archivo | Descripción |
|---------|-------------|
| `Entregable1_DemandaTaxis.ipynb` | Notebook ejecutable con todo el análisis, visualizaciones y código comentado |
| `Entregable1_DemandaTaxis_APA.docx` | Informe académico con portada, resumen, introducción, análisis por tópico, conclusiones y referencias en normas APA 7ª edición |

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
| **Fecha de entrega** | 24 de mayo de 2025 |
| **Metodología** | CRISP-DM |

---

## 📚 Referencias

- Chapman, P. et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS Inc.
- Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley.
- Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021
- van Buuren, S. (2018). *Flexible imputation of missing data* (2nd ed.). Chapman and Hall/CRC.
- Shapiro, S. S., & Wilk, M. B. (1965). An analysis of variance test for normality. *Biometrika, 52*(3-4), 591–611.

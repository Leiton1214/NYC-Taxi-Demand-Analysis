"""
🚖 NYC Taxi Demand Analysis — Predictor de Propina
Seminario de Ciencia de los Datos — Entregable No. 2
Despliegue con Streamlit
"""

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ── Configuración de la página ────────────────────────────────────────────────
st.set_page_config(
    page_title="🚖 Predictor de Propina — NYC Taxis",
    page_icon="🚖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ── CSS personalizado ─────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2rem; font-weight: 800; color: #1F3864;
        text-align: center; margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1rem; color: #555; text-align: center; margin-bottom: 1.5rem;
    }
    .result-box-high {
        background: #d4edda; border-left: 6px solid #28a745;
        padding: 1rem 1.5rem; border-radius: 8px; margin-top: 1rem;
    }
    .result-box-low {
        background: #fff3cd; border-left: 6px solid #ffc107;
        padding: 1rem 1.5rem; border-radius: 8px; margin-top: 1rem;
    }
    .metric-card {
        background: #f0f4f8; border-radius: 8px;
        padding: 0.8rem; text-align: center; margin: 0.3rem;
    }
    .footer-text {
        font-size: 0.78rem; color: #888; text-align: center; margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Pipeline de entrenamiento (se ejecuta una vez con @st.cache_resource) ────
@st.cache_resource
def cargar_modelos():
    """Carga el dataset, aplica el pipeline completo y entrena los dos modelos."""
    df = sns.load_dataset('taxis')

    # Tratamiento de nulos
    for col in ['dropoff_zone', 'dropoff_borough']:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Capping IQR
    for col in ['fare', 'distance', 'total', 'tip']:
        Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
        IQR = Q3 - Q1
        df[col] = df[col].clip(lower=Q1 - 1.5*IQR, upper=Q3 + 1.5*IQR)

    # Encoding
    le = LabelEncoder()
    cat_cols = ['color', 'payment', 'pickup_zone', 'dropoff_zone',
                'pickup_borough', 'dropoff_borough']
    for col in cat_cols:
        df[col + '_enc'] = le.fit_transform(df[col].astype(str))

    # Variable objetivo
    df['tip_alto'] = (df['tip'] > df['tip'].median()).astype(int)

    # Top 5 features (definidas en el análisis)
    top5 = ['payment_enc', 'fare', 'total', 'distance', 'dropoff_borough_enc']

    X = df[top5]
    y = df['tip_alto']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s  = scaler.transform(X_test)

    # Entrenar modelos
    rl = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
    rl.fit(X_train_s, y_train)

    dt = DecisionTreeClassifier(max_depth=5, random_state=42, class_weight='balanced')
    dt.fit(X_train_s, y_train)

    # Métricas
    from sklearn.metrics import accuracy_score
    acc_rl = accuracy_score(y_test, rl.predict(X_test_s))
    acc_dt = accuracy_score(y_test, dt.predict(X_test_s))

    # Encoders para la app
    le_payment = LabelEncoder().fit(df['payment'].astype(str))
    le_borough = LabelEncoder().fit(df['dropoff_borough'].astype(str))

    meta = {
        'scaler':       scaler,
        'rl':           rl,
        'dt':           dt,
        'acc_rl':       acc_rl,
        'acc_dt':       acc_dt,
        'le_payment':   le_payment,
        'le_borough':   le_borough,
        'payment_cats': sorted(df['payment'].dropna().unique().tolist()),
        'borough_cats': sorted(df['dropoff_borough'].dropna().unique().tolist()),
        'fare_range':   (float(df['fare'].min()),   float(df['fare'].max())),
        'total_range':  (float(df['total'].min()),  float(df['total'].max())),
        'dist_range':   (float(df['distance'].min()), float(df['distance'].max())),
    }
    return meta


# ── Encabezado ────────────────────────────────────────────────────────────────
st.markdown('<p class="main-title">🚖 Predictor de Propina</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">NYC Yellow Taxi · Seminario de Ciencia de los Datos · Entregable No. 2</p>',
            unsafe_allow_html=True)
st.divider()

with st.spinner('Cargando modelos... esto toma unos segundos la primera vez.'):
    meta = cargar_modelos()

# ── Sidebar — información del proyecto ───────────────────────────────────────
with st.sidebar:
    st.header("📋 Acerca del Proyecto")
    st.markdown("""
**Curso:** Seminario de Ciencia de los Datos  
**Dataset:** NYC Yellow Taxi (`seaborn`)  
**Variable objetivo:** `tip_alto` — propina por encima de la mediana  
**Metodología:** CRISP-DM  

---
**Modelos entrenados:**
- 🔵 Regresión Logística
- 🟢 Árbol de Decisión (max_depth=5)

**Top 5 características (F-Score ANOVA):**
1. `payment_enc`
2. `fare`
3. `total`
4. `distance`
5. `dropoff_borough_enc`
""")
    st.divider()
    st.markdown("**🔗 Repositorio GitHub:**")
    st.markdown("[Leiton1214/NYC-Taxi-Demand-Analysis](https://github.com/Leiton1214/NYC-Taxi-Demand-Analysis)")
    st.divider()

    col1, col2 = st.columns(2)
    col1.metric("Accuracy RL",  f"{meta['acc_rl']*100:.1f}%")
    col2.metric("Accuracy DT",  f"{meta['acc_dt']*100:.1f}%")

# ── Selección de modelo ───────────────────────────────────────────────────────
st.subheader("⚙️ Configuración")
modelo_sel = st.radio(
    "Selecciona el modelo de predicción:",
    ["🔵 Regresión Logística", "🟢 Árbol de Decisión"],
    horizontal=True
)

# ── Formulario de entrada ─────────────────────────────────────────────────────
st.subheader("📝 Características del Viaje")

col_a, col_b = st.columns(2)

with col_a:
    payment = st.selectbox(
        "💳 Método de pago",
        options=meta['payment_cats'],
        help="El método de pago es el predictor más importante del modelo."
    )
    fare = st.slider(
        "💵 Tarifa base (USD)",
        min_value=meta['fare_range'][0],
        max_value=meta['fare_range'][1],
        value=float(np.mean(meta['fare_range'])),
        step=0.5,
        format="$%.2f"
    )
    total = st.slider(
        "💰 Monto total (USD)",
        min_value=meta['total_range'][0],
        max_value=meta['total_range'][1],
        value=float(np.mean(meta['total_range'])),
        step=0.5,
        format="$%.2f"
    )

with col_b:
    distance = st.slider(
        "📍 Distancia (millas)",
        min_value=meta['dist_range'][0],
        max_value=meta['dist_range'][1],
        value=float(np.mean(meta['dist_range'])),
        step=0.1,
        format="%.1f mi"
    )
    borough = st.selectbox(
        "🗺️ Municipio de destino",
        options=meta['borough_cats'],
        help="Zona geográfica de destino del viaje."
    )

# ── Predicción ────────────────────────────────────────────────────────────────
st.divider()

if st.button("🚀 Predecir Propina", use_container_width=True, type="primary"):

    # Encode inputs
    payment_enc = meta['le_payment'].transform([payment])[0]
    borough_enc = meta['le_borough'].transform([borough])[0]

    X_input = np.array([[payment_enc, fare, total, distance, borough_enc]])
    X_input_s = meta['scaler'].transform(X_input)

    # Seleccionar modelo
    modelo = meta['rl'] if "Logística" in modelo_sel else meta['dt']
    nombre_modelo = "Regresión Logística" if "Logística" in modelo_sel else "Árbol de Decisión"

    pred  = modelo.predict(X_input_s)[0]
    proba = modelo.predict_proba(X_input_s)[0]

    # Resultado
    if pred == 1:
        st.markdown(f"""
        <div class="result-box-high">
            <h3>✅ Propina ALTA esperada</h3>
            <p>El modelo <b>{nombre_modelo}</b> predice que este viaje generará una propina <b>por encima de la mediana</b>.</p>
            <p>Probabilidad: <b>{proba[1]*100:.1f}%</b> propina alta · {proba[0]*100:.1f}% propina baja</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-box-low">
            <h3>⚠️ Propina BAJA esperada</h3>
            <p>El modelo <b>{nombre_modelo}</b> predice que este viaje generará una propina <b>por debajo de la mediana</b>.</p>
            <p>Probabilidad: <b>{proba[0]*100:.1f}%</b> propina baja · {proba[1]*100:.1f}% propina alta</p>
        </div>
        """, unsafe_allow_html=True)

    # Gráfico de probabilidades
    st.markdown("#### 📊 Distribución de Probabilidades")
    prob_df = pd.DataFrame({
        'Clase':        ['Propina Baja', 'Propina Alta'],
        'Probabilidad': [proba[0], proba[1]]
    })
    st.bar_chart(prob_df.set_index('Clase'), color=['#ffc107'] if pred == 0 else ['#28a745'])

    # Detalle del input
    with st.expander("🔍 Ver detalle del input procesado"):
        st.dataframe(pd.DataFrame({
            'Variable':   ['payment_enc', 'fare', 'total', 'distance', 'dropoff_borough_enc'],
            'Valor raw':  [payment, f'${fare:.2f}', f'${total:.2f}', f'{distance:.1f} mi', borough],
            'Valor enc.': [payment_enc, fare, total, distance, borough_enc],
            'Escalado':   X_input_s[0].round(4)
        }), use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<p class="footer-text">
Seminario de Ciencia de los Datos · Entregable No. 2 · Tema 18: Demanda de Taxis / Movilidad Urbana<br>
Dataset: NYC Yellow Taxi (Seaborn) · Metodología: CRISP-DM · 
<a href="https://github.com/Leiton1214/NYC-Taxi-Demand-Analysis" target="_blank">GitHub</a>
</p>
""", unsafe_allow_html=True)



import streamlit as st

st.title("Calculadora de puntaje MPNP")

# Enlace oficial
st.markdown(
    "Fuente y documentación: [Expression of Interest (EOI)](https://immigratemanitoba.com/immigrate/apply/eoi/)",
    unsafe_allow_html=True
)

st.header("1. Idioma principal")
st.badge("Máximo 125 puntos")

col11, col12 = st.columns (2)
col13, col14 = st.columns (2)

with col11: 
    # Selección de nivel CLB para cada habilidad del idioma principal
    clb_speaking = st.selectbox("¿Cuál es tu nivel en Speaking?", [
        "Menos de CLB 4 (0 pts)",
        "CLB 4 (12 pts)",
        "CLB 5 (17 pts)",
        "CLB 6 (20 pts)",
        "CLB 7 (22 pts)",
        "CLB 8 o más (25 pts)"
    ], index=None, placeholder="Seleccione una opción...")

with col12:
    clb_reading = st.selectbox("¿Cuál es tu nivel en Reading?", [
        "Menos de CLB 4 (0 pts)",
        "CLB 4 (12 pts)",
        "CLB 5 (17 pts)",
        "CLB 6 (20 pts)",
        "CLB 7 (22 pts)",
        "CLB 8 o más (25 pts)"
    ], index=None, placeholder="Seleccione una opción...")

with col13:
    clb_listening = st.selectbox("¿Cuál es tu nivel en Listening?", [
        "Menos de CLB 4 (0 pts)",
        "CLB 4 (12 pts)",
        "CLB 5 (17 pts)",
        "CLB 6 (20 pts)",
        "CLB 7 (22 pts)",
        "CLB 8 o más (25 pts)"
    ], index=None, placeholder="Seleccione una opción...")

with col14:
    clb_writing = st.selectbox("¿Cuál es tu nivel en Writing?", [
        "Menos de CLB 4 (0 pts)",
        "CLB 4 (12 pts)",
        "CLB 5 (17 pts)",
        "CLB 6 (20 pts)",
        "CLB 7 (22 pts)",
        "CLB 8 o más (25 pts)"
    ], index=None, placeholder="Seleccione una opción...")

puntos_por_clb = {
    "CLB 8 o más (25 pts)": 25,
    "CLB 7 (22 pts)": 22,
    "CLB 6 (20 pts)": 20,
    "CLB 5 (17 pts)": 17,
    "CLB 4 (12 pts)": 12,
    "Menos de CLB 4 (0 pts)": 0
}

if clb_speaking != None:
    pts_speaking = puntos_por_clb[clb_speaking]
else:
    pts_speaking = 0

if clb_reading != None:
    pts_reading = puntos_por_clb[clb_reading]
else:
    pts_reading = 0

if clb_listening != None:
    pts_listening = puntos_por_clb[clb_listening]
else:
    pts_listening = 0

if clb_writing != None:
    pts_writing = puntos_por_clb[clb_writing]
else:
    pts_writing = 0

# Preguntar por segundo idioma justo después
segundo_idioma = st.radio("¿Tienes un segundo idioma?", ("No", "Sí"))

pts_segundo_idioma = 0
if segundo_idioma == "Sí":
    clb_segundo = st.selectbox("¿Cuál es tu nivel CLB global del segundo idioma?", [
        "CLB 5 o más (25 pts)",
        "Menos de CLB 5 (0 pts)"
    ])
    if clb_segundo == "CLB 5 o más (25 pts)":
        pts_segundo_idioma = 25
    else:
        pts_segundo_idioma = 0

# Sumar todos los puntos
puntos_totales_idioma = pts_speaking + pts_reading + pts_listening + pts_writing + pts_segundo_idioma

st.badge(f"Puntaje total de Idioma: {puntos_totales_idioma} puntos", icon=":material/check:", color="green")

st.divider()

# 2. Edad
st.header("2. Edad")
st.badge("Máximo 75 puntos")
edad = st.selectbox("¿Qué edad tienes?", [
    "18 (20 pts)",
    "19 (30 pts)",
    "20 (40 pts)",
    "21 a 45 (75 pts)",
    "46 (40 pts)",
    "47 (30 pts)",
    "48 (20 pts)",
    "49 (10 pts)",
    "Más de 50 (0 pts)"
], index=None, placeholder="Seleccione una opción...")

puntos_edad = {
    "18 (20 pts)": 20,
    "19 (30 pts)": 30,
    "20 (40 pts)": 40,
    "21 a 45 (75 pts)": 75,
    "46 (40 pts)": 40,
    "47 (30 pts)": 30,
    "48 (20 pts)": 20,
    "49 (10 pts)": 10,
    "Más de 50 (0 pts)": 0
}
if edad != None:
    pts_edad = puntos_edad[edad]
else:
    pts_edad = 0

st.badge(f"Puntaje total de Edad: {pts_edad} puntos", icon=":material/check:", color="green")

st.divider()

# 3. Experiencia laboral
st.header("3. Experiencia laboral en los últimos 5 años")
st.badge("Máximo 175 puntos")

col31, col32 = st.columns(2)

with col31:
    experiencia = st.selectbox("¿Cuántos años de experiencia tienes?", [
        "Menos de un año (0 pts)",
        "1 año (40 pts)",
        "2 años (50 pts)",
        "3 años (60 pts)",
        "4 años o más (75 pts)",
    ], index=None, placeholder="Seleccione una opción...")

puntos_experiencia = {
    "Menos de un año (0 pts)": 0,
    "1 año (40 pts)": 40,
    "2 años (50 pts)": 50,
    "3 años (60 pts)": 60,
    "4 años o más (75 pts)": 75,
}

with col32:
    licenciamiento = st.checkbox("Reconocido por el organismo de licenciamiento provincial (100 pts)")
    score_regional = 100 if licenciamiento else 0

if experiencia != None:
    score_experiencia = puntos_experiencia[experiencia] + score_regional
else:
    score_experiencia = 0
    
st.badge(f"Puntaje total de Experiencia laboral: {score_experiencia} puntos", icon=":material/check:", color="green")


st.divider()

# 4. Educación
st.header("4. Nivel de educación")
st.badge("Máximo 125 puntos")

educacion = st.selectbox("Selecciona tu nivel educativo", [
    "Maestría o doctorado (125 pts)",
    "Dos programas postsecundarios de al menos dos años cada uno (115 pts)",
    "Un programa postsecundario de tres años o más (110 pts)",
    "Un programa postsecundario de dos años (100 pts)",
    "Un programa postsecundario de un año (70 pts)",
    "Certificado en oficios (Trade certificate) (70 pts)",
    "Sin educación postsecundaria formal (0 pts)"
    
], index=None, placeholder="Seleccione una opción...")
puntos_educacion = {
    "Maestría o doctorado (125 pts)": 125,
    "Dos programas postsecundarios de al menos dos años cada uno (115 pts)": 115,
    "Un programa postsecundario de tres años o más (110 pts)": 110,
    "Un programa postsecundario de dos años (100 pts)": 100,
    "Un programa postsecundario de un año (70 pts)": 70,
    "Certificado en oficios (Trade certificate) (70 pts)": 70,
    "Sin educación postsecundaria formal (0 pts)": 0
}

if educacion != None:
    score_educacion = puntos_educacion[educacion]
else:
    score_educacion = 0

st.badge(f"Puntaje total de Educación: {score_educacion} puntos", icon=":material/check:", color="green")

st.divider()

st.header("5. Adaptabilidad")
st.badge("Máximo 500 puntos")

# --- 5.1 Conexión con Manitoba (máximo 200 pts) ---
st.subheader("5.1 Conexión con Manitoba (máx. 200 pts)")
st.badge("Máximo 200 puntos", color="gray")

# Diccionario de opciones y sus puntos
opciones_conexion_mb = {
    "Familiar cercano en Manitoba": 200,
    "Experiencia laboral previa en Manitoba": 100,
    "Estudios postsecundarios en Manitoba (2 años o más)": 100,
    "Estudios postsecundarios en Manitoba (1 año)": 50,
    "Amigo cercano o familiar lejano en Manitoba": 50,
}

score_conexion_mb = 0
for label, points in opciones_conexion_mb.items():
    if st.checkbox(f"{label} ({points} pts)", key=f"conexion_{label}"):
        score_conexion_mb += points # Suma los puntos si el checkbox está marcado

# Asegurarse de que el puntaje no exceda el máximo de 200 para esta sección
if score_conexion_mb > 200:
    score_conexion_mb = 200

st.badge(f"{score_conexion_mb} puntos", color="orange")


# --- 5.2 Demanda de Manitoba (máximo 500 pts) ---
st.subheader("5.2 Demanda de Manitoba")
st.badge("Máximo 500 puntos", color="gray")

# Diccionario de opciones y sus puntos
opciones_manitoba_demand = {
    "Empleo actual en Manitoba por 6 meses o más + oferta a largo plazo": 500,
    "Invitación para aplicar bajo una Iniciativa Estratégica": 500,
}

score_demand = 0
# Crear checkboxes y calcular el puntaje de demanda
# Se toma el puntaje más alto si se marcan múltiples
for label, points in opciones_manitoba_demand.items():
    if st.checkbox(f"{label} ({points} pts)", key=f"demanda_{label}"):
        score_demand += points

if score_demand > 500:
    score_demand = 500

st.badge(f"{score_demand} puntos", color="orange")


# --- 5.3 Desarrollo regional (máximo 50 pts) ---
st.subheader("5.3 Desarrollo regional")
st.badge("Máximo 50 puntos", color="gray")


fuera_de_wpg = st.checkbox("¿Planeas establecerte fuera de Winnipeg? (50 pts)", key="regional_dev")
score_regional = 50 if fuera_de_wpg else 0

st.badge(f"{score_regional} puntos", color="orange")


# --- Puntaje total de adaptabilidad ---
score_adaptabilidad = score_conexion_mb + score_demand + score_regional

# Asegurarse de que el puntaje no exceda el máximo de 500
if score_adaptabilidad > 500: # Cambiado de >= 500 a > 500 para un límite estricto
    score_adaptabilidad = 500

st.badge(f"Puntaje total de Adaptabilidad: {score_adaptabilidad} puntos", icon=":material/check:", color="green")

st.divider()

# 6. Evaluación de Riesgo (hasta -200 pts)
st.header("6. Evaluación de riesgo (Risk Assessment)")
st.badge("Máximo -200 puntos")

puntos_riesgo_total = 0

st.write("Selecciona si alguno de estos factores de riesgo aplica a tu situación:")

riesgo_trabajo_otra_provincia = st.checkbox("Has tenido experiencia laboral en otra provincia de Canadá")
if riesgo_trabajo_otra_provincia:
    puntos_riesgo_total -= 100

riesgo_estudio_otra_provincia = st.checkbox("Has estudiado en otra provincia de Canadá")
if riesgo_estudio_otra_provincia:
    puntos_riesgo_total -= 100

riesgo_familiar_otra_provincia = st.checkbox("Tienes un familiar cercano en otra provincia de Canadá y ningún familiar cercano en Manitoba")
if riesgo_familiar_otra_provincia:
    puntos_riesgo_total -= 0

riesgo_solicitud_otra_provincia = st.checkbox("Has presentado una solicitud de inmigración previa a otra provincia de Canadá")
if riesgo_solicitud_otra_provincia:
    puntos_riesgo_total -= 0

st.badge(f"Puntaje total de Evaluación de riesgo: {puntos_riesgo_total} puntos", icon=":material/check:", color="red")

st.divider()

# Puntaje total

score_col1, score_col2, score_col3 = st.columns(3)

general = 861
postsecondary = 844

with score_col1:
    st.subheader("🎯 Tu puntaje total es:")
    puntaje_total = puntos_totales_idioma + pts_edad + score_experiencia + score_educacion + score_adaptabilidad + puntos_riesgo_total
    st.metric(label="-", value=puntaje_total)
    
with score_col2:
    st.caption("Último puntaje general")
    st.metric("2025-03-06 - Draw 240", general)
    
with score_col3:
    st.caption("Último puntaje Completed post-secondary study in Manitoba")
    st.metric("2025-03-21 - Draw 241", postsecondary)

st.divider()

st.markdown(
    "Expression of Interest (EOI) Draws: [Enlace](https://immigratemanitoba.com/notices/eoi-draw/)",
    unsafe_allow_html=True
)


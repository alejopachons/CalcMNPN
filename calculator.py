

import streamlit as st

st.title("Calculadora de puntaje MPNP (Skilled Worker)")

# Enlace oficial
st.markdown(
    "Fuente: [Expression of Interest (EOI)](https://immigratemanitoba.com/immigrate/apply/eoi/)",
    unsafe_allow_html=True
)

st.header("1. Idioma principal (125 pts máximo)")

# Selección de nivel CLB para cada habilidad del idioma principal
clb_speaking = st.selectbox("¿Cuál es tu nivel en Speaking?", [
    "CLB 8 o más (25 pts)",
    "CLB 7 (22 pts)",
    "CLB 6 (20 pts)",
    "CLB 5 (17 pts)",
    "CLB 4 (12 pts)",
    "Menos de CLB 4 (0 pts)"
], index=None, placeholder="Seleccione una opción...")

clb_reading = st.selectbox("¿Cuál es tu nivel en Reading?", [
    "CLB 8 o más (25 pts)",
    "CLB 7 (22 pts)",
    "CLB 6 (20 pts)",
    "CLB 5 (17 pts)",
    "CLB 4 (12 pts)",
    "Menos de CLB 4 (0 pts)"
], index=None, placeholder="Seleccione una opción...")

clb_listening = st.selectbox("¿Cuál es tu nivel en Listening?", [
    "CLB 8 o más (25 pts)",
    "CLB 7 (22 pts)",
    "CLB 6 (20 pts)",
    "CLB 5 (17 pts)",
    "CLB 4 (12 pts)",
    "Menos de CLB 4 (0 pts)"
], index=None, placeholder="Seleccione una opción...")

clb_writing = st.selectbox("¿Cuál es tu nivel en Writing?", [
    "CLB 8 o más (25 pts)",
    "CLB 7 (22 pts)",
    "CLB 6 (20 pts)",
    "CLB 5 (17 pts)",
    "CLB 4 (12 pts)",
    "Menos de CLB 4 (0 pts)"
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
    st.warning("Por favor selecciona una opción para continuar.")

if clb_reading != None:
    pts_reading = puntos_por_clb[clb_reading]
else:
    st.warning("Por favor selecciona una opción para continuar.")

if clb_listening != None:
    pts_listening = puntos_por_clb[clb_listening]
else:
    st.warning("Por favor selecciona una opción para continuar.")

if clb_listening != None:
    pts_writing = puntos_por_clb[clb_writing]
else:
    st.warning("Por favor selecciona una opción para continuar.")

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

# 2. Edad
st.header("2. Edad (75 pts máximo)")
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
    st.warning("Por favor selecciona tu edad para continuar.")

# 3. Experiencia laboral
st.header("3. Experiencia laboral en los últimos 5 años (175 pts máximo)")
experiencia = st.selectbox("¿Cuántos años de experiencia tienes?", [
    "Menos de un año (0 pts)",
    "1 año (40 pts)",
    "2 años (50 pts)",
    "3 años (60 pts)",
    "4 años o más (75 pts)",
    "reconocido por el organismo de licenciamiento provincial (100 pts)"
], index=None, placeholder="Seleccione una opción...")

puntos_experiencia = {
    "Menos de un año (0 pts)": 0,
    "1 año (40 pts)": 40,
    "2 años (50 pts)": 50,
    "3 años (60 pts)": 60,
    "4 años o más (75 pts)": 70,
    "reconocido por el organismo de licenciamiento provincial (100 pts)": 100
}
if experiencia != None:
    score_experiencia = puntos_experiencia[experiencia]
else:
    st.warning("Por favor selecciona una opción para continuar.")

# 4. Educación
st.header("4. Nivel de educación")
educacion = st.selectbox("Selecciona tu nivel educativo (125 pts máximo)", [
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

if educacion != None
    score_educacion = puntos_educacion[educacion]
else:
    st.warning("Por favor selecciona una opción para continuar.")


st.header("5. Adaptabilidad")

# --- 5.1 Conexión con Manitoba (máximo 200 pts) ---
st.subheader("5.1 Conexión con Manitoba (máx. 200 pts)")

conexion_mb = st.selectbox("Selecciona tu conexión más fuerte con Manitoba:", [
    "Familiar cercano en Manitoba (200 pts)",
    "Experiencia laboral previa en Manitoba (100 pts)",
    "Estudios postsecundarios en Manitoba (2 años o más) (100 pts)",
    "Estudios postsecundarios en Manitoba (1 año) (50 pts)",
    "Amigo cercano o familiar lejano en Manitoba (50 pts)",
    "Ninguna conexión (0 pts)"
])

puntos_conexion_mb = {
    "Familiar cercano en Manitoba (200 pts)": 200,
    "Experiencia laboral previa en Manitoba (100 pts)": 100,
    "Estudios postsecundarios en Manitoba (2 años o más) (100 pts)": 100,
    "Estudios postsecundarios en Manitoba (1 año) (50 pts)": 50,
    "Amigo cercano o familiar lejano en Manitoba (50 pts)": 50,
    "Ninguna conexión (0 pts)": 0
}
score_conexion_mb = puntos_conexion_mb[conexion_mb]

# --- 5.2 Demanda de Manitoba (máximo 500 pts) ---
st.subheader("5.2 Demanda de Manitoba (máx. 500 pts)")

manitoba_demand = st.selectbox("¿Cuál de estas condiciones aplica a tu perfil?", [
    "Empleo actual en Manitoba por 6 meses o más + oferta a largo plazo (500 pts)",
    "Invitación para aplicar bajo una Iniciativa Estratégica (500 pts)",
    "Ninguna (0 pts)"
])

puntos_manitoba_demand = {
    "Empleo actual en Manitoba por 6 meses o más + oferta a largo plazo (500 pts)": 500,
    "Invitación para aplicar bajo una Iniciativa Estratégica (500 pts)": 500,
    "Ninguna (0 pts)": 0
}
score_demand = puntos_manitoba_demand[manitoba_demand]

# --- 5.3 Desarrollo regional (máximo 50 pts) ---
st.subheader("5.3 Desarrollo regional (máx. 50 pts)")

fuera_de_wpg = st.checkbox("¿Planeas establecerte fuera de Winnipeg? (50 pts)")
score_regional = 50 if fuera_de_wpg else 0

# --- Puntaje total de adaptabilidad ---
score_adaptabilidad = score_conexion_mb + score_demand + score_regional


# 6. Evaluación de Riesgo (hasta -200 pts)
st.header("6. Evaluación de riesgo (Risk Assessment)")

riesgos = st.multiselect("Selecciona si alguno de estos factores aplica:", [
    "Has trabajado en otra provincia de Canadá",
    "Has estudiado en otra provincia de Canadá",
    "Tienes familiares en otra provincia de Canadá",
    "Has presentado una solicitud de inmigración a otra provincia"
], index=None, placeholder="Seleccione una opción...")

# Asignar puntajes individualmente
riesgo_puntos = {
    "Has trabajado en otra provincia de Canadá": -100,
    "Has estudiado en otra provincia de Canadá": -100,
    "Tienes familiares en otra provincia de Canadá": 0,
    "Has presentado una solicitud de inmigración a otra provincia": 0
}
if riesgos != None:
    puntos_riesgo = sum([riesgo_puntos[riesgo] for riesgo in riesgos])
else:
        st.warning("Por favor selecciona una opción para continuar.")


# Puntaje total
st.subheader("🎯 Tu puntaje total es:")
puntaje_total = score_educacion + score_experiencia + puntos_totales_idioma + score_edad + score_adaptabilidad + puntos_riesgo
st.metric(label="Puntaje MPNP estimado", value=puntaje_total)

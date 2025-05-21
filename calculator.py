

import streamlit as st

st.title("Calculadora de puntaje MPNP (Skilled Worker)")

# Enlace oficial
st.markdown(
    "Fuente: [Expression of Interest (EOI)](https://immigratemanitoba.com/immigrate/apply/eoi/)",
    unsafe_allow_html=True
)

# 1. Lenguaje
st.header("1. Idioma principal (125 pts máximo)")
clb = st.selectbox("¿Cuál es tu CLB?", [
    "CLB 8 o más (25 pts por banda)",
    "CLB 7 (22 pts por banda)",
    "CLB 6 (20 pts por banda)",
    "CLB 5 (17 pts por banda)",
    "CLB 4 (12 pts por banda)",
    "Menos de CLB 4 (0 pts)",
    "Segundo idioma - CLB 5 o superior [overall] (25 pts)"
])
puntos_idioma = {
    "CLB 8 o más (25 pts)": 25,
    "CLB 7 (22 pts por banda)": 22,
    "CLB 6 (20 pts por banda)": 20,
    "CLB 5 (17 pts por banda)": 17,
    "CLB 4 (12 pts por banda)": 12,
    "Menos de CLB 4 (0 pts)": 0,
    "Segundo idioma - CLB 5 o superior [overall] (25 pts)": 25
    
}
score_idioma = puntos_idioma[clb]

# 2. Edad
edad = st.selectbox("¿Qué edad tienes? (75 pts máximo)", [
    "18 (20 pts)",
    "19 (30 pts)",
    "20 (40 pts)",
    "21 (75 pts) a 45",
    "46 (40 pts)",
    "47 (30 pts)",
    "48 (20 pts)",
    "49 (10 pts)",
    "Más de 50 (0 pts)"
])
puntos_edad = {
    "18 (20 pts)": 20,
    "19 (30 pts)": 30,
    "20 (40 pts)": 40,
    "21 (75 pts) a 45": 75,
    "46 (40 pts)": 40,
    "47 (30 pts)": 30,
    "48 (20 pts)": 20,
    "49 (10 pts)": 10,
    "Más de 50 (0 pts)": 0
}
score_edad = puntos_edad[edad]

# 3. Experiencia laboral
st.header("3. Experiencia laboral en los últimos 5 años (175 pts máximo)")
experiencia = st.selectbox("¿Cuántos años de experiencia tienes?", [
    "Menos de un año (0 pts)",
    "1 año (40 pts)",
    "2 años (50 pts)",
    "3 años (60 pts)",
    "4 años o más (75 pts)",
    "reconocido por el organismo de licenciamiento provincial (100 pts)"
])
puntos_experiencia = {
    "Menos de un año (0 pts)": 0,
    "1 año (40 pts)": 40,
    "2 años (50 pts)": 50,
    "3 años (60 pts)": 60,
    "4 años (75 pts)": 70,
    "reconocido por el organismo de licenciamiento provincial (100 pts)": 100
}
score_experiencia = puntos_experiencia[experiencia]

# 4. Educación
st.header("4. Nivel de educación (125 pts máximo)")
educacion = st.selectbox("Selecciona tu nivel educativo", [
    "Maestría o doctorado (125 pts)",
    "Dos programas postsecundarios de al menos dos años cada uno (115 pts)",
    "Un programa postsecundario de tres años o más (110 pts)",
    "Un programa postsecundario de dos años (100 pts)",
    "Un programa postsecundario de un año (70 pts)",
    "Certificado en oficios (Trade certificate) (70 pts)",
    "Sin educación postsecundaria formal (0 pts)"
    
])
puntos_educacion = {
    "Maestría o doctorado (125 pts)": 125,
    "Dos programas postsecundarios de al menos dos años cada uno (115 pts)": 115,
    "Un programa postsecundario de tres años o más (110 pts)": 110,
    "Un programa postsecundario de dos años (100 pts)": 100,
    "Un programa postsecundario de un año (70 pts)": 70,
    "Certificado en oficios (Trade certificate) (70 pts)": 70,
    "Sin educación postsecundaria formal (0 pts)": 0
}
score_educacion = puntos_educacion[educacion]

st.header("5. Adaptabilidad (máximo 500 pts)")

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
])

# Asignar puntajes individualmente
riesgo_puntos = {
    "Has trabajado en otra provincia de Canadá": -100,
    "Has estudiado en otra provincia de Canadá": -100,
    "Tienes familiares en otra provincia de Canadá": 0,
    "Has presentado una solicitud de inmigración a otra provincia": 0
}

puntos_riesgo = sum([riesgo_puntos[riesgo] for riesgo in riesgos])


# Puntaje total
st.subheader("🎯 Tu puntaje total es:")
puntaje_total = score_educacion + score_experiencia + score_idioma + score_edad + score_adaptabilidad + puntos_riesgo
st.metric(label="Puntaje MPNP estimado", value=puntaje_total)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Título de la aplicación
st.title("🎓 Simulador Educativo Interactivo")

# Sección de entrada de parámetros ajustables
st.sidebar.header("🔧 Parámetros Ajustables")

presupuesto_total = st.sidebar.number_input("Presupuesto Total (COP)", value=8489392000)
cantidad_certificados = st.sidebar.number_input("Cantidad de Personas Certificadas", value=14389)
capacidad_maxima_estudiantes = st.sidebar.number_input("Capacidad Máxima por Curso", value=35)
total_salones = st.sidebar.number_input("Total de Salones", value=411)
numero_docentes = st.sidebar.number_input("Número de Docentes", value=30)

# Parámetros fijos
costo_promedio_curso = 590000
horas_docente_medio_tiempo = 80
horas_docente_tiempo_completo = 160
jornada_am = 4
jornada_pm = 4

# Botón para ejecutar simulación
if st.sidebar.button("Ejecutar Simulación"):
    # Cálculos del simulador
    cursos_posibles = presupuesto_total // costo_promedio_curso
    estudiantes_por_curso = min(capacidad_maxima_estudiantes, cantidad_certificados // cursos_posibles)
    salones_necesarios = min(cursos_posibles, total_salones)
    horas_totales_docentes = numero_docentes * horas_docente_tiempo_completo
    horas_requeridas_por_curso = jornada_am + jornada_pm
    horas_docentes_requeridas = cursos_posibles * horas_requeridas_por_curso

    # Crear DataFrame con resultados
    resultados = pd.DataFrame({
        'Indicador': [
            'Cursos posibles',
            'Estudiantes por curso',
            'Salones necesarios',
            'Horas docentes disponibles',
            'Horas docentes requeridas'
        ],
        'Valor': [
            cursos_posibles,
            estudiantes_por_curso,
            salones_necesarios,
            horas_totales_docentes,
            horas_docentes_requeridas
        ]
    })

    # Mostrar tabla de resultados
    st.subheader("📊 Resultados del Simulador")
    st.dataframe(resultados)

    # Visualización de resultados
    st.subheader("📈 Gráfica de Indicadores")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(resultados['Indicador'], resultados['Valor'], color='skyblue')
    ax.set_title('Simulación de Proyecto Educativo')
    ax.set_ylabel('Valor')
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("👈 Ingresa los parámetros en la barra lateral y presiona 'Ejecutar Simulación'.")

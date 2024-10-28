import streamlit as st

# Inicializamos la variable de estado para el sensor
if "sensor_status" not in st.session_state:
    st.session_state["sensor_status"] = False

st.title("Sensor Detector de Inundaciones")

# Mostrar estado del sensor
if st.session_state["sensor_status"]:
    st.success("El sensor está ACTIVADO y monitoreando.")
else:
    st.warning("El sensor está DESACTIVADO.")

# Botón para activar/desactivar el sensor
if st.button("Activar/Desactivar Sensor"):
    # Cambiar el estado del sensor
    st.session_state["sensor_status"] = not st.session_state["sensor_status"]

    # Mostrar el estado actualizado del sensor
    if st.session_state["sensor_status"]:
        st.success("El sensor ha sido ACTIVADO.")
    else:
        st.warning("El sensor ha sido DESACTIVADO.")

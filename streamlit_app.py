import streamlit as st
import time

st.title("Prosty minutnik")

sekundy = st.number_input("Podaj liczbę sekund:", 1, 120, 10)

if st.button("Start"):
    for i in range(sekundy, 0, -1):
        st.write("Pozostało:", i, "sekund")
        time.sleep(1)

    st.success("Czas minął!")

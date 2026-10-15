
import streamlit as st
import time

st.title("Prosty minutnik")

sekundy = st.number_input("Podaj liczbę sekund:", 1, 120, 10)

if st.button("Start"):
    wynik = st.empty()

    for i in range(sekundy, 0, -1):
        wynik.write(f"Pozostało: {i} sekund")
        time.sleep(1)

    wynik.success("Czas minął!")

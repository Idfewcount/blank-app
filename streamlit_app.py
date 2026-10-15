
import streamlit as st
import random
import time

st.title("Gra: Traf liczbę!")

st.write("Wybierz liczbę od 1 do 5.")
st.write("Komputer wykona 5 losowań.")

liczba = st.number_input("Twoja liczba:", 1, 5, 3)

if st.button("Graj"):
    punkty = 0
    wynik = st.empty()

    for i in range(1, 6):
        los = random.randint(1, 5)

        wynik.write(f"Losowanie {i} - wynik: {los}")

        if liczba == los:
            punkty = punkty + 1
            st.success("Trafienie!")

        if liczba != los:
            st.write("Pudło!")

        time.sleep(1)

    wynik.write("Koniec gry!")
    st.write("Zdobyte punkty:", punkty)

    if punkty >= 2:
        st.balloons()
        st.success("Wygrałeś!")

    if punkty < 2:
        st.error("Przegrałeś! Spróbuj ponownie.")

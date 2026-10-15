
import streamlit as st

st.title("Kółko i krzyżyk")

# Przygotowanie nowej gry
if "plansza" not in st.session_state:
    st.session_state.plansza = [""] * 9
    st.session_state.gracz = "X"
    st.session_state.koniec = False
    st.session_state.wynik = ""

plansza = st.session_state.plansza

st.write("Ruch gracza:", st.session_state.gracz)

# Możliwe zwycięskie układy
wygrane = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]

# Rysowanie planszy
for w in range(3):
    kolumny = st.columns(3)

    for k in range(3):
        i = 3 * w + k

        napis = plansza[i]

        if napis == "":
            napis = "·"

        if kolumny[k].button(
            napis,
            key=i,
            use_container_width=True,
            disabled=plansza[i] != "" or st.session_state.koniec
        ):
            plansza[i] = st.session_state.gracz

            # Sprawdzanie zwycięstwa
            for a, b, c in wygrane:
                if plansza[a] != "":
                    if plansza[a] == plansza[b] == plansza[c]:
                        st.session_state.koniec = True
                        st.session_state.wynik = "Wygrywa gracz " + st.session_state.gracz

            # Sprawdzanie remisu
            if not st.session_state.koniec:
                if "" not in plansza:
                    st.session_state.koniec = True
                    st.session_state.wynik = "Remis!"

            # Zmiana gracza
            if not st.session_state.koniec:
                if st.session_state.gracz == "X":
                    st.session_state.gracz = "O"
                else:
                    st.session_state.gracz = "X"

            st.rerun()

# Wynik gry
if st.session_state.koniec:
    st.success(st.session_state.wynik)

# Rozpoczęcie nowej gry
if st.button("Nowa gra"):
    st.session_state.plansza = [""] * 9
    st.session_state.gracz = "X"
    st.session_state.koniec = False
    st.session_state.wynik = ""
    st.rerun()

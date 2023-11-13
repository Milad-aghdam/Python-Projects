import streamlit as st
from monty_hall import simulation
import time

st.set_page_config(layout="wide")

st.title(" 	:video_game: Monty Hall Simulation")

number_of_game = st.number_input(" ***Input number of game to simulation:***",
                        min_value=1, max_value=10000, value=100)

col1, col2 = st.columns(2)


col1.subheader("Win percentage without switch")
chart1 = col1.line_chart(x=None, y=None, height=400)

col2.subheader("Win percentage with switch")
chart2 = col2.line_chart(x=None, y=None,  height=400)

wins_no_switch = 0
wins_switch = 0

for i in range(number_of_game):
    num_wins_with_switch, num_wins_without_switch = simulation(1)
    wins_no_switch +=  num_wins_without_switch
    wins_switch += num_wins_with_switch

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
 




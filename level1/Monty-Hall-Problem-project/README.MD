# Monty Hall Simulation
This project simulates the Monty Hall problem, a famous probability puzzle based on a game show. The problem is as follows:

Suppose you’re on a game show, and you’re given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what’s behind the doors, opens another door, say No. 3, which has a goat. He then says to you, “Do you want to pick door No. 2?” Is it to your advantage to switch your choice?

The project consists of two scripts:

- ``` monty_hall.py```: This script defines two functions that simulate one round and multiple rounds of the Monty Hall game, respectively. It also prints the number of wins for each strategy when run as a main script.
- ```app.py```: This script uses the Streamlit framework to create a web app that visualizes the simulation results in real time. It allows the user to input the number of games to simulate and displays the win percentage for each strategy as line charts.

## Installation
To run the project, you need to have Python 3.6 or higher installed on your system. You also need to install the following packages:

- ```random```: This is a built-in module that implements pseudo-random number generators for various distributions.
- ```streamlit```: This is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.

You can install the packages using the following command:

``` bash 
pip install streamlit
 ```

## Usage
To run the simulation script, navigate to the project directory and execute the following command:
```bash 
python monty_hall.py
```

This will print the number of wins for each strategy for 10000 games. You can change the number of games by modifying the number variable in the script.

To run the web app, navigate to the project directory and execute the following command:
``` bash
streamlit run app.py
```

This will launch the app in your default browser. You can input the number of games to simulate and see the win percentage for each strategy as line charts. The app will update the charts as the simulation progresses.
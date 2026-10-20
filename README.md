# Traffic-Simulation-in-Python

A minimal Python simulation of a traffic light controller. It cycles through green, yellow and red and prints the current state as simulated time passes.

## How it works

- A `TrafficLight` class holds the current state (`green`, `yellow`, `red`).
- Each tick, a random amount of time (1 to 5 seconds) is added to a timer.
- Once 60 simulated seconds pass, the light moves to the next state.
- The loop prints the state every second and runs until you stop it.

## Run it

```bash
python main.py
```

Stop it with `Ctrl+C`. No external packages are needed, only the Python standard library.

## Example output

```
Current state of traffic light: green
Current state of traffic light: green
...
Current state of traffic light: yellow
```

## Ideas for extending it

- Different durations for each light colour
- Multiple intersections or cars
- A graphical view with `pygame` or `tkinter`


---

<sub>Made by [tanaytejush](https://github.com/tanaytejush)</sub>

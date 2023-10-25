# Virtual Rubik's Cube App

## Introduction

*The Rubik’s Cube is often seen as an impossible task, that “some people can do, but not me”. But the cube wonderfully demonstrates what it takes to be great at anything. With a curious mind, patience and a little guidance, anyone can do it*

This comprehensive app serves as a one-stop solution for all things related to the Rubik’s Cube. It offers features ranging from solving random cube configurations to providing a virtual cube for learning, honing skills, and making progress. Additionally, it includes a timer to help enthusiasts enhance their speed in solving the Rubik’s Cube.

## Index

- [Introduction](#introduction)
- [Index](#index)
- [About](#about)
- [Details](#details)
- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [File Structure](#file-structure)
- [Notes](#notes)


## About

This project acts as a virtual Rubik’s Cube application, similar to what you might find on a computer or phone. It assists in finding solutions for jumbled Rubik’s Cubes and doubles as a timer to clock how fast you can solve it, whether using a physical cube or a virtual one in the program. Additionally, it keeps a log of your solves for easy reference.

Catering to a broad audience, from beginners to seasoned cubers, this project offers a wide range of features. For newcomers, it provides valuable support in tackling random cube patterns and offers a virtual platform for learning and refining Rubik’s Cube-solving skills. For those with more experience, it provides a new way to solve cubes on a screen, along with a timer and detailed information about your solves to help you get even better.

## Details

### Project Overview

- **Virtual Cube** provides a platform for learning and practicing solving
cubes in a virtual cube.
- **Cube Solver** automatically provides the solution for any particular scramble of a real cube.
- **Cube Timer** is used to measure time taken to solve a real Rubik’s cube and keeps a track of all the saved times.

### Packages Used
- **matplotlib**: Utilized for plotting the 3D interactive Rubik’s Cube.
- **tkinter**: Employed for the entire graphical user interface (GUI) aspect of the program, encompassing window displays, interactive buttons, and overall user-friendliness.
- **selenium**: Used to interact with a website for obtaining the most efficient solution for any given Rubik’s Cube configuration. This is achieved through the utilization of the Kociemba-Korf Algorithm, a complex computer algorithm, capable of solving the Rubik’s Cube in under 20 moves.
- **numpy**: Employed to create a 2D array of data necessary for plotting the cube using matplotlib.
- **copy**: Used for duplicating various lists in order to prevent aliasing.
- **random**: Utilized for generating random scrambles.
- **time**: Involved in the functioning of the timer.
- **sqlite**: Utilized to establish a connection between an sql database and Python, enabling the modification and retrieval of data from tables in a database.

### Modules
- **main.py** - The main program consisting of a GUI window using tkinter
and options in the form of a menu to perform different actions.
- **cube_moves.py** - Consists of all the possible legal moves that can be performed on a Rubik’s cube. Operations are done on a 2D list which stores the current position of the cube.
- **display_cube.py** - Consists of a method which displays the position of the cube (from a 2D list) as a 3D interactable graph using the matplotlib package.
- **cube_solver.py** - Consists of a method which uses the selenium package to get the most effective solution of any Rubik’s cube position from a website.
- **virtual_cube.py** - Displays a window consisting of a 3D cube (from display.py) with various buttons to interact with the cube as well as with an optional timer.
- **web_solver.py** - Displays a window allowing the user to enter any scrambled state of the cube and displays the most effective solving steps (from solver.py) along with a simple animation of the solve.
- **cube_timer.py** - Displays a window with a timer along with a random scramble that can be used to time the solves performed on a real cube with the user. It also displays the best, worst and average time of solves.
- **db.py** - Displays a window consisting of all the details of solves performed.

### Database Details
The **times** table in database **cube_db** is used to store the details of all the saved sessions along with timestamp. Each session consists of a unique name, the number of solves, best solve, worst solve and average time for the solves. The times table is used to track the overall progress over a period of time.

| Field | Type | Null  | Default
|----|------------|-------|-----
|Session_Name|varchar(20)|YES|NULL|
|Date_Time|datetime|YES|NULL
|Average_Time|varchar(10)|YES|NULL
|Fastest_Solve|varchar(10)|YES|NULL
|Worst_Solve|varchar(10)|YES|NULL
|Solves_Count|INTEGER|YES|NULL


## Usage
### Prerequisites
A `python 3.9` or newer environment with `matplotlib`, `tkinter` and `sqlite3` installed.
```
python setup.py install
```
Or alternatively run this command in a python environment.
```
pip install -r requirements.txt
```

### Installation

1. Clone the repository using the command:
```
git clone https://github.com/gaurav-behera/virtual-rubiks-cube.git
```
2. Run `main.py` from the `./rubiks-cube` directory
```
python main.py
```

### File Structure
```
.
├── README.md
├── requirements.txt
├── rubiks_cube
│   ├── cube_moves.py
│   ├── cube_solver.py
│   ├── cube_timer.py
│   ├── db.py
│   ├── display_cube.py
│   ├── main.py
│   ├── utils
│   │   ├── chromedriver
│   │   ├── cube_db.sqlite
│   │   └── info.txt
│   ├── virtual_cube.py
│   └── web_solver.py
└── setup.py
```

## Notes
1. The project should work completely fine on a mac device and might not work on windows/linux (due to `tkmacosx` package). Code will be updated to account for all OS.
2. The project relies on `selenium`, so the `chromedriver` present in the `/rubiks-cube/utils` folder can be changed based on the version of chrome installed.
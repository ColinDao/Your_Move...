# Your Move...

## Project Description

This project implements an AI player in Python for the classic game of Tic-tac-toe. The agent uses the minimax algorithm with alpha-beta pruning to make optimal moves and ensure it never loses. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Credit](#credit)
- [License](#license)

## Installation

You'll need to have Python and pip3 installed. You can download them from the [official Python website](https://www.python.org/downloads/).

1. Clone the repository:

```bash
git clone https://github.com/ColinDao/your-move.git
```

2. Navigate to the project directory:

```bash
cd your-move
```

3. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

To play against the AI, run the following command:

```bash
python runner.py
```

Follow the prompts to make your moves. The AI player will respond with its moves based on the optimal strategy. Good luck, it never loses!

## Features

**Minimax Algorithm**: The AI agent uses the minimax algorithm to search through the possible outcomes and determine the best move to make. <br />
<br />
**Alpha-Beta Pruning**: Alpha-beta pruning is applied to optimize the minimax algorithm and reduce the number of paths explored. <br />
<br />
**Graphical User Interface (GUI)**: A simple GUI is provided to visualize the Tic-tac-toe board and player moves.

## Credit

This project was completed as a part of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/). Go check them out!

## Technologies
**Language**: Python <br />
**Libraries**: Pygame, Time, Sys, Copy

## License

MIT License

Copyright (c) 2024 Colin Dao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

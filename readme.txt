This is an interactive Command Line Interface of solving Travelling Salesman Problem to determine the shortest distance
between given nodes in a graph.
The interface starts with pre-constructed nodes from: https://www.geeksforgeeks.org/wp-content/uploads/Euler12-300x225.png
It gives options to add node, delete node. Follow the prompts and the shortest path and distance will be updated.

The interface was built on Mac-OS Python 3.9 and is tested on Ubuntu 18.04 Python 3.6.9.
Filename: requirements.txt contains all the dependencies that are compatible with Python version 3.6.9 or higher

To start on Ubuntu desktop, open the terminal and follow the below steps:

1. Navigate to the current repository and Create a virtual environment.
python3 -m venv tsp_env

2. Activate virtual environment:
source tsp_env/bin/activate

3. Check the Python version on your desktop to make sure it is 3.6.9 or higher:
Python3 --version
> Python 3.6.9

4. Install the dependencies from requirements.txt file:
python3 -m pip install -r requirements.txt

5. Run the interactive Travelling Salesman Problem Demo:
python3 main.py

If the Python version is lower, the demo should still work, however, the dependencies should be installed manually.
If pip i3 is not installed, follow admin commands as: 1. sudo apt update  2. sudo apt install python3-pip
If there is any error in installing requirements.txt file, please consider to install the dependency manually as this
demo is not tested on the ubuntu 20.04.

For any other questions or comments, feel free to reach to: abhivellala@gmail.com

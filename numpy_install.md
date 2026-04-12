# Numpy install guideline
## Step 1: Make sure we r inside the folder
cd numpy_learn (or ~/numpy_learn)
## Step 2: Create a virtual environment:
python3 -m venv venv
This create a folder called venv inside the project. It will be the priv Python sandbox
## Step 3: Activation
source venv/bin/activate
It will change the terminal to show (venv) on the left - it means it's activated

Note: you need to do this step every time u open new terminal to activate it, to deactivate just type in command line 'deactivate'
## Step 4: install numpy inside it
pip install numpy
## Step 5: run the file
python3 numpy_practice.py

# Folder structure 
numpy_learn/
├── venv/          ← your sandbox (don't touch this)
└── numpy_practice.py ← your code
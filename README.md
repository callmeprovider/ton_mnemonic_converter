#### TON Mnemonic Formatter

A script for cleaning mnemonic phrases by removing numbers, dots (.), and parentheses (()) while preserving the original line structure.

#### Dependency Installation for Windows:
	1. cd path\to\project.
	2. python -m venv venv.
	3. .\venv\Scripts\activate.
	4. pip install -r requirements.txt.

#### Dependency Installation for MacOS / Linux:

Run the following commands in the terminal:
	1. cd path/to/project.
	2. python3 -m venv venv.
	3. MacOS/Linux: source venv/bin/activate.
	4. pip install -r requirements.txt.

#### Configuration:

Place your input mnemonic file in the root of the project directory and name it mnemonic.txt. Each line should contain mnemonic phrases.

#### Running the Script:
	1.	Make sure mnemonic.txt contains your mnemonic phrases that need cleaning.
	2.	Run the script using the following command:
	•	Windows: python3 main.py
	•	MacOS / Linux: python3 main.py

The cleaned phrases will be saved in the result.txt file, maintaining the original line structure.

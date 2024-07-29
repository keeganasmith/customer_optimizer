# Build/Installation

Dependencies: \
Node v20.10.0 - https://nodejs.org/en/learn/getting-started/how-to-install-nodejs \
Python 3.12.1 - https://www.python.org/downloads/ 

first clone the repo: \
```git clone https://github.com/keeganasmith/customer_optimizer.git``` \
Install all relevant packages with: 
```
cd customer_optimizer
cd backend
pip install -r requirements.txt
cd ..
cd frontend
npm install
```
Create a .env file with the contents: 
```
DATABASE_URI=<enter your psql database uri here>
PIN=<enter a random pin here>
```
# Running the program

Open two terminals, in one terminal run: 
```
cd backend
python3 main.py
```
in the other run:
```
cd frontend
npm run dev
```
Open http://localhost:5173 in your browser
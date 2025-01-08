# TOPO_assignment

### Setting Up the Environment
1. Clone the Repository

```
git clone https://github.com/JingRonggg/TOPO_assignment.git
```
2. Enter backend directory
```
cd cd .\backend\
```
2. Create a Virtual Environment

```
python3 -m venv venv
```
3. Activate the Virtual Environment
```
venv/Scripts/activate
```
4. Install Required Packages
```
pip install -r requirements.txt
```
5. Run the app
```
flask --app app --debug run
```
6. Using another terminal, Go back to root directory (go to TOPO_assignment directory)
```
cd ..
```
7. Enter frontend directory
```
cd .\frontend\
```
8. Install node packages
```
npm install
```
9. Run frontend
```
npm run dev
```

### To run the tests
1. cd into backend
``` 
cd ./backend/
```
2. activate venv
```
venv/scripts/activate
```
3. run pytests
```
pytests -v
```
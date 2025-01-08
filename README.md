# TOPO_assignment
### Overview
Backend uses Flask Framework to develop
Frontend uses React with Vite

When building the app, there were a lot of considerations that I had to do. One example was that I wanted to use SpringBoot for the backend as SpringBoot forces design patterns such as factory design pattern with strategy method. However, after developing with SpringBoot, I realise that it was not as fast as I thought, and I had to make the decision to switch over to Flask to develop the backend. 

I attempted to follow the model view controller (MVC) where the data is ingested in from the services and stored in the repositories. The routes folder contains all the controllers and endpoints. While developing, I have the habit of making CRUD endpoints for each controller to test while developing, hence why I did not delete those redundant endpoints. 

As for the data cleaning, I noticed that there were null values, hence I ignored those data points instead of mocking a random value for it. Moreover, I did notice that all the datasets were linked to the company FitPro, and in the dataset4.pptx, I fully ignored slide 2 as the data was repeated inside dataset2.csv.

The entry point of the backend will be backend/app.py.

Filtering of data is done on the frontend as I do not want to have too many API calls to the backend
Having too many API calls to the backend would bottleneck the system in a large applications, moreover, if there are a lot of filtering to be done with the data itself, perhaps it would be better to use GraphQL instead of REST API

On the frontend side, I have made up a table and a pie chart to represent the data required. 
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
pytest -v
```

### Assumptions and Challenges
#### Assumptions
1. I assumed that the null data were wrong data and excluded it from the data processing
2. I assumed that the pptx will not change in terms of data, I extracted it with some string manipulation
#### Challenges
1. Figuring out how to extract data from pptx
2. Figuring out how to develop a half decent frontend as I do not have much experience with frontend development
3. Figuring out how to filter the data on the frontend side as I want to call as little endpoints as possible.
4. A lot of researching and chatgpt was required on my end as there were a lot of bugs I ran into while developing it.
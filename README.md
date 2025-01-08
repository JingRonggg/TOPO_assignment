# TOPO Assignment

## Overview
This project implements a full-stack application with the following tech stack:
- **Backend**: Flask Framework
- **Frontend**: React with Vite
- **Database**: SQLite

### Approach
The initial backend development began with Spring Boot, chosen for its design-pattern enforcement (e.g., factory design pattern with strategy method). However, it was later switched to Flask for better performance and simplicity. The backend adheres to the Model-View-Controller (MVC) design pattern:
- **Models**: Data ingestion is handled by services and stored in repositories.
- **Controllers**: Contain endpoints and route logic. CRUD endpoints are included for testing purposes.

Data filtering is implemented on the frontend to reduce backend API calls, optimizing system performance. This trade-off aligns with scalability concerns, especially for large applications. For such cases, GraphQL may be a preferable alternative to REST APIs.

The frontend features a **table**, a **pie chart** and a **line chart** to represent data visually, ensuring an interactive and informative user experience. Feel free to interact with the charts

**Key considerations:**
- Null values in the datasets were excluded instead of being mocked.
- Duplicated data (e.g., `dataset4.pptx` slide 2) was ignored if it was already present in `dataset2.csv`.

The backend entry point is located in `backend/app.py`.

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/JingRonggg/TOPO_assignment.git
cd TOPO_assignment
```

### Docker setup (for easier running of the app)
1. Have docker installed
2. Open up docker application
3. Run
   ```bash
   docker-compose up --build
   ```
4. Frontend is hosted on http://localhost:5173/
5. Backend is hosted on http://localhost:5000/
### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd ./backend
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   venv/Scripts/activate  # For Windows
   source venv/bin/activate  # For macOS/Linux
   ```
4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file:
   - Follow the structure in `example.env`.
   - Update the database path: `sqlite:///database.db`.
6. Run the Flask app:
   ```bash
   flask --app app --debug run
   ```

### Frontend Setup
1. Open a new terminal and navigate back to the project root:
   ```bash
   cd ../frontend
   ```
2. Install required node packages:
   ```bash
   npm install
   ```
3. Run the frontend development server:
   ```bash
   npm run dev
   ```

---

## Testing Instructions

1. Navigate to the backend directory:
   ```bash
   cd ./backend
   ```
2. Activate the virtual environment (Assuming you have installed the env):
   ```bash
   venv/Scripts/activate  # For Windows
   source venv/bin/activate  # For macOS/Linux
   ```
3. Execute tests using Pytest:
   ```bash
   pytest -v
   ```

---

## Assumptions and Challenges

### Assumptions
1. Null data points were considered erroneous and excluded during processing.
2. Data in `dataset4.pptx` (slide 2) was assumed redundant, as it overlapped with `dataset2.csv`.
3. The `pptx` dataset's structure was assumed fixed for string manipulation.

### Challenges
1. Extracting data from `pptx` files required learning new parsing techniques.
2. Limited experience with frontend development posed challenges in implementing UI components like charts.
3. Filtering data on the frontend was non-trivial, especially while ensuring minimal API calls to the backend.
4. Debugging various bugs and learning new tools involved extensive research and assistance (e.g., from ChatGPT).

---

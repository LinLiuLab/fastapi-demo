# FastAPI Demo

Demo of FastAPI for the [Software Engineering 2024](https://linliulab.github.io/SE-2024/) course.

## Pre-requisites

-   Python 3.8 or above

## Quick Start(Docker)

```bash
docker-compose up
```

## Quick Start(Manual)

1. Clone this repository

```bash
git clone https://github.com/linliulab/fastapi-demo.git
```

2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

3. Initialize the database

-   Create a database named `fastapi_demo` in MySQL
-   Edit the database connection string in `fastapi_demo/database.py` (line 9)

4. Run the server

```bash
python -m fastapi_demo.main
```

5. Open the [API documentation](http://localhost:8000/docs) in your browser

from fastapi import FastAPI
# This line imports the FastAPI class from the fastapi module. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

app : FastAPI = FastAPI()
# Here, an instance of the FastAPI class is created and assigned to the variable app. This app will be the main point of interaction with our web application.

# This line is a decorator that tells FastAPI that the function below should be called when the user makes a GET request to the root URL (“/”) of the application.
@app.get("/") 
def index() -> str:
    return "This is Rafi Ali"

# This is the function that gets called when a GET request is made to the root URL (“/”). It returns the string “This is Rafi Ali”. The -> str part is a Python type hint that indicates this function returns a string.

# So, when you run this application and navigate to the root URL, you will see the text “This is Rafi Ali” displayed in your web browser. This is a very basic example of how you can use FastAPI to create web applications. FastAPI can do much more, including handling more complex routes, request parameters, and data validation.
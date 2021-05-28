# todo-app-fastapi
This project has a command-line interface and the backend which has the APIs that would be accessed to retrieve data.
The command-line interface is coded using Python 3 argParse module and the back end in created using FastAPI which is a python web framework.

To Run the Project follow the steps below:

> Create a python3 virtual environment:  
`python3 -m venv todo-env`

> Activate a virtual enviromrnt:  
`source todo-env/bin/activate`

> Install all required packages:  
`pip install -r requirement.txt`

> To run the program go into todo-cli directory and run make run command:  
`cd todo-cli`  
`make run`

> To use the CLI run the following command:  
`todo --help`

> To test the whole application(CLI and APIs):  
`make test`

> We can run the apis sperately by typing the following commands:  
`cd ../todo_app`  
`make run` or `uvicorn todo_app.main:app`

> To test the API:  
`make test` or `pytest`

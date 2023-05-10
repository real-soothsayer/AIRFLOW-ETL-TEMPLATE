
This is a base template for ETL profects with airflow. 

## I. Versions
- Python >= 3.8
- Airflow = 2.4.0

## II. Prerequisites

Move to the root of the project

### II.1 Initial installations
- **python** : Install python from the [official website](https://www.python.org/downloads/). If you already have python installed, you can use it if the version is >= 3.8 or manage many versions of python with pyenv. 
Please ensure that you have the right version : `python --version`
*(for some installations, the binary is called python3)*
- **pip** : It should be installed with python.
You can check if pip is linked to the right version of python : `pip --version`
You can use python module execution to ensure that you are running pip with the right version of python : `python -m pip --version`
- **virtualenv** : Install with the command : `python -m pip install --user virtualenv`

### II.2 Install other packages
1. Setup the airflow home directory.
`export AIRFLOW_HOME=<define-airflow-home-location>`
*(e.g. AIRFLOW_HOME=$(pwd)/airflow. If you don't set this parameter, Airflow will be installed into a default location)*
2. Create a virtual environment named *.venv*
`python -m virtualenv .venv`
3. Activate virtual environment
`source ./.venv/bin/activate`
4. Install the requirements
`python -m pip install -r requirements.txt`

### II.3 Run airflow

5. Setup airflow configuration items
`export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/dags`  (Update dags_folder parameter)
`export AIRFLOW__CORE__LOAD_EXAMPLES=False`  (Update load_examples parameter)
*(You can also perform this by directly modifying the airflow.cfg file)*
6. Run airflow 
`airflow standalone`

## III. Code

### III.1 Config
Update `root_path`, `data_path`, and `notif` parameters values and add new parameters to the config file if needed

### III.2 Project organisation
This is the project structure
```
dags/
├── etl/
│   ├── common/
│   │   ├── deduplicate.py
│   │   └── ...
│   ├── dags_definitions/
│   │   ├── deduplicate.py
│   │   └── ...
│   │── utils/
│   │   └── ...
│   │── hooks/
│   │   └── ...
│   │── sensors/
│   │   └── ...
│   └── __init__.py
└── .airflowignore
```
- **dags_definitions** : Here we store airflow dags definition files
- **common** : This is the place for python operators functions<>
- **utils** : Custom functions 

PS : 
`deduplicate` is an example of use case of data manipulation and should be dropped
`etl` is the name of the project package and you can change is if you want

### III.3 Testing
As per test driving development, you should create the tests while developping and even before.
All the unit tests should be stored into the folder `tests/`. Take advantage of fixtures, mocking, ... to improve your tests. All the test files should be named with the same suffix `test_*.py`.
The command to run tests is : `pytest`

## IV. Finalization
1. Documentation
`export PYTHONPATH=./dags`
run doc generation : `pdoc --html --force etl --html-dir docs` *(replace etl with the name of the project package if it is different)*
2. Security scan
`bandit -r . -lll -o security.html -f html`
3. Test
Check the test coverage : `coverage run -m pytest`
Run the tests : `pytest`
4. Lint
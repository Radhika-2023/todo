# Backend code repo for Xplor v2.0

### Note:
* Always create a feature branch while working on something new based out of main branch.
* Never pull the changes from a different branch directly into main branch. Raise a pull request instead to main branch.
* Make sure the database url is correct in alembic.ini before doing any migrations.

### Follow the below steps for configuring the project.

1. Create a virtual env [venv] in the root directory
2. Install the required packages from requirements.txt in the virtual env
    > ./venv/Scripts/activate
    
    > pip install -r requirements.txt
3. Create a file "env.py" inside "app" folder with the below contents:


    > DATABASE_URL = 'postgresql://<user_name>:<pass_word>@<host_name>:<port_no>/<database_name>'

    > JWT_SECRET_KEY = '<secret_key>'

    > ALGORITHM = "HS256"
4. Create an empty folder named "versions" inside the folder "alembic"

### Reference:
* Staging the models
    > alembic revision  --autogenerate -m "First commit"
* Updating the migration head
    > alembic upgrade head
* Starting uvicorn app-server
    > uvicorn main:app --reload
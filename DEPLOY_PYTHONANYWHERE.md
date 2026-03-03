# Deploy To PythonAnywhere (Free)

This project is a Flask app and can be deployed on PythonAnywhere Free.
The free tier limits include 1 web app, 512 MiB disk, and web apps expire
after 1 month (renew in the dashboard).

## Steps
1. Create a PythonAnywhere account and open a Bash console.
2. Upload this project to /home/<username>/the_large_project.
3. Create a virtualenv and install dependencies:
   - mkvirtualenv --python=/usr/bin/python3.X techtalk-venv
   - pip install -r /home/<username>/the_large_project/requirements.txt
4. Web tab -> Add a new web app -> Manual configuration -> select Python version.
5. Set the virtualenv path to /home/<username>/.virtualenvs/techtalk-venv.
6. Edit the WSGI config file and add:
   import sys
   path = '/home/<username>/the_large_project'
   if path not in sys.path:
       sys.path.insert(0, path)
   from wsgi import application
7. Web tab -> Static files:
   - URL: /static/
   - Path: /home/<username>/the_large_project/Thetechblog/static
8. Web tab -> Environment variables:
   - SECRET_KEY: set a long random string
9. If you need to initialize the DB:
   - export FLASK_APP=app.py
   - flask db upgrade
10. Click Reload in the Web tab.

- It is assumed Django is installed on the machine
    - to check if it is there run `$ python -m django --version`

# What these files are:
- `mysite/` root directory is just a container for the project and Django doesnt care about its name and it can be renamed. 
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner `mysite/` directory is the actual Python package for your project. and it can be used when I try to import from package (e.g. mysite.urls).
- `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- 

# Create the project 

1. create another folder with name of the project using `startapp`
    `$ python manage.py startapp projectname`
2. And write the first view code in `projectname/views.py`
3. To call the view, we need to map it to a URL - and for this we need a URLconf. To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like: 
4. The next step is to point the root URLconf at the polls.urls module. In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:



# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# Installs Django 
RUN pip3 install django

# Mounts the application code to the image
COPY . code
WORKDIR /code

# Open up port 8000 in the container which is the port Django uses by default to run the server
EXPOSE 8000

# Create tables in the project database so that we can use database tables
RUN python /code/tic_tac_toe_py/manage.py migrate

# runs the production server
ENTRYPOINT ["python", "tic_tac_toe_py/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
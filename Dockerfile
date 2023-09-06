# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip3 install -r requirements.txt
RUN pip3 install django
RUN python3 tic_tac_toe_py/manage.py migrate

# Mounts the application code to the image
COPY . code
WORKDIR /code

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "tic_tac_toe_py/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
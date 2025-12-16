#Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

#Copy your application code
COPY . /app

# install the dependencies
RUN pip install -r requirements.txt

# exposing the port where fast api app will run
EXPOSE 5000

CMD ["python", "app.py"]
# -- Image you are going to inherit
FROM python:3.7-alpine
# -- (optional) Who's maintaining the project
LABEL maintainer="Gaylon Alfano"

# -- Set the Python unbuffered environment variable
# -- Recommended when running Pythin within Docker containers
# -- It doesn't allow Python to buffer the outputs. Just prints directly.
# -- This avoids complications with Docker image when running your Python app.
# -- Adding DONTWRITE so Python won't write to .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pwd
RUN ls

# -- Switch to this new directory (like cd basically) and set as default
# -- Any application we run from the Docker container will start/run from this directory
WORKDIR /app

RUN pwd
RUN ls

# -- Install dependencies from pipenv
COPY Pipfile Pipfile.lock /app/

RUN pwd
RUN ls

RUN pip install pipenv && pipenv install --system

RUN pwd
RUN ls

# -- Copy from local machine /app folder to /app folder in our image.
# -- Allows us to copy our code we create and copy to our Docker image.
COPY . /app/

RUN pwd
RUN ls
RUN ls app

# -- Create a user that is going to run our application using Docker
# -- The -D specifies that the user will ONLY run our process from our project.
RUN adduser -D user

# -- Switches Docker to the user we just created. This is for security. Limits their scope.
# -- If we don't use this then the image will run using the root account.
# -- That means if somebody compromises our application they can have root access
# -- to the whole image.
USER user
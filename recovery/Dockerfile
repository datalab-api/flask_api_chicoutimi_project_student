# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster


# expect a build-time variable
ARG DB_HOST
ARG DB_USER
ARG DB_PASSWORD
ARG DB_PORT
ARG DB_NAME
ARG REDIS_URL
ARG FLASK_DEBUG
ARG FLASK_APP
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# add vars env app
ENV FLASK_DEBUG=${FLASK_DEBUG:-True}
ENV FLASK_APP=${FLASK_APP:-api8inf349}

# vars database apps 
ENV DB_HOST=${DB_HOST:-localhost}
ENV DB_USER=${DB_USER:-user}
ENV DB_PASSWORD=${DB_PASSWORD:-pass}
ENV DB_PORT=${DB_PORT:-5432}
ENV DB_NAME=${DB_NAME:-api8inf349}
ENV REDIS_URL=${REDIS_URL:-redis://localhost}


# Install pip requirements

WORKDIR ${FLASK_APP}

COPY requirements.txt ./requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY main.py ${FLASK_APP}
COPY services.py ${FLASK_APP}

USER root

EXPOSE 5000

CMD [ "python3", "main.py" ]


#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



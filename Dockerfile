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
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

COPY entrypoint.sh /app    
RUN chmod u+x entrypoint.sh


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER root

EXPOSE 5000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "-w 4 -b :5000 --access-logfile - --error-logfile - app:app"]
#ENTRYPOINT ["sh", "entrypoint.sh"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]



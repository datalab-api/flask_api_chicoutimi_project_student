FROM alpine:latest



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


RUN apk add --no-cache python3-dev \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY services.py /app
COPY main.py /app

COPY requirements.txt ./requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python3", "main.py"]
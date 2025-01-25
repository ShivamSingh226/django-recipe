FROM python:3.9-alpine3.13
LABEL maintainer="shivamsingh226"
ENV PYTHONUNBUFFERED 1
COPY ./req.txt  /tmp/req.txt
COPY ./req.dev.txt  /temp/req.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/req.txt && \
    if [$DEV="true"]; \
        then /py/bin/pip install -r /tmp/req.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
ENV PATH="/py/bin:$PATH"
USER django-user

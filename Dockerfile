FROM python:3.8.5
ENV PYTHONUNBUFFERED=1

RUN mkdir /carnot
WORKDIR /carnot
COPY requirements.txt /carnot/
# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python xlstosql.py

RUN apt-get update

COPY . /carnot/

EXPOSE 80

# CMD ["gunicorn", "astro.wsgi:application" "--bind" "0.0.0.0:80"]


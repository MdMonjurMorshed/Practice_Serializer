# set python version for runtime parrent image
FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

# create working directory
WORKDIR /app
RUN mkdir src

# copy requiremets.txt file to the workign directroy

COPY requirements.txt /app

# install dependency and requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

# now copy the all directory into the working directory

COPY . /app/src

EXPOSE 8000

# make command to run server

CMD ["python", "src/manage.py","runserver","0.0.0.0:8000"]



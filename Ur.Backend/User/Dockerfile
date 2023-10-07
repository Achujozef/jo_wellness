FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /user

COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt

# COPY . .

# CMD ["python","manage.py","runserver","0.0.0.0:8001"]
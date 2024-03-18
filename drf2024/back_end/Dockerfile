FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN mkdir /back_end

WORKDIR /back_end

ADD . /back_end/

RUN pip install -r requirments.txt

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
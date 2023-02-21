FROM python:3.9.0

WORKDIR /home/

RUN echo "testingg"

RUN git clone https://github.com/Park-Min-Jeong/PZONE-Django-Test.git
# RUN git clone https://github.com/jeonghui95/P_ZONE_Cloud.git

WORKDIR /home/PZONE-Django-Test

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get -y install libgl1-mesa-glx

RUN pip install gunicorn

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash","-c"," gunicorn P_ZONE_NOTICE.wsgi gunicorn --env DJANGO_SETTINGS_MODULE=P_ZONE_NOTICE.settings --bind 0.0.0.0:8000"]
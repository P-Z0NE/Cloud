FROM python:3.9.0

WORKDIR /home/

RUN echo "t"

RUN git clone https://github.com/jeonghui95/P_ZONE_MAP.git

WORKDIR /home/P_ZONE_MAP/P_ZONE_MAP

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash","-c"," gunicorn P_ZONE_NOTICE.wsgi gunicorn --env DJANGO_SETTINGS_MODULE=P_ZONE_NOTICE.settings --bind 0.0.0.0:8000"]
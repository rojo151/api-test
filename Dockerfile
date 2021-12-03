FROM python:3.8.2
ADD . /app
WORKDIR /app
RUN pip install -r ./api/requirements.txt
CMD [ "python", "./api/app.py" ]
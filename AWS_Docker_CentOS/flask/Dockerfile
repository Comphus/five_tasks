FROM python:3.7-slim
USER root
WORKDIR /app
add . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80 5000
ENV NAME World
CMD [ "python", "app/app.py"]
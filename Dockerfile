FROM python:3.7.10-slim-buster

COPY . /app/web_scraping
WORKDIR /app/web_scraping

# Install python dependencies
RUN pip install -r requirements.txt

CMD python run.py
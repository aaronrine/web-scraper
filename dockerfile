FROM python:3.9.2
ADD scraper.py /
RUN pip install \
  beautifulsoup4 \
  requests \
  matplotlib
CMD ["python","./scraper.py"]
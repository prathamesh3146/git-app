FROM python
WORKDIR /src
COPY app.py .
EXPOSE 5000
RUN pip install flask
CMD python app.py
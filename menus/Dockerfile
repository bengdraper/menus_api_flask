FROM python:3.12

WORKDIR /app/menus
ENV FLASK_APP=wsgi.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app/menus

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0"]


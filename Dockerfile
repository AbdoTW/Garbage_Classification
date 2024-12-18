FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy all project files to /code
COPY . /code

EXPOSE 8000

# Run Streamlit from the /code directory
CMD ["streamlit", "run", "main.py"]
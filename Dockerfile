FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy all project files to /code
COPY . /code

EXPOSE 8000

# command to running streamlit app on spesific port 
CMD ["streamlit", "run", "main.py", "--server.port" , "8000"]  
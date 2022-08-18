#Getting Base Image 

From python:latest

WORKDIR /usr/app/src

COPY Calculator.py ./

# no requirements to be added

CMD ["python", "Calculator.py"]

FROM python:3.8

WORKDIR /workspace
ADD requirements.txt ./requirements.txt
ADD jj2_assert.py .
ADD run.py .
RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "run.py"]

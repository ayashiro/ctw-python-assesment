FROM  python:3.7.16-alpine3.17
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python get_raw_data.py
CMD [ "python", "./main.py" ]


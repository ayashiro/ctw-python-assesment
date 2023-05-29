# CTW Coding assesment
there are two types of assesments I've worked on.
1. implement function to get Daily Stock price data from Alpha flold api then save it into database.
2. Provide a HTTP endpoint to retrive data saved on database on the first assesment.
## how to run the data 
### Task 1 
1. install required package 
```
 pip install --no-cache-dir -r requirements.txt
```
2. run `python get_raw_data.py`
1. all the data is stored on data.db, you can access `sqlite3 data.db` and run select query on `financial_data` table.


note: This is just a mock application, that only fetches Apple, Google and IBM stock price.

### task 2 
1. The the web application is expected to be run from docker-compose as 
```shell
docker-compose up -d 
```
2. It starts following steps 
 * installing required package
 * save stock data on database (sqlite)
 * launch HTTP server on port 5000 and exposes to localhost 
3. we can access finance_data endpoint and statistics endpoint as follows 
```shell
curl "http://localhost:5000/api/financial_data?start_date=2022-01-01&end_date=2023-09-01&symbol=GOOG&page=1&limit=10"
curl "http://localhost:5000/api/statistics?start_date=2022-01-01&end_date=2023-09-01&symbol=GOOG"
```

### how to change the api_key and sql endpoint based on the environment 
* Confidential properties are possessed from properties directory, in local we can use the temporal API key and sqlite.
* If it is production environment, you should set up "environment variable" and confidential properties in config-prod.properties file as follows.
  * API_KEY for Alpha Vantage's api key
  * SQL_CONFIG for SQL backend such as `mysql://user:password@hostname:port/dbname`
* In production envionment you should set `environment=prod` when running docker-compose and mount appropriate config-prod.properties under `/usr/src/app/properties` on docker's hostside   




### Required libraries.
* flask 
  * Provide a HTTP server's function to process requests.
* requests
  * Handle http request for accessing AlphaVantage  API
* sqlalchemy
  * ORM mapper to handling database operation.
* jproperties
  * external library to handle properties
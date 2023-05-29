from flask import Flask, request, jsonify
from sqlalchemy import create_engine

from financial.database import Database
from financial.http_server import DatabaseProxy

app = Flask(__name__)
httpserver = DatabaseProxy(create_engine("sqlite:///data.db/"))

@app.route("/api/statistics")
def statistics():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    symbol = request.args.get('symbol')
    return jsonify(httpserver.aggregate_query(symbol=symbol, date_from=start_date, date_to=end_date))

@app.route("/api/financial_data")
def financial_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    symbol = request.args.get('symbol')
    limit = int(request.args.get('limit'))
    page = int(request.args.get('page'))
    return jsonify(httpserver.select_query(
        symbol=symbol,
        date_from=start_date,
        date_to=end_date,
        limit_number=limit,
        page_number=page
    ))

if __name__ == '__main__':
    engine = create_engine("sqlite:///data.db")
    app.run()

from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine

from financial.http_server import DatabaseProxy

app = Flask(__name__)
httpserver = DatabaseProxy(create_engine("sqlite:///data.db/"))

@app.route("/api/statistics")
def statistics():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    symbol = request.args.get('symbol')
    if None in (start_date, end_date, symbol):
        return make_response(jsonify({"error": "unsatisfied query"}), 400)

    return jsonify(httpserver.aggregate_query(symbol=symbol, date_from=start_date, date_to=end_date))

@app.route("/api/financial_data")
def financial_data():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    symbol = request.args.get('symbol')
    limit_str = request.args.get('limit')
    page_str = request.args.get('page')
    if None in (start_date, end_date, symbol, limit_str, page_str):
        return make_response(jsonify({"error": "unsatisfied query"}), 400)
    return jsonify(httpserver.select_query(
        symbol=symbol,
        date_from=start_date,
        date_to=end_date,
        limit_number=int(limit_str),
        page_number=int(page_str) - 1
    ))

if __name__ == '__main__':
    engine = create_engine("sqlite:///data.db")
    app.run(host="0.0.0.0",port=5000)

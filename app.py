from flask import Flask, abort, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import mysql.connector
import json
import sqlite3
import os
app = Flask(__name__, static_folder='./dist/static', template_folder='./dist')
db = sqlite3.connect('frappe.db', check_same_thread=False)
cursor = db.cursor()
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/getProducts', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM products")
    res = cursor.fetchall()
    response = []
    for product in res:
        response.append(
            {"id": product[0], "name": product[1], "category": product[2]})

    return jsonify(response)


@app.route('/addProduct', methods=['POST'])
def add_product():
    req = request.get_json()
    cursor.execute("INSERT INTO products(pname,pcat) VALUES(?,?)",
                   (req["name"], req["category"]))
    db.commit()
    return get_products()


@app.route('/editProduct', methods=['POST'])
def edit_product():
    req = request.get_json()
    cursor.execute("UPDATE products SET pname=?, pcat=? where pid=?",
                   (req["name"], req["category"], req["id"]))
    db.commit()
    return get_products()


@app.route('/delProduct', methods=['POST'])
def del_product():
    req = request.get_json()
    cursor.execute("DELETE FROM prod_mov WHERE pid = ?", (req["id"],))
    cursor.execute("DELETE FROM products WHERE pid = ?", (req["id"],))
    db.commit()
    return get_products()


@app.route('/getLocations', methods=['GET'])
def get_locations():
    cursor.execute("SELECT * FROM locations")
    res = cursor.fetchall()
    response = []
    for location in res:
        response.append(
            {"id": location[0], "name": location[1]})
    return jsonify(response)


@app.route('/addLocation', methods=['POST'])
def add_location():
    req = request.get_json()
    cursor.execute("INSERT INTO locations(l_name) VALUES(?)",
                   (req["name"], ))
    db.commit()
    return get_locations()


@app.route('/editLocation', methods=['POST'])
def edit_location():
    req = request.get_json()
    cursor.execute("UPDATE locations SET l_name = ? WHERE loc_id = ?",
                   (req["name"], req["id"]))
    db.commit()
    return get_locations()


@app.route('/delLocation', methods=['POST'])
def del_location():
    req = request.get_json()

    cursor.execute("DELETE FROM locations WHERE loc_id = ?", (req["id"],))
    db.commit()
    return get_locations()


@app.route('/movements/getProducts', methods=['GET'])
def get_prod_loc(location=-1):
    req_type = location
    if location == -1:
        req = request.get_json()
        location = request.args.get("location")
    imports = "(SELECT SUM(pmi.quant) FROM prod_mov AS pmi WHERE pmo.to_loc=pmi.to_loc AND pmi.pid = pmo.pid) AS im"

    exports = "(SELECT SUM(pmi.quant) FROM prod_mov AS pmi WHERE pmo.to_loc=pmi.from_loc AND pmi.pid = pmo.pid) AS exp"

    query = """select report.pname ,report.pid, report.im,report.exp,sum(report.im -ifnull(report.exp,0) ) as bal 
                        from (SELECT p.pname as pname, pmo.pid as pid,{im},{exp} 
                        FROM prod_mov AS pmo, products AS p 
                        WHERE pmo.pid = p.pid AND pmo.to_loc=? GROUP BY pmo.to_loc, pmo.pid) as report
                        group by pid  """.format(im=imports, exp=exports)
    cursor.execute(query, (location,))
    res = cursor.fetchall()

    response = []
    for pm in res:
        if pm[4] > 0:
            response.append({"id": pm[1], "name": pm[0],
                             "Qty": str(pm[4]), "loc": location})
    if req_type == -1:
        return jsonify(response)
    else:
        return response


@app.route('/movements/import', methods=['POST'])
@app.route('/movements/export', methods=['POST'])
@app.route('/movements/move', methods=['POST'])
def moves():
    req = request.get_json()
    values = (req["pid"], req["quant"])
    names = "timestamp,pid,quant"
    inputs = "current_timestamp,?,?"
    cur_loc = req["cur_loc"]

    if req["type"] == "import":
        names += ",to_loc"
        values = values + (req["to_loc"],)
        inputs += ",?"

    elif req["type"] == "export":
        names += ",from_loc"
        values = values+(req["from_loc"],)
        inputs += ",?"
    else:
        names += ",to_loc,from_loc"
        values = values+(req["to_loc"], req["from_loc"])
        inputs += ",?,?"

    insert = "insert into prod_mov({fields}) values({inputfields})".format(
        fields=names, inputfields=inputs)

    cursor.execute(insert, values)
    db.commit()
    cursor.execute("select * from prod_mov ")
    return jsonify(get_prod_loc(cur_loc))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

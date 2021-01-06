from flask import Flask, abort, request, jsonify

from flask_cors import CORS, cross_origin
import mysql.connector
from cred import pw
import json
app = Flask(__name__)
app.config['pw'] = pw
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pw,
    database="frappe",
)
cursor = db.cursor(buffered=True)

CORS(app)




@app.route('/getProducts', methods=['GET'])
def getProducts():
    cursor.execute("SELECT * FROM products")
    res = cursor.fetchall()
    db.commit()
    response = []
    for product in res:
        response.append(
            {"id": product[0], "name": product[1], "category": product[2]})
    
    return jsonify(response)
@app.route('/addProduct', methods=['POST'])
def addProduct():
    req = request.get_json()
    print(req)
    cursor.execute("INSERT INTO products(pname,pcat) VALUES(%s,%s)",
(req["name"], req["category"]))
    db.commit()
    return getProducts()

@app.route('/editProduct', methods=['POST'])
def editProduct():
    req = request.get_json()
    print(req)
    cursor.execute("UPDATE products SET pname=%s, pcat=%s where pid=%s",
                   (req["name"], req["category"], req["id"]))
    db.commit()
    return getProducts()
@app.route('/delProduct', methods=['POST'])
def delProduct():
    req=request.get_json()
    cursor.execute("DELETE FROM prod_mov WHERE pid = %s", (req["id"],))
    cursor.execute("DELETE FROM products WHERE pid = %s", (req["id"],))
    db.commit()
    return getProducts()


@app.route('/getLocations', methods=['GET'])
def getLocations():
    cursor.execute("SELECT * FROM locations")
    res = cursor.fetchall()
    db.commit()
    response = []
    for location in res:
        response.append(
            {"id": location[0], "name": location[1]})
    
    return jsonify(response)

@app.route('/addLocation', methods=['POST'])
def addLocation():
    req = request.get_json()
    cursor.execute("INSERT INTO locations(l_name) VALUES(%s)",
                   (req["name"], ))
    db.commit()
    return getLocations()

@app.route('/editLocation', methods=['POST'])
def editLocation():
    req = request.get_json()
    cursor.execute("UPDATE locations SET l_name = %s WHERE loc_id = %s",
                   (req["name"], req["id"]))
    db.commit()
    return getLocations()

@app.route('/delLocation', methods=['POST'])
def delLocation():
    req = request.get_json()
    cursor.execute("DELETE FROM prod_mov WHERE to_loc = %s", (req["id"],))
    cursor.execute("DELETE FROM locations WHERE loc_id = %s", (req["id"],))
    db.commit()
    return getLocations()

@app.route('/movements/getProducts', methods=['POST'])
def getprodloc(location=-1):
    req_type = location
    if location ==-1:
        req = request.get_json()
        location = req["location"]
    
    cursor.execute("select test.pname ,test.pid, test.im,test.exp,sum(test.im -ifnull(test.exp,0) )as bal from (SELECT p.pname as pname, pmo.pid as pid, (SELECT SUM(pmi.quant) FROM prod_mov AS pmi WHERE pmo.to_loc=pmi.to_loc AND pmi.pid = pmo.pid) AS im , (SELECT SUM(pmi.quant) FROM prod_mov AS pmi WHERE pmo.to_loc=pmi.from_loc AND pmi.pid = pmo.pid) AS exp FROM prod_mov AS pmo, products AS p WHERE pmo.pid = p.pid AND pmo.to_loc=%s GROUP BY pmo.to_loc, pmo.pid) as test group by pid ",(location,))
    res = cursor.fetchall()
    db.commit()
    print(res)
    
    response=[]
    for pm in res:
        response.append({"id":pm[1],"name":pm[0],"Qty":str(pm[4]),"loc":location})
    if req_type == -1:
        return jsonify(response)
    else:
        return response
@app.route('/movements/import', methods=['POST'])
@app.route('/movements/export', methods=['POST'])
@app.route('/movements/move', methods=['POST'])
def moves():
    req=request.get_json()
    print(req)
    values=(req["pid"],req["quant"])
    names="pid,quant"
    inputs="%s,%s"
    # location = req["to_loc"] if "to_loc" in req else req["from_loc"]
    cur_loc=req["cur_loc"]
    

    if req["type"]=="import":
        names+=",to_loc"
        values = values + (req["to_loc"],)
        inputs+=",%s"
    
    elif req["type"]=="export":
        names+=",from_loc"
        values=values+(req["from_loc"],)
        inputs+=",%s"
    else:
        names+=",to_loc,from_loc"
        values=values+( req["to_loc"], req["from_loc"])
        inputs+=",%s,%s"
        
        
     
    
    insert = "insert into prod_mov({fields}) values({inputfields})".format(fields=names,inputfields=inputs)
    print(insert)
    cursor.execute(insert,values)
    db.commit()
    return jsonify(getprodloc(cur_loc))



if __name__ == '__main__':
    app.run(debug=True)
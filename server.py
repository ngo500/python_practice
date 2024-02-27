from flask import Flask, make_response, request
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]#data

@app.route('/')
def index():
    """
    default route- return Hello World HTML
    returns:
    200: always, HTML
    """
    return "<p> Hello World! </p>"
    #return {"message" : "Hello World Dictionary!"}
    #return jsonify(message = "Hello World JSONify!")

@app.route('/no_content')
def no_content():
    """
    no content route- return tuple with JSON message No content found
    returns:
    204: always, json
    """
    return ({"message": "No content found"}, 204)

@app.route('/exp')
def index_explicit():
    """
    explicit route- return Hello World HTML and status
    returns:
    200: always, json
    """
    resp = make_response({"message" : "<p> Hello World! </p>"})
    resp.status_code = 200
    return resp

@app.route('/data')
def get_data():
    """
    data route- checks if there is any data given
    returns:
    200: returns message with data length found
    404: if NameError occurs
    500: if no data is found
    """
    try:
        if data and len(data) > 0:
            return {"message" : f"Data with length {len(data)} was found!"}
        else:
            return {"message" : "No data found!"}, 500
    except NameError:
        return {"message" : "No data found!"}, 404

@app.route('/name_search')
def name_search():
    """
    name search route- checks if the person is found in the data based on first name
    returns:
    200: person found
    404: person not found
    422: argument is missing
    """
    query = request.args.get("q")

    if not query:
        return {"message" : "Invalid input parameter!"}, 422

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    return {"message" : "Person not found!"}, 404

@app.route('/count', methods=['GET'])
def count():
    """
    GET count, returns count of how many data exist
    returns:
    200: count of data found
    500: data not defined error
    """
    try:
        return {"data count" : len(data)}, 200
    except NameError:
        return {"message" : "Error- Data not defined!"}, 500

@app.route('/person/<uuid:id>', methods=['GET'])
def find_by_uuid(id):
    """
    GET person based on ID, return person if found
    returns:
    200: person found
    404: person not found error
    """
    for person in data:
        if person["id"] == str(id):
            return person, 200
    return {"message" : "Error- ID not found!"}, 404

@app.route('/person/<uuid:id>', methods=['DELETE'])
def delete_by_uuid(id):
    """
    DELETE person based on ID, return message stating if deleted
    returns:
    200: person found and deleted
    404: person not found, no delete
    """
    for person in data:
        if person["id"] == str(id):
            data.remove(person)
            return {"message" : str(id)}, 200
    return {"message" : "Error- Person not found!"}, 404
  

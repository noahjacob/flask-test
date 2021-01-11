# Inventory Management System



## Table of Contents
* [About](#about)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Authors](#authors)
* [Screenshots](#screenshots)




## About
* A basic inventory management system that displays products and store locations and can perform operations like add, update. 
* It keeps a track of prodcuts at different locations based on the prodcut movement logs and displays the current amount.
* It also lets the user do operations like Import, Export and Transfer products from different locations.

### Built With

- [MySQL](https://dev.mysql.com/doc/) - Database
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Backend 
- [VueJs](https://vuejs.org/v2/guide/) - Web Framework
- [Vuetify](https://vuetifyjs.com/en/getting-started/installation/) - Material UI 




## Getting Started
These instructions will help you get a copy of this project up and running on your local machine for development purposes.

### Prerequisites
All the things you need before installation.

* Install [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) 

* Install VueJs
```
npm install -g @vue/cli
```
* Install Python and Flask
```
pip3 install Flask
```

### Installation
Step-by-step instruction to help you get your development enviroment running on localhost.

1. Clone the repo
```
git clone https://github.com/noahjacob/flask-test.git
```
2. Install Flask Dependencies
```
pip3 install flask-cors
```
3. Enter your MySQL database credentials in `server.py` to connect to the database `or` Use the sql dumps of the database.
```py
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pw,
    database="frappe",
)
```

4. Getting the Flask server running
```bat
cd flask-test
python3 server.py
```
5. Installing Vue dependencies
```bat
cd flask-test
npm install
```
6. Compiles and hot-reloads for development
```
npm run serve
```
7. Compiles and minifies for production
```
npm run build
```
8. Lints and fixes files
```
npm run lint
```
[Back To The Top](#table-of-contents)

## Authors
- [Noah Jacob](https://github.com/noahjacob)

## Screenshots
### Products
<br/>

![Products](/screenshots/products.png)
<br/>

![prod_dialog](/screenshots/prods.png)

### Locations
![locations](/screenshots/locations.png)

<br/>

![edit_loc](/screenshots/edit_loc.png)

<br/>

![delete](/screenshots/del.png)

<br/>

### Importing Products
![idia](/screenshots/import.png)
<br/>

### Exporting Products
![edia](/screenshots/export.png)
<br/>

### Transferring Products
![mdia](/screenshots/transfer.png)

[Back To The Top](#table-of-contents)

---




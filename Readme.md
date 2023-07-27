# Simple E-commerce App using FASTAPI

This is a simple E-commerce app built using the FASTAPI framework. The app allows you to perform CRUD operations on items and manage inventory.

## Features

- View all items in the inventory.
- View details of a specific item.
- Create a new item.
- Update an existing item.
- Delete an item.
- Manage inventory by adjusting the quantity of items.


The app will be accessible at `http://localhost:8000`.

### API Endpoints

The following API endpoints are available:

- `GET /items`: Retrieves all items in the inventory.
- `GET /items/{item_id}`: Retrieves details of a specific item.
- `POST /items`: Creates a new item in the inventory.
- `PUT /items/{item_id}`: Updates an existing item in the inventory.
- `DELETE /items/{item_id}`: Deletes an item from the inventory.
- `POST /manage_inventory`: Manages inventory by adjusting the quantity of items.

#### POST /items

Creates a new item in the inventory.

Request Body:
json
{
  "name": "New Item",
  "price": 15.99,
  "qty": 3
}

PUT /items/{item_id}
Updates an existing item in the inventory.

Request Body:

json

{
  "name": "Updated Item",
  "price": 25.99,
  "qty": 8
}

POST /manage_inventory
Manages inventory by adjusting the quantity of items.

Request Body:

json

[
  {
    "item_id": 1,
    "qty": -2
  },
  {
    "item_id": 2,
    "qty": 5
  }
]

-Data Storage
The app uses an in-memory database for simplicity. The items are stored as dictionaries with the following properties:

item_id: Unique identifier for the item.
name: Name of the item.
price: Price of the item.
qty: Quantity of the item in stock.

Note: This app uses a local Database since I was told I don't have to build a DB server when I asked about this on Cuvette.

-Dependencies
The following dependencies are used in this project:

fastapi: Web framework for building APIs with Python.
uvicorn: ASGI server to run the application.
pydantic: Data validation and serialization library.
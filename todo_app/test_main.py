from fastapi.testclient import TestClient

from todo_app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post(
        "/items/",
        json={"title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Foo Bar",
        "status": False,
        "description": "The Foo Barters"
    }


def test_read_item():
    response = client.get("/all")
    assert response.status_code == 200

    assert response.json() == [{
        "id": 1,
        "title": "Foo Bar",
        "status": False,
        "description": "The Foo Barters"
    }]

def test_get_existing_item():
    response = client.get(
        "/item/1",

    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Foo Bar",
        "status": False,
        "description": "The Foo Barters"
    }

def test_get_existing_item_bad_id():
    response = client.get("/item/5")
    assert response.status_code == 400
    assert response.json() == {"detail": "No item found with the id"}

def test_get_item_status_false():
    response = client.get(
        "/items/False"
    )
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Foo Bar",
        "status": False,
        "description": "The Foo Barters"
    }]


def test_update_item_status():
    data = {
        "id": 1,
        "title": "Foo Bar",
        "status": True,
        "description": "The Foo Barters"
    }
    response = client.put(
        "/items",
        json=data,
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Foo Bar",
        "status": True,
        "description": "The Foo Barters"
    }

def test_get_item_status_true():
    response = client.get("/items/True")
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "title": "Foo Bar",
        "status": True,
        "description": "The Foo Barters"
    }]

def test_item_delete():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"Success": "Todo with id 1 deleted"}

def test_item_delete_wrong():
    response = client.delete("/items/2")
    assert response.status_code == 400
    assert response.json() == {"detail": "Todo with this id 2 was not found"}

def test_read_empty():
    response = client.get("/all")
    assert response.status_code == 200
    assert response.json() == []

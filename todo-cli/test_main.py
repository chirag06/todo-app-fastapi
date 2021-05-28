import pytest
from todo_cli.models import My_funtions
import json


obj_req = My_funtions()
create_task = {
    "id": 1,
    "title": "Foo Bar",
    "status": False,
    "description": "The Foo Barters"
}

updated_task = {
    "id": 1,
    "title": "Foo Bar",
    "status": True,
    "description": "The Foo Barters"
}

def test_add():
    res = obj_req.add("Foo Bar", "The Foo Barters")
    assert res.status_code == 200
    assert res.json() == create_task

def test_show():
    res = obj_req.show(1)
    assert res.status_code == 200
    assert res.json() == create_task

def test_done():
    res = obj_req.done(1)
    assert res.status_code == 200
    assert res.json() == updated_task

def test_status():
    res = obj_req.tasks_status(1)
    assert res.status_code == 200
    assert res.json() == [updated_task]

def test_status_not_done():
    res = obj_req.tasks_status(0)
    assert res.status_code == 200
    assert res.json() == []

def test_all():
    res = obj_req.all()
    assert res.status_code == 200
    assert res.json() == [updated_task]

def test_update():
    update_key = "description"
    update_value = "Hello World!"
    res = obj_req.update(1,"description", "Hello World!")
    json_obj = updated_task
    json_obj[update_key] = update_value
    assert res.status_code == 200
    assert res.json() == json_obj

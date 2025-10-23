import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


client = app.test_client()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_add_todo():
    r = client.post("/add", json={"task": "Learn DevOps"})
    assert r.status_code == 201
    assert b"Task added" in r.data

def test_toggle_todo():
    client.post("/add", json={"task": "Toggle Me"})
    r = client.post("/toggle/0")
    assert r.status_code == 200

def test_bad_toggle():
    r = client.post("/toggle/999")
    assert r.status_code == 404

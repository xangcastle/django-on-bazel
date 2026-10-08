import json

import pytest


def test_health_reports_hermetic_interpreter(client):
    body = client.get("/health/").json()

    assert body["status"] == "ok"
    assert body["python"].startswith("3.12.")
    assert ".venv/bin/python" in body["executable"]


@pytest.mark.django_db
def test_create_then_list(client):
    created = client.post("/notes/", data=json.dumps({"title": "first"}), content_type="application/json")
    assert created.status_code == 201

    listed = client.get("/notes/").json()
    assert [note["title"] for note in listed["notes"]] == ["first"]


@pytest.mark.django_db
def test_rejects_bad_body(client):
    assert client.post("/notes/", data="nope", content_type="application/json").status_code == 400

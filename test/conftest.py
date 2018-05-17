from __future__ import print_function
import pytest
import db

@pytest.fixture(scope="session", params=db.testdb_params())
def db_server(request):
    server = db.create_server(request.param)
    request.addfinalizer(server.delete)
    return server

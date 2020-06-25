import json
from django.test import TestCase

from linked_connections.views import LinkedConnections


class TestLinkedConnections(TestCase):
    def setUp(self) -> None:
        self.client.get("/initialize/", {"numUsers": 15})

    def test_get_all_connections(self):
        response = self.client.get("/connections/?page=1&pageSize=10")
        connections = json.loads(bytes(response._container[0]).decode('utf-8'))
        assert len(connections["connections"]) == 10

        response = self.client.get("/connections/?page=2&pageSize=10")
        connections = json.loads(bytes(response._container[0]).decode('utf-8'))
        assert len(connections["connections"]) == 5

    def test_get_user_connections(self):
        test_connection = LinkedConnections.users[1]
        response = self.client.get("/userConnections/?userId=1")
        connections = json.loads(bytes(response._container[0]).decode('utf-8'))
        assert len(test_connection.connected_user_ids) == len(connections["connections"])

    def test_get_connections_by_name(self):
        test_connection = LinkedConnections.users[1]
        for name in [test_connection.first_name, test_connection.last_name]:
            response = self.client.get(f"/connectionByNameLocation/?name={name}")
            connections = json.loads(bytes(response._container[0]).decode('utf-8'))
            found_connection = False
            for con in connections["connections"]:
                if con["name"] == f'{test_connection.first_name} {test_connection.last_name}':
                    found_connection = True
                    break
            if not found_connection:
                raise Exception("connection by name not found")

    def test_get_connections_by_location(self):
        test_connection = LinkedConnections.users[1]
        response = self.client.get(f"/connectionByNameLocation/?location={test_connection.location}")
        connections = json.loads(bytes(response._container[0]).decode('utf-8'))
        found_connection = False
        for con in connections["connections"]:
            if con["location"] == test_connection.location:
                found_connection = True
                break
        if not found_connection:
            raise Exception("connection by location not found")


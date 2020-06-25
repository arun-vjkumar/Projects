import json
import random
from typing import List

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from faker import Faker

fake = Faker('en_IN')


class User:
    def __init__(self, user_id: int, first_name: str, last_name: str, location: str, connected_user_ids: List[int]):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.connected_user_ids = connected_user_ids

    def add_connections(self, user_ids: List[int]):
        self.connected_user_ids.extend(user_ids)

    @staticmethod
    def to_dict(user: 'User') -> dict:
        return {
            "userId": user.user_id,
            "name": f'{user.first_name} {user.last_name}',
            "location": user.location
        }


class LinkedConnections:
    users: dict = {}

    @classmethod
    def initialize_data(cls, request: WSGIRequest) -> HttpResponse:
        num_users = int(request.GET["numUsers"])
        for i in range(1, num_users):
            names = fake.name().split(" ")
            first_name, last_name = " ".join(names[0:-1]), names[-1]
            LinkedConnections.users[i] = User(user_id=i,
                                              first_name=first_name,
                                              last_name=last_name,
                                              location=fake.city(),
                                              connected_user_ids=[])

        for user in cls.users.values():
            connection_user_id = random.randint(1, num_users - 1)
            if connection_user_id != user.user_id:
                user.add_connections([connection_user_id])
                cls.users[connection_user_id].add_connections([user.user_id])
        return HttpResponse(content="initialized successfully", status=201)

    @classmethod
    def get_all_connections(cls, request: WSGIRequest) -> HttpResponse:
        page = int(request.GET["page"])
        num_connections = int(request.GET["pageSize"])
        users = list(cls.users.values())
        sorted(users, key=lambda user: user.user_id)
        start_index = (page - 1) * num_connections
        end_index = start_index + num_connections
        if start_index >= len(users):
            start_index = len(users) - 1
        if end_index >= len(users):
            end_index = len(users) - 1

        print(start_index, end_index)
        return HttpResponse(
            content=json.dumps({"connections": [user for user in users[start_index: end_index]]}, default=User.to_dict),
            content_type="application/json"
        )

    @classmethod
    def get_user_connections(cls, request: WSGIRequest) -> HttpResponse:
        user_id = int(request.GET["userId"])
        user = cls.users[user_id]
        connections = []
        for _id in user.connected_user_ids:
            connections.append(cls.users[_id])

        return HttpResponse(
            content=json.dumps({"connections": connections}, default=User.to_dict),
            content_type="application/json"
        )

    @classmethod
    def get_connections_by_name_loc(cls, request: WSGIRequest) -> HttpResponse:
        location = str(request.GET.get("location"))
        name = str(request.GET.get("name"))
        connections = []
        for user in cls.users.values():
            if location and user.location.lower() == location.lower() or \
                    name and name.lower() in [user.first_name.lower(), user.last_name.lower()]:
                connections.append(user)
        return HttpResponse(
            content=json.dumps({"connections": connections}, default=User.to_dict),
            content_type="application/json"
        )

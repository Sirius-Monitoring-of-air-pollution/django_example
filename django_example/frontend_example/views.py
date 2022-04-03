from django.shortcuts import render
from ninja import NinjaAPI, Schema

api = NinjaAPI()


class AddScheme(Schema):
    a: int
    b: int


@api.post('/add')
def add(request, data: AddScheme):
    return {"result": data.a + data.b}

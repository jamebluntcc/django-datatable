#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render
from tables import PersonTable, ScheduleTable

class Foo(object):
    def __init__(self, id, name, calendar):
        self.id = id
        self.name = name
        self.calendar = calendar


def base(request):
    people = PersonTable()
    return render(request, "index.html", {'people': people})

def edit(request, id):
    pass

def calendar_column(request):
    data = [Foo(1, 'A', [1,2,3,4,5,6]), Foo(2, 'B', [1,2,3,4,5,6]), Foo(3, 'C', [1,2,3,4,5,6])]
    table = ScheduleTable(data)
    return render(request, "index.html", {'people': table})

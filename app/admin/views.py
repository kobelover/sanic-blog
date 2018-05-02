#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import admin
from sanic.response import json


@admin.route('/', methods=["GET", "POST"])
async def admin_helloworld(request):
    return json({'hello': 'admin '})



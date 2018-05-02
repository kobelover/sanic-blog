#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import front
from sanic.response import json


@front.route('/', methods=["GET", "POST"])
async def admin_helloworld(request):
    return json({'hello': 'front '})



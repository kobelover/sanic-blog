#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic import Sanic

app = Sanic(__name__)


from app.front import front as front_blueprint
from app.admin import admin as admin_blueprint

app.blueprint(front_blueprint, url_prefix='/')
app.blueprint(admin_blueprint, url_prefix='/admin')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
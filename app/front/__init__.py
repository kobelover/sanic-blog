#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic import Blueprint

front = Blueprint("front", __name__)

import app.front.views
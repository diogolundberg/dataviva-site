# -*- coding: utf-8 -*-
import urllib2
import json
from datetime import datetime
from itertools import groupby
from sqlalchemy import func
from flask import Blueprint, request, render_template, g, Response, make_response, send_file, jsonify, redirect, url_for

from dataviva import db, __year_range__
from dataviva.apps.general.views import get_locale
from dataviva.utils.make_query import make_query
from dataviva.apps.account.models import User, Starred
from dataviva.apps.graphs.models import UI
from dataviva.api.rais.models import Yb_rais, Yi, Yo
from dataviva.api.secex.models import Ymb, Ymp, Ymw
from dataviva.api.hedu.models import Yu, Yc_hedu
from dataviva.api.sc.models import Yc_sc
from dataviva.api.attrs.models import Yb

import json

mod = Blueprint('rankings', __name__,
                template_folder='templates',
                url_prefix='/<lang_code>/rankings',
                static_folder='static')

@mod.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', get_locale())

@mod.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.locale = values.pop('lang_code')

@mod.route('/')
def index():
    return render_template('rankings/index.html', body_class='rankings')

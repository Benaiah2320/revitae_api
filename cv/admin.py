from django.contrib import admin
from .models import *

models = [Resume, WorkHistory, PositionDetail, Skill]

for model in models:
    admin.site.register(model)

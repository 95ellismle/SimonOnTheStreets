import django_tables2 as tables
from .models import ServiceUser

class PersonTable(tables.Table):
    class Meta:
        model = ServiceUser
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

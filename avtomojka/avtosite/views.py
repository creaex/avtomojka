import datetime

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def index(request):
    chas = [{'chas': 10},
            {'chas': 11},
            {'chas': 12},
            {'chas': 13},
            {'chas': 14},
            {'chas': 15},
            {'chas': 16},
            {'chas': 17},
            {'chas': 18},
            {'chas': 19},
            {'chas': 20},
            {'chas': 21},
            ]
    now = datetime.datetime.now()
    now1 = now.strftime('%d.%m.%Y')
    tomorrow = now + datetime.timedelta(days=1)
    tim = tomorrow.strftime('%d.%m.%Y')
    NH = now.strftime('%H')
    return render(request, "avtosite/index.html", {"now": now, "tim": tim, "NH": int(NH), "chas": chas, "now1": now1})


class Home(ListView):
    template_name = "avtosite/index.html"
    tim = "datetime.datetime.today()"

    def get_context_data(self, *, object_list=None, **kwargs):
        return self.get_context_data(**kwargs)

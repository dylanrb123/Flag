import datetime
from django.shortcuts import render
from .models import FlagHalfMastInfo

# Create your views here.


def main(request):
    return render(request, 'index.html', {'answer': 'YES', 'reason': 'TESTING'})



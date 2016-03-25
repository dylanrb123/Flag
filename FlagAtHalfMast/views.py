import datetime
from django.shortcuts import render
from .models import FlagHalfMastInfo

# Create your views here.


def main(request):
    test = FlagHalfMastInfo(start_date=datetime.date.today(), end_date=datetime.date.today(), reason="TESTING")
    test.save()
    return render(request, 'index.html', {'answer': 'YES', 'reason': 'TESTING'})



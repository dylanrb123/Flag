import datetime
from django.shortcuts import render
from .models import FlagHalfMastInfo

# Create your views here.


def main(request):
    latest_info = FlagHalfMastInfo.objects.last()
    half_mast = latest_info.end_date >= datetime.datetime.now().date() >= latest_info.start_date
    if half_mast:
        ans = 'Yes'
        reas = latest_info.reason
    else:
        ans = 'No'
        reas = ""
    return render(request, 'index.html', {'answer': ans, 'reason': reas})



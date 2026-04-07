from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import PLC_Tags


# Create your views here.
def index(request):
    tags = PLC_Tags.objects.all().order_by("timestamp")
    return render(request, 'database_manager/index.html', {"tags": tags})
# Get Coils By Timestamp
def coil_detail(request, pk):
    tag = get_object_or_404(PLC_Tags, pk=pk, reg_type=0)
    return render(request, "database_manager/detail.html", {"tag": tag})
# Get Holding Registers By Timestamp
def holding_register_detail(request, pk):
    tag = get_object_or_404(PLC_Tags, pk=pk, reg_type=1)
    return render(request, "database_manager/detail.html", {"tag": tag})


# def coil_details(request):
#     coil_tags = get_object_or_404(PLC_Tags, pk=id)
#     return render(request, "database_manager/tag_details.html",{
#         "reg_type" : coil_tags.reg_type,
#         "coil_data" : coil_tags.data,
#         "timestamp" : coil_tags.timestamp
#     })
# def hr_details(request):
#     pass
    
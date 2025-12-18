from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

# Http response
def sample(request):
    name=request.GET.get("name","nandu")
    return HttpResponse(f"Hello {name} this is http response")

#Json response
# generating places information
def sample2(request):
    place=request.GET.get('place',"Hyderabad")
    distance=int(request.GET.get('distance',10))
    famous=request.GET.get('famous',"Chai")
    if distance>=1000:
        suggestion="ivanni ayyepanulu kadhu le"
    elif distance<1000 and distance>500:
        suggestion="kastapadithe vellochu" 
    else:
        suggestion="dabbulu sampadinchaka thirugu"
    placeinfo={"place":place,"distance":distance,"famous":famous,"suggestion":suggestion}
    return JsonResponse({"message":"success","data":placeinfo})


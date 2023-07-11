from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# from django.template import loader
# Create your views here.
# def showJan(request):
#   return HttpResponse('came to this page')

# def showFeb(request):
#   return HttpResponse('feb page')

# def some(request):
#   print(request)
#   return HttpResponse('on dynamic page')

monthly_challanges = {
    "jan": "Jan is starting month of year",
    "feb": "Feb is coldest month of year",
    "mar": "Mar is hottest month of year",
    "april": "April has warmest month of year",
    "may": None
}
    
def index(request):
    months = list(monthly_challanges.keys())
    return render(request,"challanges/index.html", {
        "months": months
    })
    
def monthly_challanges_by_number(request, month):
    months_list = list(monthly_challanges.keys())

    if (month > len(months_list)):
        return HttpResponseNotFound('This month is not valid')

    month_name = months_list[month-1]
    redirect_path = reverse('month-challange', args=[month_name])  # /challenges
    return HttpResponseRedirect(redirect_path)
  

def monthly_challange(request, month):
    try:
        month_text = monthly_challanges[month]
        return render(request, "challanges/challange.html", {
            "month_name":month,
            "description":month_text
        })       
    except:
        # return HttpResponseNotFound("This month is not supported")
        raise Http404()


# def index(request):
#     months = list(monthly_challanges.keys())
#     list_items = ""

#     for month in months:
#         capitilized_month = month.capitalize()
#         month_path = reverse('month-challange', args=[month])
#         list_items += f"<li><a href='{month_path}'>{capitilized_month}</a></li>"

#     list_html = f"<ul>{list_items}</ul>"
#     return HttpResponse(list_html)


# def monthly_challange(request, month):
    # try:
        # textResponse = monthly_challanges[month]
        # htmlReponse = f"<h1>{textResponse}</h1>" # to create and send html
        #  template = loader.get_template("challanges/index.html")
        #  return HttpResponse(template.render())
        # return render(request, 'challanges/index.html')       
    # except:
        # return HttpResponseNotFound("This month is not supported")

    # if(month == "jan"):
    #   return HttpResponse("This is jan month")
    # elif (month == "feb"):
    #   return HttpResponse("This is feb month")
    # elif (month == "mar"):
    #   return HttpResponse("This is mar month")
    # else:
        # print(request)
        # return HttpResponseNotFound("This is not a valid month")

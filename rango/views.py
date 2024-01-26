from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    
    return render(request, 'rango/index.html', context=context_dict)


def about(request):

    link_to_index = '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page." + link_to_index)





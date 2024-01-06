from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Entry

def home(request):
    return render(request, "home.html")

def show(request):
    data = Entry.objects.all()
    return render(request, "show.html",{'data':data})

def send(request):
    if request.method == 'POST':
        ID = request.POST.get('id')  # Use different variable names for data1 and data2
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')

        # Ensure all necessary data is available
        if ID and data1 and data2:
            Entry.objects.create(ID=ID, data1=data1, data2=data2)
            msg = "Data stored successfully"
            return render(request, "home.html", {'msg': msg})
        else:
            msg = "Missing data in the request!"
            return render(request, "home.html", {'msg': msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID = ID).delete()
    return HttpResponseRedirect("show")
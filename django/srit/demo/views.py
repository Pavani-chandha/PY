from django.shortcuts import render

def home(request):
    name="Pavani"
    return render(request, 'home.html',{'name':name})
def about(request):
    return render(request, 'about.html')
def contact(request):
    name=request.GET.get('name')
    return render(request,'home.html',{'name':name})
def json_data(request):
    data={'name':'pavani'}
    return JsonResponse(data)
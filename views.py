from django.shortcuts import render

def feecollection(request):
  return render(request,'finance/feecollection.html')
def feeduesreport(request):
  return render(request,'finance/feeduesreport.html')
def feecollectionreport(request):
  return render(request,'finance/feecollectionreport.html')

 
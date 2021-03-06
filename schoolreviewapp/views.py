from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import HttpResponseRedirect, reverse


import datetime

from .models import School, SchoolImage

class SchoolsView(ListView):
    # this is a must in ListView, it tells what model you want to use
    model = School
    template_name = 'schools/school_list.html'
    ordering = ['name']
    paginate_by = 2
   
    # contect_object_name
    # queryset = Product.objects.filter(name__contains='playstation')

class SchoolDetailView(DetailView):
    model = School
    template_name = 'schools/school_detail.html'

    def post(self, request):
        id = request.POST.get("school")
        print(id)

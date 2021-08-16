from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Record, Review
from django.urls import reverse

# Create your views here.

# GET
class Home(TemplateView):
    template_name = 'home.html'

# GET
class About(TemplateView):
    template_name = 'about.html'

# GET
class RecordList(TemplateView):
    template_name = 'record_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["records"] = Record.objects.filter(name__icontains=name)
            context["header"] = f"Results for {name}"
        else:
            context["records"] = Record.objects.all()
            context["header"] = "Trending Artists"
        
        return context

# GET POST
class RecordCreate(CreateView):
    model = Record
    fields = ['name', 'image', 'year', 'artist']
    template_name = 'record_create.html'
    
    def get_success_url(self):
        return reverse('record_detail', kwargs={'pk': self.object.pk})

class RecordDetail(DetailView):
    model = Record
    template_name = 'record_detail.html'

class RecordUpdate(UpdateView):
    model = Record
    fields = ['name', 'image', 'year', 'artist']
    template_name = 'record_update.html'
    
    def get_success_url(self):
        return reverse('record_detail', kwargs={'pk': self.object.pk})

class RecordDelete(DeleteView):
    model = Record
    template_name = "record_delete_confirmation.html"
    success_url = "/records/"

class ReviewCreate(View):

    def post(self, request, pk):
        review = request.POST.get('review')
        record = Record.objects.get(pk=pk)
        Review.objects.create(review=review, record=record)
        return redirect('record_detail', pk=pk)


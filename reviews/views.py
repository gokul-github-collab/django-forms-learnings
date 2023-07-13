from typing import Any, Dict

from django.db.models.query import QuerySet
from .models import Review
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from .models import Review
# Create your views here.


class ReviewView(CreateView):
    model = Review
    # fields = "__all__"
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewListView(ListView):
    template_name = 'reviews/review_list.html'
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self) -> QuerySet[Any]:
    #     query = super().get_queryset()
    #     data = query.filter(rating__gt=4)
    #     return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

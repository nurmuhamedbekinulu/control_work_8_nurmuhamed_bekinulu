from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from webapp.models import Product, Review
from webapp.forms import ReviewForm



class ReviewCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'review_create.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)



class ReviewDetail(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'review.html'
    model = Review


class ReviewUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'review_update.html'
    form_class = ReviewForm
    model = Review

    def get_success_url(self):
        return reverse('review_detail', kwargs={'pk': self.object.pk})


class ReviewDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('index')

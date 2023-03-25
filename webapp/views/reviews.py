from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, CreateView, UpdateView, ListView

from webapp.models import Product, Review
from webapp.forms import ReviewForm



class ReviewCreateView(CreateView):
    template_name = 'review_create.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        return redirect('product_detail', pk=product.pk)


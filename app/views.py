from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum

from .models import Product
from .forms import AddProductForm, LessProductForm
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        """
        Gets the total units  of inventory
        """
        qty = Product.objects.aggregate(Sum('quantity'))
        qty = qty['quantity__sum']

        if qty == None:
            qty = "No Inventory"

        """
        Gets the dollar value  of inventory
        """
        products = Product.objects.all()
        x = 0
        for p in products:
            x += p.price * p.quantity
        x = "$" + format(x, ',.2f')
        context = {'total': qty, 'amount': x}
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ('name', 'product_id', 'price', 'quantity')
    success_url = reverse_lazy('home')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

def inventory_add(request, pk):
    template_name = 'product_add.html'
    product = get_object_or_404(Product, pk=pk)
    form = AddProductForm
    if request.method == 'POST':
        form = form(request.POST)

        if form.is_valid():
            product.add_inventory(form.cleaned_data['quantity'], form.cleaned_data['price'])

            return HttpResponseRedirect(reverse('product_list'))

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'product_add.html', context)

def inventory_remove(request, pk):
    template_name = 'product_remove.html'
    product = get_object_or_404(Product, pk=pk)
    form = LessProductForm
    if request.method == 'POST':
        form = form(request.POST)

        if form.is_valid():
            product.remove_inventory(form.cleaned_data['quantity'])

            return HttpResponseRedirect(reverse('product_list'))

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'product_remove.html', context)

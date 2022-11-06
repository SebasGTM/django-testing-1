from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product
# Create your views here.


def product_list_view(request):
     objlist = Product.objects.all()
     context = {
          "object_list" :  objlist
     }
     return render(request, "products/list.html", context)

def product_delete_view(request, id):

     obj = get_object_or_404(Product, id=id)
     if request.method == "POST":
          obj.delete()
          return redirect("/productlist")

     context = {
          "object" : obj
     }
     return render(request, "products/delete.html", context)

def dynamic_lookup_view(request, id):
     # obj = Product.objects.get(id=my_id)
     # obj = get_object_or_404(Product, id=my_id)
     try: 
          obj = Product.objects.get(id=id)
     except Product.DoesNotExist:
          raise Http404

     context = {
          "object" : obj
     }
     return render(request, "products/detail.html", context)


def product_create_view(request):
     my_form = RawProductForm()
     if request.method == "POST":
          my_form = RawProductForm(request.POST)
          if my_form.is_valid():
               print(my_form.cleaned_data)
               Product.objects.create(**my_form.cleaned_data)
          else:
               print(my_form.errors)

     context = {
          "form" : my_form
     }
     return render(request, "products/create.html", context)

"""     form = ProductForm(request.POST or None)
    if form.is_valid():
          form.save()
          form = ProductForm()

    context = {
         'form' : form
    }
    return render(request, "products/create.html", context) """



def product_detail_view(request):
    obj = Product.objects.get(id=3)
    context = {
         'Prod_1' : obj
    }
    return render(request, "products/detail.html", context)
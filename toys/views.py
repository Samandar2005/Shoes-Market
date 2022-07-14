from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'user-profile.html')


def order(request):
    return render(request, 'order.html')


def shoes_add(request):
    bks = Shoes.objects.all()
    context = {'shoes': bks}
    return render(request, 'shoes-base.html', context=context)


def shoes(request):
    bks = Shoes.objects.all()
    context = {'shoes': bks}
    return render(request, 'shoes.html', context=context)


def index(request):
    bks = Shoes.objects.all()
    context = {'shoes': bks}
    return render(request, "index.html", context=context)


class BrandListView(ListView):
    template_name = 'brand.html'
    context_object_name = 'brand'

    def get_queryset(self):
        url_data = self.request.GET
        q = Brand.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class BrandCreateView(CreateView):
    queryset = Brand.objects.all()
    template_name = 'brand-add.html'
    fields = "__all__"

    success_url = '/brand'


class BrandUpdateView(UpdateView):
    queryset = Brand.objects.all()
    template_name = 'brand-add.html'
    fields = "__all__"
    success_url = '/brand'


class BrandDeleteView(DeleteView):
    queryset = Brand.objects.all()
    template_name = 'brand-delete-confirmation.html'
    fields = "__all__"

    success_url = '/brand'


class CompanyListView(ListView):
    template_name = 'company.html'
    context_object_name = 'company'

    def get_queryset(self):
        url_data = self.request.GET
        q = Company.objects.all()

        if 'title' in url_data and url_data['title']:
            q = q.filter(title__icontains=url_data['title'])
        if 'workers' in url_data and url_data['workers']:
            q = q.filter(workers__icontains=url_data['workers'])
        if 'annual_income' in url_data and url_data['annual_income']:
            q = q.filter(annual_income__icontains=url_data['annual_income'])
        return q


class CompanyCreateView(CreateView):
    queryset = Company.objects.all()
    template_name = 'company-add.html'
    fields = "__all__"

    success_url = '/company'


class CompanyUpdateView(UpdateView):
    queryset = Company.objects.all()
    template_name = 'company-add.html'
    fields = "__all__"
    success_url = '/company'


class CompanyDeleteView(DeleteView):
    queryset = Company.objects.all()
    template_name = 'company-delete.html'
    fields = "__all__"

    success_url = '/company'


class CompoundListView(ListView):
    template_name = 'compound.html'
    context_object_name = 'compound'

    def get_queryset(self):
        url_data = self.request.GET
        q = Compound.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class CompoundCreateView(CreateView):
    queryset = Compound.objects.all()
    template_name = 'compound-add.html'
    fields = "__all__"

    success_url = '/compound'


class CompoundUpdateView(UpdateView):
    queryset = Compound.objects.all()
    template_name = 'compound-add.html'
    fields = "__all__"
    success_url = '/compound'


class CompoundDeleteView(DeleteView):
    queryset = Compound.objects.all()
    template_name = 'compound-delete.html'
    fields = "__all__"

    success_url = '/compound'


class MaterialListView(ListView):
    template_name = 'material.html'
    context_object_name = 'material'

    def get_queryset(self):
        url_data = self.request.GET
        q = Material.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class MaterialCreateView(CreateView):
    queryset = Material.objects.all()
    template_name = 'material-add.html'
    fields = "__all__"

    success_url = '/material'


class MaterialUpdateView(UpdateView):
    queryset = Material.objects.all()
    template_name = 'material-add.html'
    fields = "__all__"
    success_url = '/material'


class MaterialDeleteView(DeleteView):
    queryset = Material.objects.all()
    template_name = 'material-delete.html'
    fields = "__all__"

    success_url = '/material'


class ShoesListView(ListView):
    template_name = 'shoes-1.html'
    context_object_name = 'shoes'

    def render_to_response(self, context, ** response_kwargs):
        response = super().render_to_response(context, **response_kwargs)

        for key, val in self.last_user_query.items():
            response.set_cookie(key, val)
        return response

    def get_queryset(self):
        self.last_user_query = {}

        xaridor = Group.objects.get(name='Xaridor')
        if self.request.user.has_perm("can_view_shoes") or xaridor in self.request.user.groups.all():

            url_data = self.request.GET
            if len(list(url_data.items())) == 0:
                url_data = self.request.COOKIES
            q = Shoes.objects.all()
            if 'name' in url_data and url_data['name']:
                q = q.filter(name__icontains=url_data['name'])
                self.last_user_query['name'] = url_data['name']
            if 'brand' in url_data and url_data['brand']:
                q = q.filter(brand__name__icontains=url_data['brand'])
                self.last_user_query['brand'] = url_data['brand']
            if 'company' in url_data and url_data['company']:
                q = q.filter(company__title__icontains=url_data['company'])
                self.last_user_query['company'] = url_data['company']
            if 'color' in url_data and url_data['color']:
                q = q.filter(color__icontains=url_data['color'])
                self.last_user_query['color'] = url_data['color']

            if 'material' in url_data and url_data['material']:
                q = q.filter(material__name__icontains=url_data['material'])
                self.last_user_query['material'] = url_data['material']

            if 'the_size' in url_data and url_data['the_size']:
                q = q.filter(the_size=url_data['the_size'])
                self.last_user_query['the_size'] = url_data['the_size']
            if 'price' in url_data and url_data['price']:
                q = q.filter(price=url_data['price'])
                self.last_user_query['price'] = url_data['price']
            if 'from_date' in url_data and url_data['from_date']:
                q = q.filter(date__gte=url_data['from_date'])
                self.last_user_query['from_date'] = url_data['from_date']
            if 'to_date' in url_data and url_data['to_date']:
                q = q.filter(date__lte=url_data['to_date'])
                self.last_user_query['to_date'] = url_data['to_date']
            return q


class ShoesCreateView(CreateView):
    queryset = Shoes.objects.all()
    template_name = 'shoes-add.html'
    fields = "__all__"

    success_url = '/shoes'


class ShoesUpdateView(UpdateView):
    queryset = Shoes.objects.all()
    template_name = 'shoes-add.html'
    fields = "__all__"

    success_url = '/shoes'


class ShoesDeleteView(DeleteView):
    queryset = Shoes.objects.all()
    template_name = 'shoes-delete.html'
    fields = "__all__"

    success_url = '/shoes'


def collection(request):
    return render(request, "collection.html")


def contact(request):
    return render(request, "contact.html")


def racingboots(request):
    return render(request, "racing.html")


def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='user-login.html', context={'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('main')
            else:
                return render(request, template_name='user-login.html', context={'form': form})


def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterModelForm()

        return render(request, template_name='user-register.html', context={'form': form})
    else:
        form = UserRegisterModelForm(data=request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name='Xaridor'))
            user.save()

            login(request, user)

            return redirect('main')
        else:
            return render(request, template_name='user-register.html', context={'form': form})


class ShoesListViewMain(ListView):
    queryset = Shoes.objects.all()
    template_name = 'shoes_base.html'
    context_object_name = 'shoes'

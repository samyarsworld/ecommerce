from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory

from .filters import OrderFilter

from .decorators import unauthenticated_user, allowed_users, admin_only

from .models import *
from .forms import OrderForm, CutomerForm

@login_required(login_url='login')
@admin_only
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all().order_by('-customer')
    total_orders = orders.count()
    delivered = Order.objects.filter(status='delivered').count()
    pending = Order.objects.filter(status='pending').count()

    context = {'customers': customers,
            'orders': orders,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending
    }

    return render(request, 'website/home.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles='customer')
def userPage(request):
    customer = request.user.customer
    orders = customer.has_ordered.all()
    total_orders = orders.count()
    delivered = orders.filter(status='delivered').count()
    pending = orders.filter(status='pending').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs #queryset

    context = {'customer': customer,
            'orders': orders,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending,
            'myFilter': myFilter
    }
    return render(request, 'website/user.html', context)


@login_required(login_url='login')
@admin_only
def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'website/products.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customerDetail(request, id):

    customer = Customer.objects.get(id=id)
    #orders = Order.objects.get(customer=id) or:
    orders = customer.has_ordered.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs #queryset


    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter
    }
    return render(request, 'website/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createOrder(request, id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=7 )
    customer = Customer.objects.get(id=id)
    #form = OrderForm(initial={'customer': customer})
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)

    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)

        if formset.is_valid():
            formset.customer = id
            formset.save()
            return redirect('home')

    context = {'formset': formset}
    return render(request, 'website/create_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def updateOrder(request, id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # By defining instance you actually grab that record from the table rather than creating a new one
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'website/update_order.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'item': order}
    return render(request, 'website/delete_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def settingView(request):
    form = CutomerForm(instance=request.user.customer)
    if request.method == 'POST':
        # you need to capture the post data and the files that are sent, here images
        form = CutomerForm(request.POST, request.FILES,instance=request.user.customer)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'website/account_setting.html', context)





@unauthenticated_user
def registerView(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #group = Group.objects.get(name='customer')
            #user.groups.add(group)
            #Customer.objects.create(user=user)

            messages.success(request, 'Account was created for ' + username)
        
            return redirect(reverse('login'))
        
        else:
            context = {'form': form}
            return render(request, 'website/register.html', context)

    context = {'form': form}
    return render(request, 'website/register.html', context)

@unauthenticated_user
def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                messages.info(request, 'Username OR password is incorrect')


        return render(request, 'website/login.html')

def logoutView(request):
    logout(request)
    return redirect(reverse('login'))
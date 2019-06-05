from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
import pdb

# Create your views here.
def new(request):
    return render(request, 'orders/new.html')

def create(request):
    currentuser = request.user
    
    if request.method == "POST":
        spicy = request.POST.get('spicy')
        
        sidemenu_var = request.POST.getlist('sidemenu')
        sidemenus=[]
        if '1' in sidemenu_var:
            sidemenus.append('주먹김밥')
        if '2' in sidemenu_var:
            sidemenus.append('계란찜')
            
        str_sidemenus = ', '.join(str(x) for x in sidemenus)
        
        topping_var = request.POST.getlist('topping')
        toppings=[]
        if '1' in topping_var:
            toppings.append('치즈')
        if '2' in topping_var:
            toppings.append('햄(7개)')
        if '3' in topping_var:
            toppings.append('계란(2알)')
        if '4' in topping_var:
            toppings.append('메추리알(5알)')
        if '5' in topping_var:
            toppings.append('떡추가')
        if '6' in topping_var:
            toppings.append('오뎅추가')
        if '7' in topping_var:
            toppings.append('순대(300g)')
        if '8' in topping_var:
            toppings.append('베이컨')
        if '9' in topping_var:
            toppings.append('튀김만두(4개)')
        if '10' in topping_var:
            toppings.append('김말이(3개)')
        if '11' in topping_var:
            toppings.append('야채튀김(1개)')
        if '12' in topping_var:
            toppings.append('순살치킨(5개)')
        if '13' in topping_var:
            toppings.append('치즈스틱(3개)')
        if '14' in topping_var:
            toppings.append('모듬튀김(야채튀김1개+김말이1개+만두2개)')
        if '15' in topping_var:
            toppings.append('우동사리')
        if '16' in topping_var:
            toppings.append('라면사리')
        if '17' in topping_var:
            toppings.append('당면사리')
        if '18' in topping_var:
            toppings.append('중국당면')
        
        str_toppings = ', '.join(str(y) for y in toppings)
        pdb.set_trace()
        
        drink = request.POST.get('drink')
        order = Order.objects.create(spicy=spicy, sidemenus=str_sidemenus, toppings=str_toppings, drink=drink, user=currentuser)
        
    return render(request, 'orders/success.html', {'order': order, 'sidemenus': sidemenus, 'toppings': toppings})


def show(request):
    currentuser = request.user
    orders = Order.objects.filter(user=currentuser).order_by('-id')
    # pdb.set_trace()
    return render(request, 'orders/show.html', {'orders': orders})
    
    
def success(request):
    return render(request, 'orders/success.html')
    

def create_review(request, id):
    order = get_object_or_404(Order, pk=id)
    
    if request.method == "POST":
        currentuser = request.user
        content = request.POST.get('content')
        review = Review(content=content, order=order, user=currentuser)
        review.save()
        
        return redirect('orders:show')
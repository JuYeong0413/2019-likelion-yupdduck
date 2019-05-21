from django.shortcuts import render
# from orders .models import Order

def main(request):
    # orders = Post.objects.all()
    return render(request, 'main.html')
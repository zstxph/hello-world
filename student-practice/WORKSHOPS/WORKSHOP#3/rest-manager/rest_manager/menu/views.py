from django.shortcuts import render, redirect
from .models import MenuItem, Course


# Create your views here.

def index(request): #the index view
    menuItems = menuItem.objects.all() #querying all menu items with the object manager
    courses = Course.objects.all()

    if (request.method == 'POST'): #checking if the request method is POST
        if ("itemAdd" in request.POST): #checking if there is a request to add a menu item

            dish_title = request.POST["itemName"]
            price = request.POST["price"]
            course = request.POST["course"]
            description = request.POST["description"]
            current_menu_item = MenuItem(dish_title=dish_title, price=price, course = Course.objects.get(name-course), description=description)
            current_menu_item.save() #saving the menu item
            return redirect("/") #reloading the page
    
    return render(request, 'index.html', {"menuItems":menuItems, "courses": courses})
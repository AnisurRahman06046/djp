from django.shortcuts import render
from food.forms import ContactForm
from . import models
# Create your views here.
def home(request):
    data = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965"
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923"
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927"
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924"
        },
        {
            "strMeal": "Pate Chinois",
"strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930"
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932"
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804"
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933"
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925"
        }
    ]

    return render(request,'index.html',{'meals':data})



def User(request):
    return render(request,'form.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request,'about.html',{'name':name,'email':email})
    return render(request,'about.html')


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./food/upload/'+ file.name, 'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            print(form.cleaned_data)
            return render(request,'djangoform.html',{'form':form})
    else:
        form = ContactForm()
    return render(request,'djangoform.html',{'form':form})



def Users(request):
    student = models.Student.objects.all()
    return render(request,'users.html',{'data':student})
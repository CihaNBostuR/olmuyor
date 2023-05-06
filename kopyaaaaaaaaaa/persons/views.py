from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import YayinEvi,Sinif,KitapTuru,DersTuru,Kitapismi

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})


# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})


# AJAX for yayinevies
def load_yayinevi(request):
    basimyiliId = request.GET.get('basimyiliId')
    yayinevies = YayinEvi.objects.filter(basimyili=basimyiliId).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'yayinevies': yayinevies})

# AJAX for TYT-AYT
def load_tyt_ayt(request):
    yayineviId = request.GET.get('yayineviId')
    kitaptürü = Sinif.objects.filter(yayinevi=yayineviId).all()
    print(kitaptürü)
    return render(request, 'persons/city_dropdown_list_options.html', {'kitaptürü': kitaptürü})


# AJAX for Deneme-Test
def load_type(request):
    sinifId = request.GET.get('sinifId')
    kitaptürüx = KitapTuru.objects.filter(sinif=sinifId).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'kitaptürüx': kitaptürüx})

# AJAX for Ders
def load_ders(request):
    kitapturuId = request.GET.get('kitapturuId')
    dersturu = DersTuru.objects.filter(kitapturu=kitapturuId).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'dersturu': dersturu})

# AJAX for Ders
def load_isim(request):
    dersturuId = request.GET.get('dersturuId')
    kitapismi = Kitapismi.objects.filter(kitapismi=dersturuId).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'kitapismi': kitapismi})

def load_gethtml(request):
    message = request.GET.get('dersturuId')
    template_name = "persons/kitap{}.html".format(message)
    print(template_name)
    x="kitap{{message}}.html"
    print(x)
    return render(request, template_name,{'message': message})




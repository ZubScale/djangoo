from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from bands.models import Musician, Band, Venue
from .forms import MusicianForm # Asegúrate de crear este archivo primero

# --- VISTAS DE LECTURA (LISTADOS) ---

def musicians(request):
    """Listado de músicos con paginación dinámica."""
    all_musicians = Musician.objects.all().order_by('last_name')
    
    # Actividad: permitir cambiar objetos por página vía URL (?per_page=5)
    per_page = request.GET.get('per_page', 2)
    paginator = Paginator(all_musicians, int(per_page))
    
    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)
    
    return render(request, "musicians.html", {
        'musicians': page.object_list, 
        'page': page
    })

def musician(request, musician_id):
    """Detalle individual de un músico."""
    musician_obj = get_object_or_404(Musician, id=musician_id)
    return render(request, "musician.html", {"musician": musician_obj})

def bands(request):
    """Listado de bandas (Relación Muchos a Muchos)."""
    all_bands = Band.objects.all().order_by('name')
    return render(request, "bands.html", {"bands": all_bands})

def venues(request):
    """Listado de locales y salas (Relación Inversa)."""
    all_venues = Venue.objects.all().order_by('name')
    return render(request, "venues.html", {"venues": all_venues})


# --- VISTAS DE CREACIÓN (FORMULARIOS) ---

def musician_add(request):
    """Formulario para agregar un músico nuevo."""
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musicians') # Redirige al listado tras guardar
    else:
        form = MusicianForm()
    
    return render(request, "musician_add.html", {'form': form})
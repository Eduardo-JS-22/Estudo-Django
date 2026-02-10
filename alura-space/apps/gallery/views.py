from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from apps.gallery.models import Image
from django.contrib import messages
from apps.gallery.forms import ImageForm

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta página.")
        return redirect('login')
    
    images = Image.objects.order_by('-image_date').filter(published=True)
    return render(request, 'gallery/index.html', {'cards': images})

def image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/image.html', {'image': image})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta função.")
        return redirect('login')
    
    images = Image.objects.order_by('-image_date').filter(published=True)
    if 'search' in request.GET:
        search_term = request.GET['search']
        if search_term:
            images = images.filter(description__icontains=search_term)
            return render(request, 'gallery/search.html', {'cards': images, 'search_term': search_term})
    return render(request, 'gallery/search.html')

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta função.")
        return redirect('login')
    
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Imagem cadastrada com sucesso!")
            return redirect('index')
    
    return render(request, 'gallery/new_image.html', {'form': form})

def edit_image(request, image_id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta função.")
        return redirect('login')
    
    # Lógica para editar uma imagem existente (formulário, validação, etc.)
    return HttpResponse(f"Página de edição da imagem {image_id}")

def delete_image(request, image_id):
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para acessar esta função.")
        return redirect('login')
    
    # Lógica para deletar uma imagem existente (confirmação, etc.)
    return HttpResponse(f"Página de confirmação para deletar a imagem {image_id}")
from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.contrib import messages

def index(request):
    img = Image.objects.all()
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('index')
    else:
        form = ImageForm()

    return render(request, 'index.html', {'img': img, 'form': form})

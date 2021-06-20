from django.shortcuts import render
from .models import Album
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm

# Create your views here.
def album_list(request):
    albums = Album.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'albums/post_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/post_detail.html', {'album': album})

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_date = timezone.now()
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/post_edit.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            album.created_date = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/post_edit.html', {'form': form})


def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')

    return render(request, 'albums/post_list.html', {"album": album})
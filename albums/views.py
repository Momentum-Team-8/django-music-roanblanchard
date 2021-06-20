from django.shortcuts import render
from .models import Album
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# Create your views here.
def album_list(request):
    albums = Album.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'albums/post_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/post_detail.html', {'album': album})
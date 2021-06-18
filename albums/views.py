from django.shortcuts import render
from .models import Album
from django.utils import timezone

# Create your views here.
def album_list(request):
    albums = Album.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'albums/post_list.html', {'albums': albums})
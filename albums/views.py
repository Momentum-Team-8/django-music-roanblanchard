from django.shortcuts import render

# Create your views here.
def album_list(request):
    return render(request, 'albums/post_list.html', {})
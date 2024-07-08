from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    if query:
        quotes = Quote.objects.filter(Q(tags__icontains=query))
    else:
        quotes = Quote.objects.none()
    return render(request, 'quotes/search_results.html', {'quotes': quotes})

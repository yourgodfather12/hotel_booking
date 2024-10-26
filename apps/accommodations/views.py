from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Accommodation  # Ensure your model is correct


def home(request):
    accommodations_list = Accommodation.objects.all()
    paginator = Paginator(accommodations_list, 5)  # Display 5 items per page
    page_number = request.GET.get('page')
    accommodations = paginator.get_page(page_number)

    context = {'accommodations': accommodations}
    return render(request, 'accommodations/home.html', context)


def advanced_search(request):
    query = request.GET.get('query', '').strip()
    accommodations = Accommodation.objects.filter(name__icontains=query) if query else Accommodation.objects.none()

    # Adding pagination for search results
    paginator = Paginator(accommodations, 5)  # Display 5 search results per page
    page_number = request.GET.get('page')
    accommodations = paginator.get_page(page_number)

    context = {'accommodations': accommodations, 'query': query}
    return render(request, 'accommodations/advanced_search.html', context)


def recommendations(request):
    recommended_accommodations = Accommodation.objects.filter(rating__gte=4)[:10]  # Filter top recommendations
    context = {'recommended_accommodations': recommended_accommodations}
    return render(request, 'accommodations/recommendations.html', context)


def accommodation_detail(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    context = {'accommodation': accommodation}
    return render(request, 'accommodations/accommodation_detail.html', context)

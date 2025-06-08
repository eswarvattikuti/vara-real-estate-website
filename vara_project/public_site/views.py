from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Import the Property model from the admin_panel app
# Assuming 'admin_panel' is the app name where Property model is defined.
# Adjust if the app_name for Property model is different.
from admin_panel.models import Property

def home_view(request):
    featured_properties = Property.objects.filter(status='FOR_SALE').order_by('-date_added')[:3] # Get latest 3 'For Sale'
    context = {
        'featured_properties': featured_properties
    }
    return render(request, 'index.html', context)

def property_list_view(request):
    property_list_all = Property.objects.filter(status='FOR_SALE').order_by('-date_added')

    paginator = Paginator(property_list_all, 6) # Show 6 properties per page
    page_number = request.GET.get('page')
    try:
        properties = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        properties = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        properties = paginator.page(paginator.num_pages)

    context = {
        'properties': properties, # This will be the paginated list
        'is_paginated': True # To help template decide on showing pagination controls
    }
    return render(request, 'pages/properties.html', context)

def property_detail_view(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id, status='FOR_SALE')
    # We might also want to fetch related properties or other details later.
    context = {
        'property': property_instance
    }
    return render(request, 'pages/property-detail.html', context)

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    # This view will be updated later to handle form submission
    return render(request, 'pages/contact.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse # Added reverse
from .models import Property
from .forms import PropertyForm
from django.contrib import messages # Optional: for user feedback

class AdminLoginView(auth_views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('admin_dashboard_overview')

@login_required(login_url=reverse_lazy('login'))
def dashboard_overview_view(request):
    return render(request, 'index.html')

@login_required(login_url=reverse_lazy('login'))
def property_listings_view(request):
    properties = Property.objects.all() # Fetches all properties
    return render(request, 'pages/listings.html', {'properties': properties})

@login_required(login_url=reverse_lazy('login'))
def manage_inquiries_view(request):
    # Placeholder - not part of this CRUD task
    return render(request, 'pages/inquiries.html')

@login_required(login_url=reverse_lazy('login'))
def add_property_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property added successfully!') # Optional
            return redirect(reverse('admin_property_listings'))
        else:
            messages.error(request, 'Please correct the errors below.') # Optional
    else:
        form = PropertyForm()
    return render(request, 'pages/edit-listing.html', {
        'form': form,
        'form_title': 'Add New Property',
        'form_action_url': reverse('admin_add_property') # URL for the form to post to
    })

@login_required(login_url=reverse_lazy('login'))
def edit_property_view(request, property_id): # property_id is now required
    property_instance = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property updated successfully!') # Optional
            return redirect(reverse('admin_property_listings'))
        else:
            messages.error(request, 'Please correct the errors below.') # Optional
    else:
        form = PropertyForm(instance=property_instance)
    return render(request, 'pages/edit-listing.html', {
        'form': form,
        'form_title': f'Edit Property: {property_instance.title}',
        'form_action_url': reverse('admin_edit_property', args=[property_id])
    })

@login_required(login_url=reverse_lazy('login'))
def delete_property_view(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    if request.method == 'POST': # Ensure deletion is via POST for safety
        property_instance.delete()
        messages.success(request, 'Property deleted successfully!') # Optional
        return redirect(reverse('admin_property_listings'))

    # If GET request, could show a confirmation page.
    # For this implementation, we'll redirect to listings if not POST.
    # A more robust solution would be a confirmation template.
    # Example: return render(request, 'pages/delete_confirm.html', {'property': property_instance})
    messages.warning(request, 'Deletion must be confirmed via POST request.') # Optional
    return redirect(reverse('admin_property_listings'))

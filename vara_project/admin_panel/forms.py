from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title',
            'description',
            'address',
            'price',
            'area_sqft',
            'bedrooms',
            'bathrooms',
            'features',
            'status',
            'main_image', # This will be rendered as a FileInput for uploads
        ]
        # You can customize widgets here if needed, for example:
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'features': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g., Garden, Pool, Security'}),
        }

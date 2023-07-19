from django import forms

from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['owner_name', 'owner_social', 'owner_image', 'owner_review']
        widgets = {
            'owner_review': forms.Textarea(attrs={'rows': 6}),
        }



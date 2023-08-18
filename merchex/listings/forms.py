from django import forms
from . models import Band, Listing


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        # fields = '__all__' # delete this line. Only use to display all the fields in the Model
        exclude = ('active', 'official_homepage')  # add this line


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # fields = '__all__' # delete this line. Only use to display all the fields in the Model
        exclude = ('sold',)  # add this line

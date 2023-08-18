from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Band, Listing
from . forms import ContactUsForm, BandForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)  # we insert this line to get the Band with that id
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  # we update this line to pass the band to the template


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listings_list.html',  {'listings': listings})


def listing_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request,
                  'listings/listings_detail.html',
                  {'listing': listing})


def about(request):
    return render(request, 'listings/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['tendekai50@gmail.com'],
            )
            return redirect('email-sent')  # add this return statement
        # if the form is not valid, we let execution continue to the return
        # statement below, and display the form again (with errors).

    else:
        form = ContactUsForm()  # instantiate a new form here
    return render(request,
                  'listings/contact.html',
                  {'form': form})  # pass that form to the template


def email_sent(request):
    return render(request, 'listings/email-sent.html')


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            band = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'listings/band_add.html',
                  {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            listing = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
                  'listings/listing_add.html',
                  {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})


def listing_update(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        # delete the band from the database
        band.delete()
        # redirect to the bands list
        return redirect('band-list')

        # no need for an `else` here. If it's a GET request, just continue
    return render(request, 'listings/band_delete.html', {'band': band})


def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return redirect('listing-list')

    return render(request, 'listings/listing_delete.html', {'listing': listing})


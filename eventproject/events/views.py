from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue, EventUser
from .forms import VenueForm, EventForm
from django.http import HttpResponse
import csv

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#create pdf for venue
def venue_pdf(request):
    #create Bytestream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    #add some text
    #lines = ["line1", "line2", "line3"]
    venues = Venue.objects.all()

    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")

    #loop
    for line in lines:
        textob.textLine(line)

    #finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    #return
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

#venue csv
def venue_csv(request):
    response  = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    #create a csv writer
    writer = csv.writer(response)

    #designated model
    venues = Venue.objects.all()

    #add column heading to the csv files
    writer.writerow(['Venue Name', 'Venue Address', 'Venue ZIP Code', 'Venue Phone', 'Venue Web', 'Venue Email'])
    
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])
    
 
    return response

#text file generator for venue
def venue_text(request):
    response  = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    lines=[]
    venues = Venue.objects.all()
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')
    
    response.writelines(lines)
    return response

#delete venue
def delete_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect("venue-detail")


#delete event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect("list-events")

#update Event
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form  = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'event': event, 'form':form})



#add event
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else: 
        form = EventForm
        if 'submitted' in request.GET:
            submitted =  True
    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})


#update venue
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form  = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('venue-list')

    return render(request, 'events/update_venue.html', {'venue': venue, 'form':form})

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Events"
    #convert month string to numbers
    month = month.capitalize()#this is to capitalize the first letter of the string
    month_number = list(calendar.month_name).index(month)

    #create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    #create a current year
    now = datetime.now()
    current_year = now.year

    #current time
    time_now = now.strftime('%I:%M %p')



    return render(request, 'events/home.html', {"name": name,
                                            "year":year, 
                                            "month":month, 
                                            'month_number':month_number,
                                            "cal":cal,
                                            'current_year': current_year,
                                            'time_now': time_now
                                            })

#Events List
def all_events(request):
    events = Event.objects.all().order_by('name')
    return render(request, 'events/events_list.html', {'events': events})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else: 
        form = VenueForm
        if 'submitted' in request.GET:
            submitted =  True
    return render(request, 'events/add_venue.html', {'form':form , 'submitted':submitted})


def venue_list(request):
    venue_list = Venue.objects.all().order_by('name')
    return render(request, 'events/venue_page.html', {'venue_list': venue_list })
    
def venue_detail(request, venue_id):
    venue_detail = Venue.objects.get(pk=venue_id)
    return render(request, 'events/venue_detail.html', {'venue_detail':venue_detail})

def search_venue(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html', {'searched':searched, 'venues':venues})
    else:
        return render(request, 'events/search_venue.html', {})
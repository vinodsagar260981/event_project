from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events/', views.all_events, name="list-events"),
    path('add_venue/', views.add_venue, name="add-venue"),
    path('venue_list/', views.venue_list, name="venue-list"),
    path('venue_detail/<venue_id>', views.venue_detail, name="venue-detail"),
    path('search_venue/', views.search_venue, name="search-venue"),
    path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
    path('add_event/', views.add_event, name="add-event"),
    path('update_event/<event_id>', views.update_event, name="update-event"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
    path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
    path('venue_text/', views.venue_text, name="venue-text"),
    path('venue_csv/', views.venue_csv, name="venue-csv"),
    path('venue_pdf/', views.venue_pdf, name="venue-pdf"),
]
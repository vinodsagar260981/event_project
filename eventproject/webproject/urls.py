from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("events.urls")),
    path('members/', include("django.contrib.auth.urls")),
    path('members/', include("members.urls")),
]

#configure admin title
admin.site.site_header = "My Club Admin Page"
admin.site.site_title = "Browser Title"
admin.site.index_title = "Party "
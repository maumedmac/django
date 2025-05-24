#from admin.contrib admin
from django.urls import path,include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('apps.web.urls'))
]
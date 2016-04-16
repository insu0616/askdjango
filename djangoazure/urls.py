
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from blog import views

def hello(request):
    return HttpResponse('''
        <h1>Hello, <a href="http://facebook.com/askdjango/" target="_blank">AskDjango</a></h1>
    ''')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , hello),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


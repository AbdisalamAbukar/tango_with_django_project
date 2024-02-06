from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    # The above maps any URLs starting with rango/ to be handled by rango.
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from rango.models import Category
python_category = Category.objects.get(name="Python")  # Adjust if your category name is different
print(python_category.slug)  # Check if the slug is set
if not python_category.slug:
    python_category.slug = 'python'  # Set an appropriate slug
    python_category.save()

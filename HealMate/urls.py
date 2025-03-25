"""
URL configuration for HealMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Home import views as home_views
from Client import views as clientviews
from Service import views as service_views
from ServiceOrder import views as service_order_views
from Shop import views as shopviews
from User import views as user_view
from Bill import views as bill_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', home_views.showhome, name='home'),
        path('about/', home_views.showabout, name='about'),
        path('client/', clientviews.showCustomer,name='customer'),
        path('Creg/',clientviews.customerRegistration,name='Cregi'),
        path('profile/',clientviews.CustomerProfile,name= 'profile'),
        path('service/',service_views.show_service,name='service'),
        path('order_service/', service_order_views.ConfirmOrder, name='s_order'),
        path('show_product/',shopviews.showproduct,name='product'),
        path('order_product/',shopviews.orderproduct,name='productorder'),
        path('registration/', user_view.user_registration, name='userreg'),
        path('product_bill/', bill_views.ShowProduct_Bill, name='p_bill'),
        path('service_bill/', bill_views.ShowService_Bill, name='s_bill'),
        path('accounts/', include('django.contrib.auth.urls')),
        path('show_product/<int:product_id>', shopviews.showDetails, name='detail_view'),
        path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

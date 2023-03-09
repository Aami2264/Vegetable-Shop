from django.urls import path
from Frontend import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('homepage/', views.homepage, name="homepage"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('contactus/',views.contactus,name="contactus"),
    path('blog/',views.blog,name="blog"),
    path('disprodfrmcat/<itemcatg>',views.disprodfrmcat,name="disprodfrmcat"),
    path('ProdSingle/<int:dataid>', views.ProdSingle, name="ProdSingle"),
    path('Reglogin/',views.Reglogin, name="Reglogin"),
    path('Savecustomer/',views.Savecustomer,name="Savecustomer"),
    path('Customerlogin/',views.Customerlogin,name="Customerlogin"),
    path('Customerlogout/', views.Customerlogout, name="Customerlogout"),
    path('ContactMsg/',views.ContactMsg, name="ContactMsg")
]
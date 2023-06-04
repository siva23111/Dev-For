from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    path("",views.home, name="h"),
    path("tab",views.tab, name="tab"),
    path("tabview/<int:desc>/",views.tabview, name="tabv"),
    path("raise/",views.rais, name="raise"),
    path("register/",views.reg, name="reg"),
    path("Login/",views.log, name="log"),
    path("Logout/",views.logo, name="logo"),
    path("Tableview/",views.tview, name="tav"),
    path("like/<int:pk>", views.likepost, name="likepost"),
    path("about/",views.abt, name="abt"),

]
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("inner_page/", views.inner_page, name="inner-page"),
    path("portfolio_details/", views.portfolio_details, name="portfolio-details")

]
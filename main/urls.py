from django.urls import path
from .views import *

urlpatterns = [
    path('team/', TeamView.as_view(), name='team'),
    path('order/', OrderView.as_view(), name='order'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('faq-type/', FAQTypeView.as_view(), name='faq-inf'),
    path('certificate/', CertificateView.as_view(), name='certificate'),
    path('feedback/', ClientsFeedbackView.as_view(), name='feedback'),
    path('services/', ServiceView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('whyus/', WhyUsView.as_view(), name='whyus'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<str:service_name>/', ProjectsView.as_view(), name='projects-by-service'),
    path('price/', PricePlanView.as_view(), name='price-plan'),
    path('tag/', TagListView.as_view(), name='tag'),
    path('features-list/', FeaturesListView.as_view(), name='features-list'),
    path('service-type/', ServiceTypeListApiView.as_view(), name='service-type-list'),
]

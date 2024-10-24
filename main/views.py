from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Response

from main.filters import ProjectFilter
from .models import *
from main import serializers
from rest_framework import generics


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class SubscribeView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = serializers.SubscriptionSerializer


class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer


class ProjectsView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def get_queryset(self):
        service_name = self.kwargs.get('service_name')
        if service_name:
            return Projects.objects.filter(service__name=service_name)
        return Projects.objects.all()


class ServiceView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceInfoView(generics.ListAPIView):
    queryset = ServiceInfo.objects.all()
    serializer_class = serializers.ServiceInfoSerializer


class ClientsFeedbackView(generics.ListAPIView):
    queryset = ClientsFeedback.objects.all()
    serializer_class = serializers.ClientsFeedbackSerializer


class CertificateView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer


class FAQView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = serializers.FAQSerializer


class FAQTypeView(generics.ListAPIView):
    queryset = FAQType.objects.all()
    serializer_class = serializers.FAQTypeSerializer


class WhyUsView(generics.ListAPIView):
    queryset = WhyUs.objects.all()
    serializer_class = serializers.WhyUsSerializer


class PartnersView(generics.ListAPIView):
    queryset = Partnership.objects.all()
    serializer_class = serializers.PartnerSerializer


class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = serializers.AboutSerializers


class PricePlanView(generics.ListAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = serializers.PricePlanSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class FeaturesListView(generics.ListAPIView):
    queryset = Feature.objects.all()
    serializer_class = serializers.FeaturesSerializer


class ServiceTypeListApiView(generics.ListAPIView):
    serializer_class = serializers.ServiceTypeSerializer
    queryset = ServiceType.objects.all()

from rest_framework import serializers
from .models import *


class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyUs
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en'
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'information_uz', 'information_ru', 'information_en', 'image'
        ]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['id', 'icon', 'link']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'full_name', 'phone_number']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['id', 'image']


class ClientsFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsFeedback
        fields = [
            'id', 'full_name', 'image', 'profession_uz', 'profession_ru', 'profession_en', 'message_uz', 'message_ru',
            'message_en'
        ]


class ServiceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'image', 'description_uz', 'description_ru', 'description_en',
            'services'
        ]


class ServiceSerializer(serializers.ModelSerializer):
    service_info = ServiceInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'title', 'service_info', ]


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id', 'title_uz', 'title_ru', 'title_en']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'id', 'full_name', 'occupation_uz', 'occupation_ru', 'occupation_en', 'image', 'description_uz',
            'description_ru', 'description_en',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'service', 'image', 'link', 'tags'
        ]


class FAQTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQType
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en'
        ]


class FAQSerializer(serializers.ModelSerializer):
    type = FAQTypeSerializer(read_only=True)

    class Meta:
        model = FAQ
        fields = ['id', 'question_uz', 'question_ru', 'question_en', 'answer_uz', 'answer_ru', 'answer_en', 'type']


class OrderSerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'full_name', 'phone_number', 'message', 'services'
        ]


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id', 'title_uz', 'title_ru', 'title_en', 'image', 'description_uz', 'description_ru', 'description_en'
        ]


class PricePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePlan
        fields = ('title', 'limit_date', 'limit_user', 'features', 'price')


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('title', 'tick')

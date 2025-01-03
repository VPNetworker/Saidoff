from django.contrib import admin
from .models import (WhyUs,
                     Certificate,
                     Services,
                     ServiceInfo,
                     SocialMedia,
                     Subscribe,
                     Projects,
                     Team,
                     FAQ,
                     FAQType,
                     Order,
                     Partnership,
                     ClientsFeedback,
                     About,
                     ServiceType,
                     Tag)
from .models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(WhyUs)
class WhyUsAdmin(TranslationAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ('title',)

    class ServiceInfoInline(admin.TabularInline):
        model = ServiceInfo
        extra = 1

    inlines = [ServiceInfoInline]


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'link', 'order')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


@admin.register(ClientsFeedback)
class ClientsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'profession',)
    list_display_links = ('id', 'full_name', 'profession',)
    search_fields = ('full_name', 'profession',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'is_checked',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name', 'phone_number',)
    list_filter = ('is_checked',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'is_checked',)
    list_display_links = ('id', 'full_name',)
    search_fields = ('full_name', 'phone_number',)
    list_filter = ('is_checked',)


@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'occupation', 'order')
    list_display_links = ('id', 'full_name', 'occupation',)
    search_fields = ('full_name',)
    list_filter = ('occupation',)


@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('id', 'type',)
    list_display_links = ('id', 'type',)
    list_filter = ('type',)


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

@admin.register(Feature)
class FeatureAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'tick')
    list_display_links = ('id',)


@admin.register(PricePlan)
class PricePlanAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'price', 'limit_date', 'limit_user')
    list_display_links = ('id',)



class ServiceInline(admin.StackedInline):
    model = Services
    extra = 0


@admin.register(ServiceType)
class ServiceTypeAdmin(TranslationAdmin):
    list_display = ('id', 'title',)
    inlines = [ServiceInline]


admin.site.register(Certificate, TranslationAdmin)
admin.site.register(Partnership)
admin.site.register(SocialMedia)
admin.site.register(FAQType, TranslationAdmin)
admin.site.register(Tag)

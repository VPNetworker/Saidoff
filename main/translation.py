from modeltranslation.translator import TranslationOptions, register
from main import models


@register(models.WhyUs)
class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.Team)
class WhyUsTranslation(TranslationOptions):
    fields = ('occupation', 'description')


@register(models.Certificate)
class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'information')


@register(models.ClientsFeedback)
class WhyUsTranslation(TranslationOptions):
    fields = ('profession', 'message')


@register(models.ServiceInfo)
class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.Services)
class ServicesTranslation(TranslationOptions):
    fields = ('title',)


@register(models.FAQ)
class WhyUsTranslation(TranslationOptions):
    fields = ('question', 'answer')


@register(models.FAQType)
class WhyUsTranslation(TranslationOptions):
    fields = ('title',)


@register(models.About)
class WhyUsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(models.ServiceType)
class ServiceTypeTranslation(TranslationOptions):
    fields = ('title',)


@register(models.Projects)
class ProjectsTranslation(TranslationOptions):
    fields = ('title',)


@register(models.Tag)
class TagTranslation(TranslationOptions):
    fields = ('title',)


@register(models.Feature)
class FeatureTranslation(TranslationOptions):
    fields = ('title',)


@register(models.PricePlan)
class PricePlanTranslation(TranslationOptions):
    fields = ('title',)

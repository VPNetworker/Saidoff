from django.db import models
from django.utils.translation import gettext_lazy as _
from config.settings import DEFAULT_SITE_URL

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class WhyUs(TimeStamp):
    title = models.CharField(_("title"), max_length=212)
    description = models.TextField(_("description"))

    def __str__(self):
        return self.title


class Order(TimeStamp):
    full_name = models.CharField(_("full_name"), max_length=212)
    phone_number = models.CharField(max_length=212)
    is_checked = models.BooleanField(default=False)
    services = models.ForeignKey('Services', on_delete=models.CASCADE)
    message = models.TextField()
    def __str__(self):
        return self.full_name


class Subscribe(TimeStamp):
    full_name = models.CharField(_("full_name"), max_length=212)
    phone_number = models.CharField(max_length=212)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Team(TimeStamp):
    full_name = models.CharField(_("full_name"), max_length=212)
    occupation = models.CharField(max_length=212)
    image = models.ImageField(upload_to='team/')
    description = models.TextField()

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.full_name


class Partnership(TimeStamp):
    image = models.FileField(upload_to='partnership/')

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

class Certificate(TimeStamp):
    title = models.CharField(_("title"), max_length=212)
    information = models.TextField(_("information"))
    image = models.ImageField(upload_to='certificate/')

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.title


class ClientsFeedback(TimeStamp):
    full_name = models.CharField(_("full_name"), max_length=212)
    image = models.ImageField(upload_to='feedback/')
    profession = models.CharField(_("profession"), max_length=212)
    message = models.TextField(_("message"))

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.full_name


class ServiceInfo(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='service/')
    description = models.TextField(_("description"))
    services = models.ForeignKey('Services', on_delete=models.CASCADE, related_name='service_info')

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.title


class Services(TimeStamp):
    title = models.CharField(_("title"), max_length=212)
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return self.title


class ServiceType(TimeStamp):
    title = models.CharField(_("title"), max_length=212)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(_("title"), max_length=125)


class Projects(TimeStamp):
    title = models.CharField(_("title"), max_length=212)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/')
    link = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.title


class SocialMedia(TimeStamp):
    icon = models.ImageField(upload_to='social_media/')
    link = models.URLField(null=True, blank=True)

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.icon}'

class FAQType(TimeStamp):
    title = models.CharField(_("title"), max_length=212)

    def __str__(self):
        return self.title


class FAQ(TimeStamp):
    question = models.TextField(_("question"))
    answer = models.TextField(_("answer"))
    type = models.ForeignKey('FAQType', on_delete=models.CASCADE)


class About(TimeStamp):
    title = models.CharField(_("title"), max_length=212)
    image = models.ImageField(upload_to='about/')
    description = models.TextField(_("description"))

    def get_image(self):
        return f'{DEFAULT_SITE_URL}/{self.image}'

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(_("title"), max_length=125)
    tick = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PricePlan(models.Model):
    title = models.CharField(_("title"), max_length=125)
    price = models.FloatField()
    limit_date = models.CharField(max_length=125)
    limit_user = models.CharField(max_length=125)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.title
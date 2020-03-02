from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _ 
from userena.models import UserenaBaseProfile

class Customer(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='customer',
                                on_delete=models.CASCADE)
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)



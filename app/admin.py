from django.contrib import admin
from .models import User
from .models import ArduinoData
from .models import EMPLOYEES
from .models import ADDDEVICES
# from .models import ck_IP
# from .new import ArduinoDataForm
# from .models import ConsoleData
# Register your models here.
admin.site.register(User)
admin.site.register(ArduinoData)
admin.site.register(EMPLOYEES)
admin.site.register(ADDDEVICES)
# admin.site.register(ArduinoDataForm)
# admin.site.register(ConsoleData)
# admin.site.register(ck_IP)
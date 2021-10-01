from apps.api import models
from apps.web.forms.bootstrap import BootStrapModelForm


class AgreeDepartModelForm(BootStrapModelForm):
    class Meta:
        model = models.Department
        exclude = ['status', ]
        # fields = "__all__"

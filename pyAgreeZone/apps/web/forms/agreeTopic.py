from apps.api import models
from apps.web.forms.bootstrap import BootStrapModelForm


class AgreeTopicModelForm(BootStrapModelForm):
    class Meta:
        model = models.Topic
        exclude = ['count', ]
        # fields = "__all__"

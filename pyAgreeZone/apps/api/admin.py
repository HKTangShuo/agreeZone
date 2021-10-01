from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class pyAgreeZoneModelAdmin(admin.ModelAdmin):

    def cover(self, *args, **kwargs):
        return mark_safe("<a href='{0}'>{0}</a>".format(self.cover))

    list_display = ['title', cover, ]


admin.site.register(models.AgreeMessage, pyAgreeZoneModelAdmin)

#
# class AuctionItemModelAdmin(admin.ModelAdmin):
#     list_display = ['title', 'cover', 'auction', 'status']

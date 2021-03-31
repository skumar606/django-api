from django.contrib import admin
from .models import User
from .models import UserLoginHistory

import csv
from django.http import HttpResponse

# register user model
admin.site.register(User)

# define a function to export selected data as csv
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected"

class UserLoginHistoryAdmin(admin.ModelAdmin):
    actions = [export_as_csv]

# register UserLoginHistory model with UserLoginHistoryAdmin option
admin.site.register(UserLoginHistory, UserLoginHistoryAdmin)
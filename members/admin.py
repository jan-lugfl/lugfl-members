from members.models import Member
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
  list_display = ('aktiv', 'nachname', 'vorname', 'stadt')
  list_display_links = ('nachname', 'vorname')
  list_filter = ['aktiv']
  search_fields = ['vorname', 'nachname']

admin.site.register(Member, MemberAdmin)

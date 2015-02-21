from django.contrib import admin

from landing.models import *


class PageAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TestimonialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
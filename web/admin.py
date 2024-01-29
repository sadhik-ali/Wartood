from django.contrib import admin

from .models import (
    BangaloreStone,
    Category,
    Contact,
    Email,
    Enquiry,
    EnquiryForm,
    Project,
    ServiceImage,
    TandurStone,
    Update,
    kadappaStone,
    BeforeAfter,
    Testimonial,
)

# Register your models here.

admin.site.register(Email)


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    search_fields = ("name", "email", "subject", "message")
    list_filter = ("name", "email", "subject", "message")


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    inlines = [ServiceImageInline]
    list_display = ("admin_photo", "title")
    search_fields = ("icon", "title")
    list_filter = ("icon", "title")


@admin.register(EnquiryForm)
class Enquiry_FormAdmin(admin.ModelAdmin):
    list_display = ("Product", "Name", "Phone", "Message")
    search_fields = ("Product", "Name", "Phone", "Message")
    list_filter = ("Product", "Name", "Phone", "Message")


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("display_image", "service", "title")
    search_fields = ("service", "title")
    list_filter = ("service", "title")


@admin.register(Category)
class Categorydmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)

@admin.register(BeforeAfter)
class BeforeAfterAdmin(admin.ModelAdmin):
    list_display = ("before_image","after_image")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name","image")


@admin.register(TandurStone)
class TandurStonesAdmin(admin.ModelAdmin):
    list_display = (
        "tandur_image",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(kadappaStone)
class kadappaStonesAdmin(admin.ModelAdmin):
    list_display = (
        "kadappa_image",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(BangaloreStone)
class BangaloreStonesAdmin(admin.ModelAdmin):
    list_display = (
        "bangalore_image",
        "name",
    )
    search_fields = ("name",)
    list_filter = ("name",)

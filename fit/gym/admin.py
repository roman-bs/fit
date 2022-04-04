from django.contrib import admin

from gym.models import Gym, Tags, Trainer, Program, Product


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title",)
    search_fields = ("title",)


class TagsAdminInline(admin.TabularInline):
    model = Tags.gyms.through


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("name",)

    inlines = (TagsAdminInline,)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title",)
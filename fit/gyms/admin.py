from django.contrib import admin

from gyms.models import Gym, Tags, Training_program, Diet, Сoach, Сlient


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title",)
    search_fields = ("title",)


class TagsAdminInline(admin.TabularInline):
    model = Tags.gyms.through


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):

    inlines = (TagsAdminInline,)


@admin.register(Training_program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Сoach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Сlient)
class СlientAdmin(admin.ModelAdmin):
    list_display = ("title",)
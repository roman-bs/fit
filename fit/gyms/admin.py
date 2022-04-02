from django.contrib import admin

from gyms.models import Gym, Tags, Diet, Trainer


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title",)
    search_fields = ("title",)


#class TagsAdminInline(admin.TabularInline):
    #model = Tags.gyms.through


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ("title",)

    #inlines = (TagsAdminInline,)


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("title",)

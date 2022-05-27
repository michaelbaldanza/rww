from django.contrib import admin
from .models import MinistryPage, GalleryImage, Post, GuidedMeditation, GuidedMeditationPage, SacredJourney, SpiritualDirection, MinisterialRecord, MainPage, SlideImage, Music, StyleControl

class MinistryPageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'video_caption', 'created_on')
    search_fields = ['heading',]

class MinisterialRecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['firs_name', 'last_name']

class GuidedMeditationAdmin(admin.ModelAdmin):
    list_display = ('title', 'audio_file', 'created_on')
    search_fields = ['title']

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption', 'updated_on', 'created_on')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class SacredJourneyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'destination', 'start_date', 'end_date', 'updated_on', 'status'
        )
    list_filter = ('status',)
    search_fields = ['name', 'destination']
    prepopulated_fields = {'slug': ('name',)}

class SpiritualDirectionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'what_is_spiritual_direction',
        )
    search_fields = [
        'title', 'what_is_spiritual_direction', 'what_do_spiritual_directors_do',
    ]

admin.site.register(StyleControl)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(SlideImage)
admin.site.register(MainPage)
admin.site.register(Music)
admin.site.register(SpiritualDirection, SpiritualDirectionAdmin)
admin.site.register(SacredJourney, SacredJourneyAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(GuidedMeditationPage)
admin.site.register(GuidedMeditation, GuidedMeditationAdmin)
admin.site.register(MinistryPage, MinistryPageAdmin)
admin.site.register(MinisterialRecord, MinisterialRecordAdmin)
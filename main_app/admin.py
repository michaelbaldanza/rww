from django.contrib import admin
from .models import MinistryPage, GalleryImage, Post, GuidedMeditation, GuidedMeditationPage, SacredJourney, SpiritualDirection, MinisterialRecord, MainPage, SlideImage, Music, StyleControl, ArtAndMusicPage, SacredJourneyPage, BlogIndexPage, GlobalPostStyle, StyleSheet, ContactPage

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
    list_display = ('id', 'image', 'caption', 'category', 'updated_on', 'created_on')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class SacredJourneyAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'destination', 'start_date', 'end_date', 'updated_on', 'status'
        )
    list_filter = ('status',)
    search_fields = ['title', 'destination']
    prepopulated_fields = {'slug': ('title',)}

class SpiritualDirectionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'what_is_spiritual_direction',
        )
    search_fields = [
        'title', 'what_is_spiritual_direction', 'what_do_spiritual_directors_do',
    ]

class StyleSheetAdmin(admin.ModelAdmin):
    list_display = ('parent', 'created_on', 'updated_on')

# repeated content
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GuidedMeditation, GuidedMeditationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(SacredJourney, SacredJourneyAdmin)
admin.site.register(SlideImage)

# individual pages
admin.site.register(ArtAndMusicPage)
admin.site.register(BlogIndexPage)
admin.site.register(ContactPage)
admin.site.register(GuidedMeditationPage)
admin.site.register(MainPage)
admin.site.register(MinisterialRecord, MinisterialRecordAdmin)
admin.site.register(MinistryPage, MinistryPageAdmin)
admin.site.register(Music)
admin.site.register(SacredJourneyPage)
admin.site.register(SpiritualDirection, SpiritualDirectionAdmin)

# cross-content styling
admin.site.register(GlobalPostStyle)
admin.site.register(StyleControl)
admin.site.register(StyleSheet, StyleSheetAdmin)
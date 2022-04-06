from django.contrib import admin
from .models import MainPageFragment, MinistryFragment, Photo, Post, Meditation, MainPagePhoto, SacredJourney, MinisterialRecord, MinisterialRecordImage

class MainPageFragmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'content', 'created_on')
    search_fields = ['role', 'content']

class MainPagePhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'status', 'role', 'order', 'hyperlink')
    search_fields = ['role', 'status', 'photo', 'order', 'hyperlink']

class MinistryFragmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'content', 'created_on')
    search_fields = ['role', 'content']

class MinisterialRecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ['firs_name', 'last_name']

class MinisterialRecordImageAdmin(admin.ModelAdmin):
    list_display = ('name_of_file', 'category', 'position', 'updated_on', 'created_on')
    search_fields = ['category']

class MeditationAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'created_on', 'status')
    list_filter = ('status',)
    search_fields = ['title',]

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name_of_file', 'category', 'created_on',)
    search_fields = ['name_of_file',]

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

admin.site.register(SacredJourney, SacredJourneyAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Meditation, MeditationAdmin)
admin.site.register(MainPageFragment, MainPageFragmentAdmin)
admin.site.register(MainPagePhoto, MainPagePhotoAdmin)
admin.site.register(MinistryFragment, MinistryFragmentAdmin)
admin.site.register(MinisterialRecord, MinisterialRecordAdmin)
admin.site.register(MinisterialRecordImage, MinisterialRecordImageAdmin)
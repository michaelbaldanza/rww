from django.contrib import admin
from .models import MainPageFragment, MinistryFragment, Post, Meditation

class MainPageFragmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'content', 'created_on')
    search_fields = ['role', 'content']

class MinistryFragmentAdmin(admin.ModelAdmin):
    list_display = ('role', 'content', 'created_on')
    search_fields = ['role', 'content']

class MeditationAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'status', 'created_on',)
    list_filter = ('status',)
    search_fields = ['title',]

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Meditation, MeditationAdmin)
admin.site.register(MainPageFragment, MainPageFragmentAdmin)
admin.site.register(MinistryFragment, MinistryFragmentAdmin)
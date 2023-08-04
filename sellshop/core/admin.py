from django.contrib import admin
from .models import Author, Blog, Blogcomment, CreativeTeam, GetInTouch, AboutUs, NewsLetter

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_at']
    class Meta:
        model = Author

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'published']
    class Meta:
        model = Blog

@admin.register(Blogcomment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog', 'created_at']
    class Meta:
        model = Blogcomment

@admin.register(CreativeTeam)
class CreativeTeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_at']
    class Meta:
        model = CreativeTeam

@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    class Meta:
        model = GetInTouch

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    class Meta:
        model = AboutUs

@admin.register(NewsLetter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'created_at', 'is_active']
    class Meta:
        model = NewsLetter
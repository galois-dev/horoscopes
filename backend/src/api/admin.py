from django.contrib import admin
from .models import Horoscope, Horoscope_Message, Horoscope_Push_Notification, Astrological_Profile, Tag, User_Subscription

# Register your models here.
@admin.register(Horoscope)
class HoroscopeAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'description',
        'summary',
        'tags',
    )
    list_display = (
        'name',
        'created_at',
        'updated_at',
        'summary',
        'description',
    )
    list_filter = (
        'created_at',
        'created_by',
    )
    

@admin.register(Horoscope_Message)
class Horoscope_MessageAdmin(admin.ModelAdmin):
    fields = (
        'sent_to',
        'horoscope',
        'status',
    )
    list_display = (
        'created_at',
        'sent_to',
        'horoscope',
        'status',
    )
    list_filter = (
        'created_at',
        'sent_to',
        'horoscope',
        'status',
    )
    class Meta:
        ordering = ['-created_at']

@admin.register(Horoscope_Push_Notification)
class Horoscope_Push_NotificationAdmin(admin.ModelAdmin):
    fields = (
        'horoscope',
        'user',
        'scheduled_at',
    )
    list_display = (
        'horoscope',
        'user',
        'created_at',
        'updated_at',
        'scheduled_at',
    )
    list_filter = (
        'horoscope',
        'user',
        'created_at',
        'updated_at',
        'scheduled_at',
    )

@admin.register(Astrological_Profile)
class Astrological_ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'birth_date',
        'birth_time',
        'residence',
        'starsign',
        'planetary_affinity',
    )
    list_display = (
        'user',
        'birth_date',
        'birth_time',
        'residence',
        'starsign',
        'planetary_affinity',
        'updated_at',
        'created_at',
    )
    list_filter = (
        'user',
        'birth_date',
        'birth_time',
        'residence',
        'starsign',
        'planetary_affinity',
        'updated_at',
        'created_at',
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = (
        'name',
    )
    list_display = (
        'name',
        'created_at',
        'updated_at',
        'updated_by',
    )
    list_filter = (
        'name',
        'created_at',
        'updated_at',
        'updated_by',
    )

@admin.register(User_Subscription)
class User_SubscriptionAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'subscription',
        'stripe_subscription_id',
        'stripe_subscription_blob',
    )
    list_display = (
        'user',
        'subscription',
        'created_at',
        'updated_at',
        'stripe_subscription_id',
        'stripe_subscription_blob',
    )
    list_filter = (
        'user',
        'subscription',
        'created_at',
    )
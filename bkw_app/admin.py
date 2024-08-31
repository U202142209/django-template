from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import BkwCourse, BkwUser, BkwSubscription

# 自定义管理后台的标题
admin.site.site_header = "iBeike-数据中心"
admin.site.site_title = "iBeike-数据中心"


@admin.register(BkwCourse)
class BkwCourseAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'number', 'name', 'teacher',
        'time', 'capacity', 'registered_count', 'point',
        'take_end_date', 'drop_end_date'
    )
    search_fields = [
        'id', 'number', 'name', 'teacher',
        'time', 'capacity', 'registered_count', 'point',
        'take_end_date', 'drop_end_date'
    ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(BkwUser)
class BkwUserAdmin(admin.ModelAdmin):
    using = "bkw"
    list_display = ('id', 'unionid', 'created_at')
    search_fields = ['id', 'unionid', ]

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BkwSubscription)
class BkwSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'course_n', 'show_user_link', "show_course_link", 'pushed', 'deleted', "form_id", 'created_at', 'updated_at')
    search_fields = (
        "user__id", "user__unionid",
        "course__id", "course__number", "course__name", "course__teacher",
    )

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def show_user_link(self, obj: BkwSubscription):
        base_url = reverse('admin:schedule_app_scheduleuser_changelist')
        return format_html('<a href="{}?q={}" target="_blank" >{}</a>', base_url, obj.user.id, obj.user.id[0:10])

    def show_course_link(self, obj: BkwSubscription):
        course = obj.course
        base_url = reverse('admin:schedule_app_schedulecourse_changelist')
        return format_html('<a href="{}?q={}" target="_blank" >{}</a>', base_url, course.id, course)

    show_user_link.short_description = "用户"
    show_course_link.short_description = "课程名称"

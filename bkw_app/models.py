from django.db import models


class BkwCourse(models.Model):
    id = models.CharField(max_length=30, primary_key=True, verbose_name='通知单号')
    number = models.CharField(max_length=12, verbose_name='课程编号')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='课程名称')
    teacher = models.CharField(max_length=255, null=True, blank=True, verbose_name='教师')
    time = models.CharField(max_length=255, null=True, blank=True, verbose_name='上课时间')
    capacity = models.IntegerField(null=True, blank=True, verbose_name='课程容量')
    registered_count = models.IntegerField(null=True, blank=True, verbose_name='已选人数')
    point = models.FloatField(null=True, blank=True, verbose_name='学分')
    take_end_date = models.CharField(max_length=20, null=True, blank=True, verbose_name='选课结束日期')
    drop_end_date = models.CharField(max_length=20, null=True, blank=True, verbose_name='退课结束日期')

    def __str__(self):
        return  self.name

    class Meta:
        db_table = 'course'
        unique_together = (('id', 'number'),)
        managed = False
        verbose_name = '数据 / 课程'
        verbose_name_plural = '数据 / 课程'
        app_label = "bkw_app"
        # 按照课程容量升序排列
        ordering = ['capacity']


class BkwInfo(models.Model):
    key = models.CharField(max_length=255, verbose_name='键')
    value = models.CharField(max_length=255, verbose_name='值')

    class Meta:
        app_label = "bkw_app"
        db_table = 'info'
        managed = False
        verbose_name = '信息'
        verbose_name_plural = '信息'


class BkwUser(models.Model):
    id = models.CharField(max_length=32, primary_key=True, verbose_name='Openid')
    unionid = models.CharField(max_length=64, verbose_name='UnionID')
    created_at = models.DateTimeField(null=True, blank=True, verbose_name='创建时间')

    def __str__(self):
        return self.id

    class Meta:
        app_label = "bkw_app"
        db_table = 'user'
        managed = False
        verbose_name = '数据 / 用户'
        verbose_name_plural = '数据 / 用户'
        # 按照 created_at 降序排列
        ordering = ['-created_at']


class BkwSubscription(models.Model):
    user = models.ForeignKey(
        to=BkwUser,
        on_delete=models.RESTRICT,
        related_name='subscriptions',
        to_field='id',
        db_column='user_id', verbose_name='用户ID')
    course = models.ForeignKey(
        to=BkwCourse,
        on_delete=models.RESTRICT,
        related_name='subscriptions',
        to_field='id',
        db_column='course_id', verbose_name='课程ID')
    course_n = models.CharField(max_length=12, verbose_name='课程编号')
    form_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='表单ID')
    pushed = models.BooleanField(default=False, verbose_name='是否已推送')
    deleted = models.BooleanField(default=False, verbose_name='是否已删除')
    # created_at = models.DateTimeField(null=True, blank=True, verbose_name='创建时间')
    created_at = models.DateTimeField(verbose_name='创建时间', primary_key=True)
    updated_at = models.DateTimeField(null=True, blank=True, verbose_name='更新时间')

    class Meta:
        app_label = "bkw_app"
        db_table = 'subscription'
        managed = False
        verbose_name = '数据 / 订阅'
        verbose_name_plural = '数据 / 订阅'

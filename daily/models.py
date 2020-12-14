# from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CitiesCity(models.Model):
    city_code = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    city_name = models.CharField(max_length=50)
    city_level = models.CharField(max_length=50)
    province_code = models.DecimalField(max_digits=20, decimal_places=0)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities_city'
        unique_together = (('province_code', 'city_name', 'city_level'),)


class CitiesCounty(models.Model):
    county_code = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    county_name = models.CharField(max_length=50)
    county_level = models.CharField(max_length=50)
    city_code = models.DecimalField(max_digits=20, decimal_places=0)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities_county'
        unique_together = (('city_code', 'county_name', 'county_level'),)


class CitiesProvince(models.Model):
    province_code = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    province_name = models.CharField(unique=True, max_length=50)
    province_level = models.CharField(max_length=50)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cities_province'
        unique_together = (('province_name', 'province_level'),)


class Comment(models.Model):
    comment_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=50)
    article_id = models.BigIntegerField(blank=True, null=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    relation_table = models.CharField(max_length=255, blank=True, null=True)
    parent_comment_id = models.BigIntegerField(blank=True, null=True)
    parent_comment_user_id = models.BigIntegerField()
    reply_comment_id = models.BigIntegerField(blank=True, null=True)
    reply_comment_user_id = models.BigIntegerField(blank=True, null=True)
    comment_level = models.IntegerField()
    content = models.CharField(max_length=255)
    status_id = models.IntegerField()
    praise_num = models.IntegerField()
    top_status = models.SmallIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'


class Cost(models.Model):
    cost_id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    cost_context = models.CharField(max_length=255)
    cost_money = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost'


class DailyFiles(models.Model):
    file_id = models.BigIntegerField(primary_key=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    file_url = models.CharField(max_length=500, blank=True, null=True)
    file_size = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField()
    updeted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_files'


class Diary(models.Model):
    diary_id = models.BigIntegerField(primary_key=True)
    diary_context = models.TextField(blank=True, null=True)
    diary_html = models.TextField(blank=True, null=True)
    dialy_date = models.DateTimeField(blank=True, null=True)
    mood_type = models.IntegerField(blank=True, null=True)
    mood = models.CharField(max_length=255, blank=True, null=True)
    temperature = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    weather_type = models.IntegerField(blank=True, null=True)
    weather = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.SmallIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diary'


class Event(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    event_context = models.TextField()
    time_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING)
    plan_time = models.DateTimeField(blank=True, null=True)
    remind = models.IntegerField(blank=True, null=True)
    remind_time = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class Label(models.Model):
    label_id = models.BigIntegerField(primary_key=True)
    label_context = models.CharField(max_length=255)
    label_type = models.IntegerField(blank=True, null=True)
    relation_id = models.BigIntegerField(blank=True, null=True)
    relation_table = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'label'


class Learn(models.Model):
    learn_id = models.BigIntegerField(primary_key=True)
    learn_title = models.CharField(max_length=255)
    learn_html = models.TextField(blank=True, null=True)
    learn_context = models.TextField()
    dir = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'learn'


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class SpringScheduledTask(models.Model):
    cron_id = models.IntegerField(primary_key=True)
    cron_key = models.CharField(unique=True, max_length=128)
    cron_expression = models.CharField(max_length=20)
    task_explain = models.CharField(max_length=50)
    status_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spring_scheduled_task'


class TravelNote(models.Model):
    travel_id = models.BigIntegerField(primary_key=True)
    travel_title = models.CharField(max_length=255, blank=True, null=True)
    travel_img = models.BigIntegerField(blank=True, null=True)
    travel_html = models.TextField(blank=True, null=True)
    travel_note = models.TextField()
    user_id = models.BigIntegerField()
    province_code = models.BigIntegerField(blank=True, null=True)
    city_code = models.BigIntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'travel_note'


class UserInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    pwd = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    status_id = models.SmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'

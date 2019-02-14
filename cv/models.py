# cv/models

from django.db import models


class Resume(models.Model):

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=100,
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=100,
    )
    url_name = models.CharField(
        verbose_name='URL Name',
        max_length=30,
        help_text='String to display in URL. Must be unique',
        unique=True
    )
    title = models.CharField(
        verbose_name='Job Title',
        max_length=100,
    )
    city = models.CharField(
        max_length=100,
    )
    state = models.CharField(
        max_length=20,
    )
    zip = models.PositiveSmallIntegerField(
        verbose_name='Zip Code',
    )
    summary = models.TextField(
        help_text='One or two paragraphs summarizing your goals, history, and skills.',
    )
    hook = models.TextField(
        help_text='short blurb or tag line',
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class WorkHistory(models.Model):
    hook = models.TextField(
        help_text='short description of position'
    )
    org_name = models.CharField(
        verbose_name='Organization Name',
        max_length=100,
    )
    org_description = models.CharField(
        verbose_name='Organization Description',
        max_length=200,
    )
    org_city = models.CharField(
        verbose_name='Organization City',
        max_length=100,
    )
    org_state = models.CharField(
        verbose_name='Organization State',
        max_length=100,
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    current = models.BooleanField(
        verbose_name='Current Position',
        default=False,
    )
    end_date = models.DateField(
        verbose_name='End Date',
        null=True,
    )
    title = models.CharField(
        verbose_name='Position Title',
        max_length=200,
    )
    resume = models.ForeignKey(
        to=Resume,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['start_date']
        verbose_name_plural = 'Work Histories'

    def __str__(self):
        return '{} {}'.format(self.org_name, self.title)


class PositionDetail(models.Model):
    position = models.ForeignKey(
        to=WorkHistory,
        on_delete=models.CASCADE,
    )
    sort = models.PositiveSmallIntegerField(
        help_text='order to display entries',
    )
    description = models.TextField(
        help_text='short description of an aspect of the position',
    )

    def __str__(self):
        return '{0:<20}'.format(self.description)

    class Meta:
        ordering = ['sort']
        verbose_name = 'Position Detail'


class Skill(models.Model):
    name = models.CharField(
        verbose_name='Skill',
        max_length=100,
        help_text='One or two word skill name. Try to reuse first.',
    )
    positions = models.ManyToManyField(
        to=WorkHistory,
    )

    def __str__(self):
        return '{}'.format(self.name)


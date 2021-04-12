# Generated by Django 2.2.8 on 2021-02-04 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0025_auto_20210202_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementmergerequirement',
            name='enableGrandTotal',
            field=models.BooleanField(default=False, help_text='Toggle the "Grant Total" field, which will take over the weighted sum total (otherwise, will use weighted sum total) (only needed for the first node)'),
        ),
        migrations.AddField(
            model_name='requirementmergerequirement',
            name='grandTotal',
            field=models.FloatField(default=None, help_text='The grand total points needed from the weighted sum of connected events (only needed for the first node)', null=True),
        ),
        migrations.AddField(
            model_name='requriementevent',
            name='enableTitle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requriementevent',
            name='title',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='requirementmergerequirement',
            name='candidateSemesterActive',
            field=models.ForeignKey(help_text='Candidate semester this Merged Requirement will take place (ignored if it is a connected node)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='coursesemester.Semester'),
        ),
        migrations.AlterField(
            model_name='requirementmergerequirement',
            name='enable',
            field=models.BooleanField(default=False, help_text='Toggle this Merge node (when ON, this will exist as a first node) (Ignored if it is a connected node)'),
        ),
        migrations.AlterField(
            model_name='requirementmergerequirement',
            name='linkedRequirement',
            field=models.ForeignKey(blank=True, help_text='Connect to another Merged Requirement node here (Candidate Semester, Grand Total, and all Enable fields for all connected nodes will be ignored) (A Cycle will make the Grand Total equal Infinite (higher precidence to Grand Total and weighted total sum))', null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidate.RequirementMergeRequirement'),
        ),
    ]
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tasks.priority'),
        ),
    ]
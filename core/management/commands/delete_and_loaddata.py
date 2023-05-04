from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import Article, Author, Category, Tags, Images

#TODO: fix loaddata command, currently filename can't be passed as argument

class Command(BaseCommand):
    help = 'Delete all data and load fresh data'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='Specifies the fixture file to load data from')

    def delete_data(self):
        Article.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()
        Tags.objects.all().delete()
        Images.objects.all().delete()

    def handle(self, *args, **options):
        
        print(args)
        print(options)
        filename = options['filename']
        self.delete_data()
        call_command('loaddata', filename)
        self.stdout.write(self.style.SUCCESS('Successfully deleted data'))
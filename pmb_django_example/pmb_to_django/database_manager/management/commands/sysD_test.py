from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # need to give it this handle [it calls your command script]
    def handle(self, *args, **options):
        self.test_message()
        # you can think of this as your main() function.
        # everything in this method will be executed by Django when your command is ran
        # NOTE: python manange.py sysD_test is how you call the command
        # No other work or setup is required just follow the file structure
    def test_message(self):
        self.stdout.write(self.style.SUCCESS("This Database Update Command Ran Successfully"))
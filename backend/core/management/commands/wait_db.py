from django.core.management.base import BaseCommand
from django.db import OperationalError, connection
from django.db.backends.dummy.base import DatabaseWrapper
import time

connection: DatabaseWrapper = connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db")
        con_db = False

        while not con_db:
            try:
                connection.ensure_connection()
                con_db = True
            except OperationalError:
                self.stdout.write("Database is unavailable, wait 3 sec")
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS("Database is available"))

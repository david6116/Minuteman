"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from datetime import timedelta

from django.core.urlresolvers import reverse
from django.test import TestCase

from minuteman.models import Log, Project, Client, Contractor



class ViewsTest(TestCase):
    fixtures = ['minuteman_tests']

    def test_dashboard(self):

        self.client.login(username='cody', password='cody')
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_project_summary(self):

        self.client.login(username='cody', password='cody')
        response = self.client.get(reverse("project_summary"))
        self.assertEqual(response.status_code, 200)


    def test_project_total(self):

        self.client.login(username='cody', password='cody')
        response = self.client.get(reverse("project_total"))
        self.assertEqual(response.status_code, 200)

class ModelsTests(TestCase):
    fixtures = ['minuteman_tests']

    def test_project_summary(self):

        project = Project.objects.get(id=2)

        self.assertEqual(project.summary(), timedelta(21913, 10860) )
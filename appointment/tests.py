"""Tests for Django project"""
import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .utils import Calendar
from .models import Meeting
from django.contrib.auth.models import User


def create_meeting(subject, description, location, start_time, contact, end_time):
    """For create meeting object"""
    time = timezone.now() + datetime.timedelta(days=start_time)
    time_end = timezone.now() + datetime.timedelta(days=end_time)
    return Meeting.objects.create(subject=subject, description=description, location=location, start_time=time, contact=contact, end_time=time_end)


class MeetingModelTest(TestCase):
    """Tests for Meeting Model."""

    def setUp(self):
        """Set up for test"""
        self.meeting1 = create_meeting("Subject1", "Easy", "BKK", -1, "191", 10)

    def test_str_meeting(self):
        """Test representation of Meeting object"""
        self.assertEqual(str(self.meeting1), "Subject1")

    def test_get_html_url_from_meeting(self):
        """Can get a URL from the Meeting object?"""
        self.assertEqual(self.meeting1.get_html_url, '<a href="/1/detail"> Subject1</a>')

    def test_get_meeting_date(self):
        """Can get the meeting date?"""
        start_time = timezone.now() + datetime.timedelta(days=-1)
        self.assertEqual(self.meeting1.date_meeting(), start_time.strftime('%d %B %Y'))

class IndexViewTest(TestCase):
    """Test for TewMa home page."""

    def test_check_default_home_page(self):
        """If user is not authenticated, show Welcome, AnonymousUser """
        response = self.client.get(reverse('appointment:home_page'))
        self.assertContains(response, "Welcome, AnonymousUser")

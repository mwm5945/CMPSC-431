from django.core.urlresolvers import resolve
from django.test import Client, TestCase


class SupplyLogisticsUrlsTests(TestCase):
    """Test the Supply Logistics urls."""

    def test_requests_pattern_resolves_correct_view(self):
        """Test pattern resolves the correct view."""
        match = resolve('/int/supply-logistics/')
        self.assertEqual(match.func.__name__, 'SupplyLogisticsView')


class SupplyLogisticsViewTests(TestCase):
    """Tests for the Supply Logistics View."""

    fixtures = ['ThonGroupType.json', 'ThonGroup.json', 'ThinkUser.json']

    def test_get_supply_logistics_view_returns_correct_html(self):
        """Test that the get view returns correct html."""
        c = Client()
        c.post('/login/', {'username': 'mqr5228', 'password': 'foobar'})
        response = c.get('/int/supply-logistics/')
        self.assertEqual(response.status_code, 200)

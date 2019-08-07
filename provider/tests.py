from django.test import TestCase
from .models import Provider, ServiceArea
from rest_framework.test import APIClient


class ProviderTest(TestCase):
    """ Test module for Provider model """

    def setUp(self):
        Provider.objects.create(
            name='test', email="test@email.com", language='HINDI',
            currency='INR', phone_number="8989898989")
        Provider.objects.create(
            name='test2', email='test2@email.com', language='ENG',
            currency='USD', phone_number="8989898989")

    def test_get(self):
        client = APIClient()
        request = client.get('/provider/')
        self.assertEqual(request.status_code, 200)

    def test_getOne(self):
        client = APIClient()
        data = Provider.objects.create(
            name='test2', email='test2@email.com', language='ENG',
            currency='USD', phone_number="8989898989")
        p_id = str(data.id)
        url = '/provider/'+p_id+'/'
        request = client.get(url)
        self.assertEqual(request.status_code, 200)

    def test_post(self):
        client = APIClient()
        data = {
              "email": "testput@gmail.com",
              "language": "CANADA ENG",
              "name": "Test Again",
              "phone_number": "999999999",
              "currency": "CAD"
            }
        header = "Content-Type: application/json"
        request = client.post('/provider/', data=data, header=header)
        self.assertEqual(request.status_code, 201)

    def test_delete(self):
        client = APIClient()
        data = Provider.objects.create(
            name='test2', email='test2@email.com', language='ENG',
            currency='USD', phone_number="8989898989")
        p_id = str(data.id)
        url = '/provider/'+p_id+'/'
        request = client.delete(url)
        self.assertEqual(request.status_code, 204)


class ServiceAreaTest(TestCase):
    """ Test module for ServiceArea model """

    def setUp(self):
        provider = Provider.objects.create(
            name='test', email="test@email.com", language='HINDI',
            currency='INR', phone_number="8989898989")
        ServiceArea.objects.create(
            name='test2', provider=provider, area=222,
            mpoly="SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481,\
                   22.13676452636719 11.44839617401166,\
                   22.40043640136718 18.6521004771425,\
                   16.28929138183593 20.26026464944022,\
                   18.28536987304687 15.01177978112481)))", price=8989)

    def test_get(self):
        client = APIClient()
        request = client.get('/service-area/')
        self.assertEqual(request.status_code, 200)

    def test_getOne(self):
        client = APIClient()
        p_id = str(ServiceArea.objects.all()[0].id)
        url = '/service-area/'+p_id+'/'
        request = client.get(url)
        self.assertEqual(request.status_code, 200)

    def test_post(self):
        client = APIClient()
        p_id = str(Provider.objects.all()[0].id)
        data = {"name": 'test2', "provider": "http://127.0.0.1:8000/provider/"+p_id+"/",
                "area": 222, "mpoly": "SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481,\
                   22.13676452636719 11.44839617401166,\
                   22.40043640136718 18.6521004771425,\
                   16.28929138183593 20.26026464944022,\
                   18.28536987304687 15.01177978112481)))", "price": 8989
                }
        header = "Content-Type: application/json"
        request = client.post('/service-area/', data=data, header=header)
        self.assertEqual(request.status_code, 201)


class SearchApiTest(TestCase):
    """ Test module for Search api """

    def setUp(self):
        provider = Provider.objects.create(
            name='test', email="test@email.com", language='HINDI',
            currency='INR', phone_number="8989898989")
        ServiceArea.objects.create(
            name='test2', provider=provider, area=222,
            mpoly="SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481,\
                   22.13676452636719 11.44839617401166,\
                   22.40043640136718 18.6521004771425,\
                   16.28929138183593 20.26026464944022,\
                   18.28536987304687 15.01177978112481)))", price=8989)

        ServiceArea.objects.create(
            name='test2', provider=provider, area=222,
            mpoly="SRID=4326;MULTIPOLYGON (((4.391784667968747 32.62087018318108,\
                    16.88323974609375 29.34267830248893,\
                    26.80664062499999 29.32591746930778,\
                    34.97222900390624 20.80233659297902,\
                    41.90597534179686 9.260713181867553,\
                    45.63720703125 6.019019363914672,\
                    39.85702514648437 -2.071844477055492,\
                    28.96682739257812 -28.54833838763142,\
                    19.51583862304687 -30.47471581151384,\
                    14.62692260742188 -18.00746792135298,\
                    15.35888671875 -6.581395858207814,\
                    10.74600219726563 7.640220359946578,\
                    -9.805297851562491 8.057869896976522,\
                    -13.34701538085937 23.54888092385873,\
                    -4.827117919921863 33.17778985580033,\
                    4.391784667968747 32.62087018318108)))", price=8989)

    def test_serach_api(self):
        client = APIClient()
        url = '/area/?lat=18.28536987304687&lon=15.01177978112481'
        request = client.get(url)
        self.assertEqual(request.status_code, 200)

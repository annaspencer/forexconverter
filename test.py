from app import app
from unittest import TestCase



class ConversionTestCase(TestCase):
    def test_homepage(self):
        # """ tests homepage route """
       with app.test_client() as client:
           res = client.get("/")
           html = res.get_data(as_text=True)

           self.assertEqual(res.status_code, 200)
           self.assertIn('<h1>Forex Currency Converter</h1>', html)


    def test_success_int(self):
        # tests conversion sucess response with int input
        with app.test_client() as client:
            res = client.get("/convert?convert_from=EUR&convert_to=EUR&amount=12")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<div class="alert alert-success" role="alert">', html)

    def test_success_float(self):
        # tests conversion sucess response with float input
        with app.test_client() as client:
            res = client.get("/convert?convert_from=EUR&convert_to=EUR&amount=1.00")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<div class="alert alert-success" role="alert">', html)

    def test_success_float(self):
        # tests conversion sucess response with large float input
        with app.test_client() as client:
            res = client.get("/convert?convert_from=EUR&convert_to=EUR&amount=1.00234444444444433434343434343")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<div class="alert alert-success" role="alert">', html)


    def test_form_redirect(self):
        # tests conversion error response with alpha / symbol character input
        with app.test_client() as client:
            res = client.get("/convert?convert_from=EUR&convert_to=EUR&amount=ABC,0#5 ^&&")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/error')

    def test_form_error_html(self):
        # tests conversion error response html follow redirect
        with app.test_client() as client:
            res = client.get("/convert?convert_from=EUR&convert_to=EUR&amount=ABC,0", follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>Input not valid. Use only numeric values and decimals. Please try again.</p>', html)

    def test_error_route(self):
        # tests error route
        with app.test_client() as client:
           res = client.get("/error")
           html = res.get_data(as_text=True)

           self.assertEqual(res.status_code, 200)
           self.assertIn('<p>Input not valid. Use only numeric values and decimals. Please try again.</p>', html)



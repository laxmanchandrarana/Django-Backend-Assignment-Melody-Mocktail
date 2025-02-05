from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from .models import Redirect

class RedirectAPITests(APITestCase):
    def setUp(self):
        self.redirect1 = Redirect.objects.create(
            title_web="Web Title 1",
            title_phone="Phone Title 1",
            position=2,
            is_active=True,
            availability="both",
            redirect_url_web="http://example.com/web1",
            redirect_url_phone="http://example.com/phone1"
        )
        self.redirect2 = Redirect.objects.create(
            title_web="Web Title 2",
            title_phone="Phone Title 2",
            position=1,
            is_active=False,
            availability="web_only",
            redirect_url_web="http://example.com/web2",
            redirect_url_phone="http://example.com/phone2"
        )

    def test_get_redirects(self):
        """Test retrieving the list of redirects."""
        url = reverse('redirect-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure two objects are returned

    def test_sorting_by_position(self):
        """Test if redirects are sorted by position (ascending)."""
        url = reverse('redirect-list-create') + '?ordering=position'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure redirect2 (position=1) comes before redirect1 (position=2)
        self.assertEqual(response.data[0]['position'], 1)
        self.assertEqual(response.data[1]['position'], 2)

    def generate_test_image(self):
        """Generate a simple image for testing purposes."""
        file = io.BytesIO()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(file, 'JPEG')
        file.name = 'test_image.jpg'
        file.seek(0)
        return file

    def test_upload_images(self):
        """Test uploading valid images for phone and web."""
        url = reverse('redirect-list-create')

        image_phone = SimpleUploadedFile("phone_image.jpg", self.generate_test_image().read(), content_type="image/jpeg")
        image_web = SimpleUploadedFile("web_image.jpg", self.generate_test_image().read(), content_type="image/jpeg")

        data = {
            "title_web": "Image Web",
            "title_phone": "Image Phone",
            "position": 3,
            "is_active": True,
            "availability": "both",
            "redirect_url_web": "http://example.com/image-web",
            "redirect_url_phone": "http://example.com/image-phone",
            "image_phone": image_phone,
            "image_web": image_web
        }

        response = self.client.post(url, data, format='multipart')
        
        # Debugging output to verify response
        print("RESPONSE DATA:", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('image_phone', response.data)
        self.assertIn('image_web', response.data)


    def test_default_ordering_by_position(self):
        """Test that default ordering by position is applied (Meta class)."""
        url = reverse('redirect-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Ensure the first item in response has position=1
        self.assertEqual(response.data[0]['position'], 1)

    def test_toggle_is_active(self):
        """Test toggling the is_active flag."""
        url = reverse('redirect-detail', kwargs={'pk': self.redirect1.pk})
        
        # Deactivate the redirect
        response = self.client.patch(url, {"is_active": False}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify the change
        self.redirect1.refresh_from_db()
        self.assertFalse(self.redirect1.is_active)

    def test_large_dataset_performance(self):
        """Test API performance with a large number of records."""
        # Create 50 redirects to simulate a larger dataset
        for i in range(3, 53):
            Redirect.objects.create(
                title_web=f"Web Title {i}",
                title_phone=f"Phone Title {i}",
                position=i,
                is_active=True,
                availability="both",
                redirect_url_web=f"http://example.com/web{i}",
                redirect_url_phone=f"http://example.com/phone{i}"
            )
        
        url = reverse('redirect-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 52)  # Total records should now be 52

    def test_invalid_availability_value(self):
        """Test that invalid availability values are rejected."""
        url = reverse('redirect-list-create')
        data = {
            "title_web": "Invalid Availability",
            "title_phone": "Invalid Availability Phone",
            "position": 4,
            "is_active": True,
            "availability": "invalid_choice",  # Invalid choice
            "redirect_url_web": "http://example.com/invalid",
            "redirect_url_phone": "http://example.com/invalid-phone"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('availability', response.data)
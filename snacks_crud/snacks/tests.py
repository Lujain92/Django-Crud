from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class SnackTest(TestCase):
    def test_list_view_status(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse('snack')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')



    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test')

        self.snack=Snack.objects.create(
            title='test1',
            desc="mohammad",
            purchaser=self.user 
        )


    def test_str_method(self):
        self.assertEqual(str(self.snack),'test1')    

    def test_detail_view(self):
        url = reverse('detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')


    def test_create_view(self):

        data={
            'title':'test',
            'desc':'lujain',
            'purchaser':self.user.id

         }
        url = reverse('create')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertRedirects(response,reverse('detail',args=[2]))
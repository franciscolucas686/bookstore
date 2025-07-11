from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from product.models.product import Product
from order.models import Order
from order.serializers import OrderSerializer

class OrderSerializerTest(TestCase):
    def setUp(self):
        # Cria usuário para o pedido
        self.user = User.objects.create_user(username="francisco", password="123456")

        # Cria dois produtos
        self.produto1 = Product.objects.create(title="Notebook", price=3000)
        self.produto2 = Product.objects.create(title="Mouse", price=100)

        # Cria um pedido e adiciona os produtos
        self.pedido = Order.objects.create(user=self.user)
        self.pedido.product.set([self.produto1, self.produto2])  # ManyToMany

    def test_serializer_valido(self):
        serializer = OrderSerializer(instance=self.pedido)
        self.assertEqual(serializer.data['total'], 3100)  # 3000 + 100
        self.assertEqual(len(serializer.data['product']), 2)
        self.assertEqual(serializer.data['product'][0]['title'], "Notebook")
        self.assertEqual(serializer.data['product'][1]['title'], "Mouse")

    def test_serializer_retorna_total_corretamente(self):
        serializer = OrderSerializer(instance=self.pedido)
        total_calculado = serializer.data['total']
        self.assertEqual(total_calculado, 3100)

    def test_serializer_vazio(self):
        pedido_vazio = Order.objects.create(user=self.user)
        serializer = OrderSerializer(instance=pedido_vazio)
        self.assertEqual(serializer.data['total'], 0)
        self.assertEqual(len(serializer.data['product']), 0)

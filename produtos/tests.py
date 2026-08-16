from django.test import TestCase

from .models import Produto


class ProdutoModelTest(TestCase):
    def test_criar_produto(self):
        produto = Produto.objects.create(
            nome='SSD 1TB',
            descricao='Armazenamento rápido para PC.',
            preco='499.90',
            estoque=12,
        )

        self.assertEqual(str(produto), 'SSD 1TB')

    def test_view_produtos_exibe_produtos_do_banco(self):
        Produto.objects.create(
            nome='Teclado Mecânico',
            descricao='Teclado com switches azuis.',
            preco='299.99',
            estoque=8,
            imagem='produtos/teclado.jpg',
        )

        response = self.client.get('/produtos/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teclado Mecânico')
        self.assertContains(response, 'R$')
        self.assertContains(response, '/media/produtos/teclado.jpg')

    def test_produto_possui_campo_imagem(self):
        field = Produto._meta.get_field('imagem')

        self.assertEqual(field.name, 'imagem')


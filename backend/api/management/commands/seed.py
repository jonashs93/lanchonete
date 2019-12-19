from django.core.management.base import BaseCommand
from ...models import Ingrediente
from ...models import Lanche


# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_lanches():
    """Deletes all the table data"""
    Lanche.objects.all().delete()

def clear_ingredientes():
    """Deletes all the table data"""
    Ingrediente.objects.all().delete()


def create_ingrediente(nome, valor, alias):
    ingrediente = Ingrediente(
        nome=nome,
        valor=valor,
        alias=alias
    )
    ingrediente.save()
    return ingrediente

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_lanches()
    clear_ingredientes()
    if mode == MODE_CLEAR:
        return

    alface = create_ingrediente("Alface", 0.40, "alface")
    bacon = create_ingrediente("Bacon", 2.00, "bacon")
    hamburguer_carne = create_ingrediente("Hambúrguer de carne", 3.00, "hamburguer_carne")
    ovo = create_ingrediente("Ovo", 0.80, "ovo")
    queijo = create_ingrediente("Queijo", 1.50, "queijo")

    lanche = Lanche(nome="X-Bacon")
    lanche.save()
    lanche.ingredientes.set([bacon, hamburguer_carne, queijo])

    lanche = Lanche(nome="X-Burguer")
    lanche.save()
    lanche.ingredientes.set([hamburguer_carne, queijo])

    lanche = Lanche(nome="X-Egg")
    lanche.save()
    lanche.ingredientes.set([ovo, hamburguer_carne, queijo])

    lanche = Lanche(nome="X-Bacon")
    lanche.save()
    lanche.ingredientes.set([ovo, bacon, hamburguer_carne, queijo])

    lanche = Lanche(nome="Personalizado")
    lanche.save()

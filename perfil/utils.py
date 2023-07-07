from django.db.models import Sum


def calcula_total(obj, campo):
    """
    Recebe um queryset junto com o campo que vai ser somado, e retorna o valor do campo somado.
    """
    total = obj.aggregate(Sum(campo))[f'{campo}__sum']
    return total

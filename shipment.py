# This file is part jasper_reports module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.modules.jasper_reports.jasper import JasperReport

__all__ = ['DeliveryNote']


class DeliveryNote(JasperReport):
    __metaclass__ = PoolMeta
    __name__ = 'stock.shipment.out.delivery_note'

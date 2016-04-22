from __future__ import unicode_literals

from django.db import models


class Buyer(models.Model):
	name = models.CharField(max_length=120)
	vat_tin_no = models.CharField(max_length=12, blank=True)
	invoice_no = models.CharField(max_length=10, blank=True)
	invoice_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	po_no = models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Buyer, self).save(*args, **kwargs)
		self.invoice_no = "IN0000%s" %(self.id) 
		super(Buyer, self).save(*args, **kwargs)

class Measurement(models.Model):
	name = models.CharField(max_length=5)

	def __unicode__(self):
		return self.name

PER = (
	('mg', 'MG'),
	('kg', 'KG'),
	('inch', 'INCH'),
)

class Product(models.Model):
	buyer = models.ForeignKey(Buyer)
	description = models.CharField(max_length=120)
	qty = models.DecimalField(decimal_places=2, max_digits=20)
	per = models.CharField(max_length=120, choices=PER, default='mg')
	rate = models.DecimalField(decimal_places=2, max_digits=20)
	amount = models.DecimalField(decimal_places=2, max_digits=20)

	def __unicode__(self):
		return self.buyer.name







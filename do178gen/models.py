from __future__ import unicode_literals

from django.db import models


class TextBlock(models.Model):
	BLOCKS = (
		('introduction', u"Введение")
	)
	textid = models.CharField(max_length=16, choices=BLOCKS)
	data = models.CharField(max_length=2048)
#	pub_date = models.DateTimeField('date published')


class Config(models.Model):
	BLOCKS = (
		('name', u'Наименование')
		('sign', u'Децимальный номер')
		('copyright', u'Авторские права')
	)
	textid = models.CharField(max_length=16, choices=BLOCKS)
	data = models.CharField(max_length=2048)

class Version(models.Model):
	verid = models.CharField(max_length=16)
	date = models.DateTimeField('date')
	responsible = models.CharField(max_length=32)

class Document(models.Model):
	docid = models.CharField(max_length=16)
	name = models.CharField(max_length=64)
	ref = models.CharField(max_length=32)
	sign = models.CharField(max_length=32)
	#inv = models.CharField(max_length=16)

class Instrument(models.Model):
	TYPES = (
		(1, "Hardware")
		(2, "Software")
		(3, "Verification")
	)
	type = models.IntegerField(choices=BLOCKS)
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=64)
	version = models.CharField(max_length=16)
	function = models.CharField(max_length=64)
	qualified_level = models.CharField(max_length=16)

class Reports(models.Model):
	version = models.ForeignKey('Version')
	date_get = models.DateTimeField('date published')
	date_put = models.DateTimeField('date published')
	performer = models.CharField(max_length=32)
	status = models.CharField(max_length=16)
	life_cycle = models.CharField(max_length=16)
	description = models.CharField(max_length=1024)
	solution = models.CharField(max_length=1024)
	sender = models.CharField(max_length=32)

class QualityAssuranceCheck(models.Model):
	text = models.CharField(max_length=64)

class QualityAssurance(models.Model):
	name = models.CharField(max_length=64)
	input_doc = models.ManyToManyField(Document)
	check = ForeignKey('quality_assurance_check')

class RegistrationDocumentChanges(models.Model):
	doc = ForeignKey('Document')
	version = models.ForeignKey('Version')
	date = models.DateTimeField('date')
	reason = models.CharField(max_length=64)
	description = models.CharField(max_length=64)

class Requirement(models.Model):
	name = models.CharField(max_length=64)
	text = models.CharField(max_length=2048)
	comment = models.CharField(max_length=2048)
	doc = models.CharField(max_length=16)
	mnemonic = models.CharField(max_length=16)
	id_create = models.IntegerFIeld()
	id_modify = models.IntegerFIeld()
	num = models.IntegerFIeld()
	state = models.CharField(max_length=16)
	ready = models.CharField(max_length=16)
	type = models.CharField(max_length=16)
	category = models.CharField(max_length=16)
	level = models.CharField(max_length=1)
	verification = models.CharField(max_length=64)
	stend = models.CharField(max_length=32)
	applicability = models.CharField(max_length=64)
	parrent = ForeignKey('self')
	keywords = models.CharField(max_length=64)
	performance = models.CharField(max_length=64)
	memory = models.CharField(max_length=64)
	TEMPLATES = (
		(1, "Other"),
		(10, "Memory"),
		(11, "Interface")
	)
	template = IntegerField(choices=TEMPLATES)

class TestGroup(models.Model):
	name = models.CharField(max_length=64)

class TestMethod(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=64)
	parametr = models.CharField(max_length=64)
	methodic = models.CharField(max_length=2048)
	condiion = models.CharField(max_length=2048)

class Test(models.Model):
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=1024)
	group = ForeignKey('TestGroup')
	req = models.ManyToManyField('Requirement')
	methods = models.ManyToManyField('TestMethod')

class ValidationValid(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=64)
class ValidationExamination(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=64)
class ValidationAnalysis(models.Model):
	num = models.IntegerField()
	name = models.CharField(max_length=64)

class Validation(models.Model):
	name = models.CharField(max_length=64)
	input_doc = models.ManyToManyField(Document)
	valid = models.ManyToManyField('ValidationValid')
	instruction = models.CharField(max_length=2048)	
	examination = models.ManyToManyField('ValidationExamination')
	analysis = models.ManyToManyField('ValidationAnalysis')



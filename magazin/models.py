from django.db import models
from django.utils import timezone

# Create your models here.

class firstPost (models.Model):
	text = models.TextField (verbose_name = "Текст")
	image = models.ImageField(upload_to = 'media', verbose_name = "Картинка")
	title = models.CharField (max_length = 200, verbose_name = "Заголовок")
	def __str__ (self):
		return self.title

	class Meta:
		verbose_name = "Первая запись"
		verbose_name_plural = "Первые записи"


class secondPost(models.Model):
	text = models.TextField (verbose_name = "Текст")
	image = models.ImageField(upload_to = 'media', verbose_name = "Картинка")
	title = models.CharField (max_length = 200, verbose_name = "Заголовок")
	link = models.CharField (max_length = 200, verbose_name = "Ссылка")
	buttonText = models.CharField (max_length = 30, verbose_name = "Надпись на кнопке")

	def __str__ (self):
		return self.title

	class Meta:
		verbose_name = "Вторая запись"
		verbose_name_plural = "Вторые записи"

class Comments (models.Model):
	name = models.CharField (max_length = 200, verbose_name = "Имя")
	title = models.CharField (max_length = 200, verbose_name = "Тема")
	email = models.EmailField ()
	text = models.TextField ()
	data = models.DateField (default = timezone.now())

	def __str__ (self):
		return (str(self.data)+' ' + str(self.name))

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"

class Order (models.Model):

	deliveryCostDict = {'Самовывоз' : 0,
						'Курьер' : 250,
						'Почта' : -1
						}

	deliveryMethodList = (
		('Самовывоз', 'Самовывоз'),
		('Курьер', 'Доставка курьером'),
		('Почта', 'Доставка почтой'),
	)

	statusList = (
		('Аннулирован', 'Аннулирован'),
		('В обработке', 'В обработке'),
		('Собирается', 'Собирается'),
		('В доставке', 'Отправлен в службу доставки'),
		('В самовывозе', 'Можно забрать из самовывоза'),
		('Выполнен', 'Выполнен'),
	)

	paymentMethodList = (('qiwi', 'Visa QIWI Wallet'),
						 ('наличка', 'Наличными'),
						)

	name = models.CharField (max_length = 200, verbose_name = "Имя заказчика")
	email = models.EmailField ( blank = True)
	telefon = models.CharField (max_length = 30, verbose_name = "Телефон")
	status = models.CharField (default = "В обработке", max_length = 200, verbose_name = "Статус заказа", choices = statusList)
	quantity = models.IntegerField (default = 0, verbose_name = "Количество товара")
	summ = models.FloatField (default = 0, verbose_name = "Сумма")
	data = models.DateField (default = timezone.now(), verbose_name = "Дата размещения")
	deliveryData = models.DateField (verbose_name = "Дата доставки")
	deliveryMethod = models.CharField (max_length = 20, choices = deliveryMethodList, verbose_name = "Способ доставки")
	Address = models.CharField (max_length = 300, default = '', verbose_name = "Адрес")
	deliveryCost = models.IntegerField (default = 0, verbose_name = "Стоимость доставки")
	paymentMethod = models.CharField (choices = paymentMethodList, verbose_name = "Способ оплаты", max_length = 100)
	qiwiAccNumber = models.CharField (max_length = 20, default = '', blank = True)



	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def __str__ (self):
		return (str(self.id) + ' ' + str(self.name) + ' ' + str(self.status))


from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Order
import datetime

class ContactForm (forms.Form):
	name = forms.CharField (max_length = 100, label = "Имя *")
	email = forms.EmailField (label = "Email *")
	title = forms.CharField (max_length = 100, label = "Тема *")
	message = forms.CharField (widget = forms.Textarea, label = "Сообщение *")



class OrderFormNew (forms.Form):
	deliveryMethodList = Order.deliveryMethodList
	paymentMethodList = Order.paymentMethodList

	error_css_class = 'error'
	required_css_class = 'required'

	quantity = forms.IntegerField (widget = forms.TextInput, min_value = 1, label = "Количество товара *")
	deliveryMethod = forms.ChoiceField (choices = deliveryMethodList, label = "Способ доставки *")
	paymentMethod = forms.ChoiceField (choices = paymentMethodList, label = "Способ оплаты *")


class deliveryForm (forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'

	quantity = forms.IntegerField (widget = forms.HiddenInput, min_value = 1)
	deliveryMethod = forms.CharField (max_length = 30, widget = forms.HiddenInput)
	deliveryData = forms.DateField (label = "Дата получения *", widget=SelectDateWidget(), initial = datetime.datetime.now())


class deliveryForm1 (deliveryForm):    #самовывоз

#################################################
#   Адреса пунктов самовывоза                   #
#################################################
	addressList = (('1','1'),)
	Address = forms.ChoiceField (choices = addressList, label = "Пункт самовывоза *")


class deliveryForm2 (deliveryForm): #курьер, почта
	
	Address = forms.CharField (max_length = 200, label = "Адрес доставки *")



class paymentForm1 (forms.Form):  #наличка

	error_css_class = 'error'
	required_css_class = 'required'

	name = forms.CharField (max_length = 200, label = "Ф.И.О. *")
	telefon = forms.CharField (max_length = 30, label = "Телефон *")
	email = forms.EmailField (required = False, label = "Email" )
	paymentMethod = forms.CharField (max_length = 30, widget = forms.HiddenInput)

	buttonName = 'Заказать'

#########################################################################
#                    													#
#       Добавить чек-бокс "С условиями согласен"                      	#
#																		#
#########################################################################



class paymentForm2 (paymentForm1): #оплата через qiwi

	qiwiAccNumber = forms.CharField (max_length = 50, label = "Номер QIWI-кошелька *")




























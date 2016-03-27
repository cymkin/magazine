from django.shortcuts import render
from magazin import models
from .forms import ContactForm, OrderFormNew, deliveryForm1, deliveryForm2, paymentForm1, paymentForm2
from django.http import HttpResponseRedirect


# Create your views here.
price = 1 				# Цена 1 ед. товара

def home (request):
	firstList = models.firstPost.objects.all ()
	secondList = models.secondPost.objects.all ()
	return render (request, 'home.html', {"firstList" : firstList, "secondList" : secondList})


def contact (request):
	secondList = models.secondPost.objects.all ()
	if request.method == 'POST':
		form = ContactForm (request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			f = models.Comments (name = cd['name'], email = cd['email'], text = cd['message'], title = cd['title'])
			f.save()
			return HttpResponseRedirect ('/contactthanks/')

	else:
		form = ContactForm ()

	return render (request, 'contact.html', {"form" : form, "secondList" : secondList})



def orderNew (request):
	secondList = models.secondPost.objects.all ()
	if request.method == 'POST':
		form = OrderFormNew (request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			formDict = {'quantity' : cd['quantity'],
				  'paymentMethod' : cd['paymentMethod'],
				  'deliveryMethod' : cd['deliveryMethod']}

			#############################################################
			#															#
			#   в зависимости от способа доставки и оплаты выбираем     #
			#   соответствующие классы форм                             #
			#															#
			#############################################################

			if formDict ['deliveryMethod'] == 'Самовывоз' : supClass2 = deliveryForm1
			else :
				supClass2 = deliveryForm2 #доставка почтой или курьером

			#############################################################
			#															#			
			# 		выбираем форму оплаты								#
			#															#
			#############################################################

			if formDict ['paymentMethod'] == 'наличка' : supClass1 = paymentForm1
			else : supClass1 = paymentForm2

			class lastOrderForm (supClass1, supClass2):
				pass

			form = lastOrderForm (initial={'quantity' : formDict['quantity'],
										   'deliveryMethod' : formDict ['deliveryMethod'],
										   'paymentMethod' : formDict ['paymentMethod']})

			return render (request, 'order2.html', {"form" : form, "secondList" : secondList})

	else:
		form = OrderFormNew ()

	return render (request, 'order.html', {"form" : form, "secondList" : secondList})


#########################################################################################
#																						#
#			Обработка второй формы														#
#																						#
#########################################################################################

def order2 (request):
	secondList = models.secondPost.objects.all ()
	if request.method == 'POST':

		#form = OrderForm (request.POST)

			#############################################################
			#															#
			#   в зависимости от способа доставки и оплаты выбираем     #
			#   соответствующие классы форм                             #
			#															#
			#############################################################
		if request.POST['deliveryMethod'] == 'Самовывоз' : supClass2 = deliveryForm1
		else :
			supClass2 = deliveryForm2 #доставка почтой или курьером

		if request.POST['paymentMethod'] == 'наличка' : supClass1 = paymentForm1
		else : supClass1 = paymentForm2
		class lastOrderForm (supClass1, supClass2):
			pass

		form = lastOrderForm (request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			f = models.Order (name = cd['name'],
							  email = cd['email'],
							  telefon = cd['telefon'],
							  status = '0',
							  quantity = cd['quantity'],
							  summ = price* int (cd['quantity']),
							  deliveryData = cd['deliveryData'],
							  deliveryMethod = cd['deliveryMethod'],
							  deliveryCost = models.Order.deliveryCostDict[cd['deliveryMethod']],
							  Address = cd['Address'],
							  qiwiAccNumber = cd['qiwiAccNumber'] if cd['paymentMethod'] == 'qiwi' else '',
							  paymentMethod = cd['paymentMethod'],
							  )
			f.save()
			return HttpResponseRedirect ('/orderthanks/')
		else :
			return render (request, 'order2.html', {"form" : form, "secondList" : secondList})

	else:
		form = OrderFormNew ()
	return render (request, 'order.html', {"form" : form, "secondList" : secondList})



def orderthx (request):
	secondList = models.secondPost.objects.all ()
	return render (request, 'orderthanks.html', {"secondList" : secondList})

def contactthx (request):
	secondList = models.secondPost.objects.all ()
	return render (request, 'contactthanks.html', {"secondList" : secondList})
















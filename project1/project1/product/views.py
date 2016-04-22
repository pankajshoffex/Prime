from django.shortcuts import render

from easy_pdf.views import PDFTemplateView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.forms.formsets import formset_factory, BaseFormSet
from django.template import RequestContext

from .models import Buyer, Product
from .forms import BuyerForm, ProductForm
from num2words import num2words



def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print username
		print password
		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			messages.error(request, "Incorrect Username or Password")
			return HttpResponseRedirect("/login/")	

	return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/login/')


class InvoicePDFView(PDFTemplateView):
	template_name = "invoice.html"

	def get_context_data(self, *args, **kwargs):
		return super(InvoicePDFView, self).get_context_data(*args, **kwargs)

class HomeView(TemplateView):
	template_name = "index.html"

	@method_decorator(login_required(login_url="/login/"))
	def dispatch(self, *args, **kwargs):
		return super(HomeView, self).dispatch(*args, **kwargs)

def create_invoice(request):
	flag = False
	msg = ""
	class RequiredFormSet(BaseFormSet):
		def __init__(self, *args, **kwargs):
			super(RequiredFormSet, self).__init__(*args, **kwargs)
			for form in self.forms:
				form.empty_permitted = False

	invoiceIteamFactory = formset_factory(ProductForm, extra=3, can_delete=True, formset=RequiredFormSet)
	if request.method == "POST":
		form = BuyerForm(request.POST)
		print request.POST
		formset = invoiceIteamFactory(request.POST)
		if form.is_valid() and formset.is_valid():
			buyer = form.save()
			for form in formset:
				product = form.save(commit=False)
				product.buyer = buyer
				product.save()
				flag = True
				msg = "Invoice added Successfully."
	form = BuyerForm()
	formset = invoiceIteamFactory()
	return render(
		request,
		'product/buyer_add.html',
		{
			'form': form,
			'formset': formset,
			'page': 'invoice',
			'flag': flag,
			'msg': msg
		},
	)


class InvoiceListView(ListView):
	model = Buyer
	template_name = "product/buyer_list.html"

	def get_context_data(self, **kwargs):
		context = super(InvoiceListView, self).get_context_data(**kwargs)
		return context








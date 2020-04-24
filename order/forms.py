from django import forms
from order.models import OrderItem

class GetQuantityForm(forms.ModelForm):

	class Meta:
		model = OrderItem
		fields = ['quantity']
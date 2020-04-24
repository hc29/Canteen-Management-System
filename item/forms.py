from django import forms
from item.models import FoodItem

class AddItemForm(forms.ModelForm):
	
	class Meta:
		model = FoodItem
		fields = ['title', 'details', 'price']




class UpdateItemForm(forms.ModelForm):

	class Meta:
		model = FoodItem
		fields = ['title', 'details', 'price']

	def save(self, commit=True):
		food_item 				= self.instance
		food_item.title			= self.cleaned_data['title']
		food_item.details		= self.cleaned_data['details']
		food_item.price			= self.cleaned_data['price']

		if commit:
			food_item.save()

		return food_item
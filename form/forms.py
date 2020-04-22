from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class electives(forms.Form):
	blank_choice = [('', '---------'),]
	Choices = [
		
		(1, 'Elective 1'),
		(2, 'Elective 2'),
		(3, 'Elective 3'),
		(4, 'Elective 4'),
		(5, 'Elective 5'),
		(6, 'Elective 6'),

		]
	name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	pref1 = forms.ChoiceField(
		choices = Choices+blank_choice,
		widget =forms.Select(attrs={
			'style': 'width:200px',
			'id': 'p1'}) )
	pref2 = forms.ChoiceField(
		choices = Choices+blank_choice,
		widget =forms.Select(attrs={
						'style': 'width:200px',

			'id': 'p2'}) )
	pref3 = forms.ChoiceField(
		choices = Choices+blank_choice,
		widget =forms.Select(attrs={
						'style': 'width:200px',

			'id': 'p3'}) )
	pref4 = forms.ChoiceField(
		choices = Choices+blank_choice,
		widget =forms.Select(attrs={
						'style': 'width:200px',

			'id': 'p4'}) )
	

	def clean(self):
		cd = self.cleaned_data
		p1 = cd.get("pref1")
		p2 = cd.get("pref2")
		p3 = cd.get("pref3")
		p4 = cd.get("pref4")

		if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4: 
			raise ValidationError("Fields Should be Unique")

		return cd
# class electives(forms.Form):
# 	name=forms.CharField(max_length=100)
# 	Elective1 = forms.CharField(max_length=100, required=False)
# 	Elective2 = forms.CharField(max_length=100, required=False)
# 	Elective3 = forms.CharField(max_length=100, required=False)
# 	Elective4 = forms.CharField(max_length=100, required=False)
# 	Elective5 = forms.CharField(max_length=100, required=False)
# 	Elective6 = forms.CharField(max_length=100, required=False)

# 	def clean(self):
# 		cd = self.cleaned_data
# 		p=[cd.get("Elective1"),
# 		cd.get("Elective2"),
# 		cd.get("Elective3"),
# 		cd.get("Elective4"),
# 		cd.get("Elective5"),
# 		cd.get("Elective6"),]
# 		lis = ['1','2','3','4','']
# 		for i in range(len(p)):
# 			if p[i] in lis:
# 				print("input ok")
# 			else:
# 				raise ValidationError("Input should be in {1,2,3,4}")
# 				return cd

# 		for i in range(len(p)):
# 			for j in range(len(p)):
# 				if i!=j and p[i]!='':
# 					if p[i]==p[j]:
# 						raise ValidationError("Fields Should be Unique")
# 						return cd
					



# 		return cd

class lol(forms.Form):
	post = forms.CharField()
	



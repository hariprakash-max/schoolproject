from django import forms
from admissions.models import student
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
 
#////-------------- creating html forms using django forms---------------///////  
        
# from django import forms 
class VendorForm(forms.Form): 
    name = forms.CharField() 
    address = forms.CharField() 
    contact = forms.CharField() 
    item = forms.CharField()        
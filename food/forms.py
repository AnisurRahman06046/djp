from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='Email')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # file = forms.FileField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # appointment = forms.DateField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    # # check = forms.BooleanField()
    # CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    # MEALS = [('P','Pepperoni'),('Mash','Mashroom'),('B','Beef'),('C','Chicken')]
    # pizza = forms.MultipleChoiceField(choices=MEALS,widget=forms.CheckboxSelectMultiple)
    
    
    # def clean_name(self):
    #     valName = self.cleaned_data['name']
    #     if len(valName) < 5:
    #         raise forms.ValidationError('Name must be at least 5 chars')
    #     return valName
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data['name']
    #     valEmail = self.cleaned_data['email']
    #     if len(valName)<4:
    #         raise forms.ValidationError('name must be at least 4 chars')
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError('invalid email')
    #     return cleaned_data
    
    
    
    def clean(self):
        cleaned_data = super().clean()
        valName = cleaned_data.get('name')
        valEmail = cleaned_data.get('email', '')  # Default value is set to empty string

        if valName and len(valName) < 4:
            raise forms.ValidationError('Name must be at least 4 characters')

        if  '.com' not in valEmail:
            raise forms.ValidationError('Invalid email')

        return cleaned_data




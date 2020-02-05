from django import forms

class FormName(forms.Form):
    version1 = forms.CharField()
    version2 = forms.CharField()

    #Check if the inputs are version numbers
    def clean(self):
        all_clean_data = super().clean()



        try:
            v1 = [int(i) for i in all_clean_data['version1'].split('.')]
            v2 = [int(i) for i in all_clean_data['version2'].split('.')]

        except:
            raise forms.ValidationError("MAKE SURE THEY ARE VERSION NUMBERS!")


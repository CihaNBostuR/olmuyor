from django import forms

from .models import YayinEvi,Kitap,Sinif,KitapTuru,DersTuru,Kitapismi
# ,DersTuru,Kitap

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Kitap
        fields = '__all__'


    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['yayinevi'].queryset = YayinEvi.objects.none()

        if 'basimyili' in self.data:
            try:
                basimyiliId = int(self.data.get('basimyili'))
                self.fields['yayinevi'].queryset = YayinEvi.objects.filter(basimyiliId=basimyiliId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['yayinevi'].queryset = self.instance.basimyili.yayinevi_set.order_by('name')
# 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sinif'].queryset = Sinif.objects.none()
        print("asadmsd")
        if 'yayinevi' in self.data:
            try:
                yayineviId = int(self.data.get('yayinevi'))
                self.fields['sinif'].queryset = YayinEvi.objects.filter(yayineviId=yayineviId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sinif'].queryset = self.instance.yayinevi.sinif_set.order_by('name')
# ------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kitapturu'].queryset = Sinif.objects.none()
        print("asadmsd")
        if 'sinif' in self.data:
            try:
                sinifId = int(self.data.get('sinif'))
                self.fields['kitapturu'].queryset = KitapTuru.objects.filter(sinifId=sinifId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['kitapturu'].queryset = self.instance.sinif.kitapturu_set.order_by('name')
# ------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dersturu'].queryset = KitapTuru.objects.all()

        if 'kitapturu' in self.data:
            print("adckmağeodfcka")
            try:
                kitapturuId = int(self.data.get('kitapturu'))
                self.fields['dersturu'].queryset = DersTuru.objects.filter(kitapturuId=kitapturuId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['dersturu'].queryset = self.instance.kitapturu.dersturu_set.order_by('name')

 # ------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kitapismi'].queryset = DersTuru.objects.all()

        if 'dersturu' in self.data:
            try:
                dersturuId = int(self.data.get('dersturu'))
                self.fields['kitapismi'].queryset = Kitapismi.objects.filter(kitapismi=dersturuId).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['kitapismi'].queryset = self.instance.dersturu.kitapismi_set.order_by('name')


# ------------------------------------------------------------------------------------------------------------------------------------
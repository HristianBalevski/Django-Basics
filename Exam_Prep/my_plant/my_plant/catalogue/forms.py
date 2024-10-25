from django.forms import ModelForm

from my_plant.catalogue.models import Plant


class CreatePlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class DeletePlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DeletePlantForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

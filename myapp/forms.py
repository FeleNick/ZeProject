from django import forms
from .models import Item, Task


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','description' ,'completed']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['task_name'].initial = kwargs['instance'].task_name

        

class TaskEdit(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'completed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['task_name'].initial = kwargs['instance'].task_name   



           
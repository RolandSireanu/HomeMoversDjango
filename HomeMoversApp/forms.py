from django import forms
from .models import MessageModel
import ipdb
class MessageModelForm(forms.ModelForm):

    class Meta:
        model = MessageModel
        fields = ["first_name", "last_name", "phone", "email", "message"]
        exclude = [];
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs);
        self.fields["first_name"].widget.attrs.update({"type":"text",  "class":"form-control", "name":"firstName", "placeholder":"first name"});
        self.fields["last_name"].widget.attrs.update({"type":"text",  "class":"form-control", "name":"lastName", "placeholder":"last name"});
        self.fields["email"].widget.attrs.update({"type":"email",  "class":"form-control", "name":"email", "placeholder":"email"});
        self.fields["phone"].widget.attrs.update({"type":"text",  "class":"form-control", "name":"phone", "placeholder":"phone number"});
        self.fields["message"].widget.attrs.update({"type":"text",  "class":"message-box", "name":"message", "placeholder":"message"});
    
    def setFieldInvalid(self, arg_fieldName):
        self.fields[arg_fieldName].widget.attrs["class"] += " is-invalid";
        self.fields[arg_fieldName].widget.attrs["value"] = "";
        # self.fields[arg_fieldName].widget.attrs.update({"class":value});

    def clean_phone(self):
        if self.cleaned_data["phone"][0] != '+':
            raise forms.ValidationError("Phone number should start with +");
        if len(self.cleaned_data["phone"]) != 12:
            raise forms.ValidationError("Phone number should be 12 characters long !")
        return self.cleaned_data["phone"];
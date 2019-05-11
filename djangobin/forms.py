from django import forms
from django.core.exceptions import ValidationError
from .models import Language
from django.forms import ModelForm, Textarea
 
 
class LanguageForm(forms.ModelForm):
	class Meta:
	    model = Language
	    fields = '__all__'
	    widgets = {
	        'file_extension': Textarea(attrs={'rows': 5, 'cols': 10}),
	    }
	    labels = {
	        'mime': 'MIME Type',
	        'lang_code': 'Language Code',
	    },
	    help_texts = {            
	        'lang_code': 'Short name of the Pygment lexer to use',
	        'file_extension': 'Specify extension like *.txt, *.md etc;'
	    },

	def clean_name(self):
		name = self.cleaned_data['name']
		if name == 'djangobin' or name == 'DJANGOBIN':
			raise ValidationError("name can't be {}.".format(name))

		# Always return the data
		return name

	def clean_slug(self):
		return self.cleaned_data['slug'].lower()
		# r = Language.objects.filter(slug=slug)
  #       if r.count:
  #           raise ValidationError("{0} already exists".format(slug))
 
  #       return slug.lower()

	def clean(self):
		cleaned_data = super(LanguageForm, self) .clean()
		slug = cleaned_data.get('slug')
		mime = cleaned_data.get('mime')

		if slug == mime:	
			raise ValidationError("Slug and MIME shouldn't be same.")

		# Always return the data
		return cleaned_data

	def save(self):
		new_lang = Language.objects.create(
		name = self.cleaned_data['name'],
		lang_code = self.cleaned_data['lang_code'],
		slug = self.cleaned_data['slug'],
		mime = self.cleaned_data['mime'],
		)
		return new_lang
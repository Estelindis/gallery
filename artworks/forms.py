from django import forms
from .models import Artist, Canvas, Design, Artwork


class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        artists = Artist.objects.all()
        artist_friendly_names = [(
            art.id, art.get_friendly_name()) for art in artists]
        canvasses = Canvas.objects.all()
        canvas_friendly_names = [(
            can.id, can.get_friendly_name()) for can in canvasses]
        designs = Design.objects.all()
        design_friendly_names = [(
            des.id, des.get_friendly_name()) for des in designs]

        self.fields['artist'].choices = artist_friendly_names
        self.fields['canvas'].choices = canvas_friendly_names
        self.fields['design'].choices = design_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

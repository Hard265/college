from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        label='Select a CSV file',
        help_text='Maximum size: 2MB'
    )

    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        if not file.name.endswith('.csv'):
            raise forms.ValidationError('Invalid file type. Please upload a CSV file.')
        if file.size > 2 * 1024 * 1024:  # 2MB limit
            raise forms.ValidationError('File size exceeds 2MB.')
        return file

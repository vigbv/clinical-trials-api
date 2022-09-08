from django.db import models

# Defining study model (from clinicaltrials.org, covid-19 study), keeping it simple for now
class StudyItem(models.Model):
    nct_id = models.CharField(max_length=30)
    study_url = models.CharField(max_length=300)
    study_title = models.CharField(max_length=500)
    study_status = models.CharField(max_length=50)
    sponsor_collaborators = models.CharField(max_length=500)
    
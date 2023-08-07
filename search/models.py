from django.db import models


class LeadRocks(models.Model):
    linked_url = models.CharField(max_length=255)
    full_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    job_title = models.CharField(max_length=255)
    facebook_profile = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    company_facebook = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    team_size = models.CharField(max_length=255)
    revenue_range = models.CharField(max_length=255)
    total_funding = models.CharField(max_length=255)
    work_email_1 = models.CharField(max_length=255)
    work_email_1_status = models.CharField(max_length=255)
    direct_email_1 = models.CharField(max_length=255)
    direct_email_1_status = models.CharField(max_length=255)
    direct_email_2 = models.CharField(max_length=255)
    direct_email_2_status = models.CharField(max_length=255)
    phone_1 = models.CharField(max_length=255)
    phone_2 = models.CharField(max_length=255)
    phone_3 = models.CharField(max_length=255)
    phone_4 = models.CharField(max_length=255)
    phone_5 = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.linked_url

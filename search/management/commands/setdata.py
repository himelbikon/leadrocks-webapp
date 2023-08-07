from django.core.management import BaseCommand
from search.models import LeadRocks
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        LeadRocks.objects.all().delete()
        df = pd.read_csv('search/leadrocks.csv')
        df = df.fillna('')

        for index, row in df.iterrows():
            leadrocks = LeadRocks(
                linked_url=row["Linked Url"],
                full_name=row["Full Name"],
                first_name=row["First Name"],
                last_name=row["Last Name"],
                job_title=row["Job Title"],
                facebook_profile=row["Facebook Profile"],
                location=row["Location"],
                company=row["Company"],
                company_website=row["Company Website"],
                company_facebook=row["Company Facebook"],
                company_email=row["Company Email"],
                company_phone=row["Company Phone"],
                industry=row["Industry"],
                team_size=row["Team Size"],
                revenue_range=row["Revenue Range"],
                total_funding=row["Total Funding"],
                work_email_1=row["Work Email #1"],
                work_email_1_status=row["Work Email #1 Status"],
                direct_email_1=row["Direct Email #1"],
                direct_email_1_status=row["Direct Email #1 Status"],
                direct_email_2=row["Direct Email #2"],
                direct_email_2_status=row["Direct Email #2 Status"],
                phone_1=row["Phone #1"],
                phone_2=row["Phone #2"],
                phone_3=row["Phone #3"],
                phone_4=row["Phone #4"],
                phone_5=row["Phone #5"],
            )
            leadrocks.save()

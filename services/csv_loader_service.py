import csv
from datetime import datetime
from models import db, MemberActivity

class CSVLoaderService:
    def __init__(self, db):
        self.db = db

    def load_csv_data(self, file_path):
        try:
            self._clear_existing_data()
            
            with open(file_path, 'r') as file:
                csv_reader = csv.DictReader(file)
                
                for row in csv_reader:
                    activity = MemberActivity(
                        date=datetime.strptime(row['Date'], '%Y-%m-%d').date(),
                        membership_id=row['Membership_ID'],
                        membership_type=row['Membership_Type'],
                        activity=row['Activity'],
                        revenue=float(row['Revenue']),
                        duration=int(row['Duration (Minutes)']),
                        location=row['Location']
                    )
                    self.db.session.add(activity)
                
                self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()
            raise e

    def _clear_existing_data(self):
        try:
            MemberActivity.query.delete()
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            raise 
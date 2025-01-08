from .base_repository import BaseRepository
from ..models import MemberActivity
from datetime import datetime

class MemberActivityRepository(BaseRepository):
    def get_all(self):
        return MemberActivity.query.all()

    def get_by_id(self, id):
        return MemberActivity.query.get(id)

    def get_by_date_range(self, start_date, end_date):
        return MemberActivity.query.filter(
            MemberActivity.date.between(start_date, end_date)
        ).all()

    def get_by_membership_id(self, membership_id):
        return MemberActivity.query.filter_by(membership_id=membership_id).all()

    def get_by_activity_type(self, activity):
        return MemberActivity.query.filter_by(activity=activity).all()

    def create(self, activity):
        self.db.session.add(activity)
        self.db.session.commit()
        return activity

    def update(self, activity):
        self.db.session.commit()
        return activity

    def delete(self, activity):
        self.db.session.delete(activity)
        self.db.session.commit() 
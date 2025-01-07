from .base_repository import BaseRepository
from models import QuarterlyPerformance

class QuarterlyPerformanceRepository(BaseRepository):
    def get_all(self):
        return QuarterlyPerformance.query.order_by(
            QuarterlyPerformance.year.desc(),
            QuarterlyPerformance.quarter.desc()
        ).all()

    def get_by_id(self, id):
        return QuarterlyPerformance.query.get(id)

    def get_by_year(self, year):
        return QuarterlyPerformance.query.filter_by(year=year).order_by(
            QuarterlyPerformance.quarter
        ).all()

    def get_by_year_and_quarter(self, year, quarter):
        return QuarterlyPerformance.query.filter_by(
            year=year,
            quarter=quarter
        ).first()

    def create(self, performance):
        self.db.session.add(performance)
        self.db.session.commit()
        return performance

    def update(self, performance):
        self.db.session.commit()
        return performance

    def delete(self, performance):
        self.db.session.delete(performance)
        self.db.session.commit() 
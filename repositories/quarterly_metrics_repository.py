from .base_repository import BaseRepository
from models import QuaterlyMetrics

class QuarterlyMetricsRepository(BaseRepository):
    def get_all(self):
        return QuaterlyMetrics.query.order_by(
            QuaterlyMetrics.year.desc(),
            QuaterlyMetrics.quarter.desc()
        ).all()

    def get_by_id(self, id):
        return QuaterlyMetrics.query.get(id)

    def get_by_year(self, year):
        return QuaterlyMetrics.query.filter_by(year=year).all()

    def create(self, metrics):
        self.db.session.add(metrics)
        self.db.session.commit()
        return metrics

    def update(self, metrics):
        self.db.session.commit()
        return metrics

    def delete(self, metrics):
        self.db.session.delete(metrics)
        self.db.session.commit()
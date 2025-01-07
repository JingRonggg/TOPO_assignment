from flask import Blueprint, jsonify, request
from http import HTTPStatus

pptx_data_blueprint = Blueprint('pptx_data', __name__)

class PPTXDataController:
    def __init__(self, annual_summary_repo, quarterly_metrics_repo, revenue_by_activity_repo):
        self.annual_summary_repo = annual_summary_repo
        self.quarterly_metrics_repo = quarterly_metrics_repo
        self.revenue_by_activity_repo = revenue_by_activity_repo

    def register_routes(self, blueprint):
        # Annual Summary routes
        blueprint.route('/annual-summary', methods=['GET'])(self.get_annual_summary)
        
        # Quarterly Metrics routes
        blueprint.route('/quarterly-metrics', methods=['GET'])(self.get_quarterly_metrics)
        blueprint.route('/quarterly-metrics/<int:year>', methods=['GET'])(
            self.get_quarterly_metrics_by_year
        )
        
        # Revenue by Activity routes
        blueprint.route('/revenue-by-activity', methods=['GET'])(self.get_revenue_by_activity)

    def get_annual_summary(self):
        summaries = self.annual_summary_repo.get_all()
        return jsonify([self._serialize_annual_summary(s) for s in summaries]), HTTPStatus.OK

    def get_quarterly_metrics(self):
        metrics = self.quarterly_metrics_repo.get_all()
        return jsonify([self._serialize_quarterly_metrics(m) for m in metrics]), HTTPStatus.OK

    def get_quarterly_metrics_by_year(self, year):
        metrics = self.quarterly_metrics_repo.get_by_year(year)
        return jsonify([self._serialize_quarterly_metrics(m) for m in metrics]), HTTPStatus.OK

    def get_revenue_by_activity(self):
        revenues = self.revenue_by_activity_repo.get_all()
        return jsonify([self._serialize_revenue_by_activity(r) for r in revenues]), HTTPStatus.OK

    def _serialize_annual_summary(self, summary):
        return {
            'id': summary.id,
            'total_revenue': summary.total_revenue,
            'total_membership_sold': summary.total_membership_sold,
            'top_location': summary.top_location
        }

    def _serialize_quarterly_metrics(self, metrics):
        return {
            'id': metrics.id,
            'year': metrics.year,
            'quarter': metrics.quarter,
            'revenue': metrics.revenue,
            'memberships_sold': metrics.memberships_sold,
            'duration': metrics.duration
        }

    def _serialize_revenue_by_activity(self, revenue):
        return {
            'id': revenue.id,
            'gym': revenue.gym,
            'pool': revenue.pool,
            'tennis_court': revenue.tennis_court,
            'personal_training': revenue.personal_training,
            'others': revenue.others
        }
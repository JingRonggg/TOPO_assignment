from flask import Blueprint, jsonify, request
from http import HTTPStatus

overall_blueprint = Blueprint('overall', __name__)

class OverallController:
    def __init__(self, company_repository, member_activity_repository, quarterly_performance_repository, key_highlights_repository, revenue_distribution_repository):
        self.company_repository = company_repository
        self.member_activity_repository = member_activity_repository
        self.quarterly_performance_repository = quarterly_performance_repository
        self.key_highlights_repository = key_highlights_repository
        self.revenue_distribution_repository = revenue_distribution_repository

    def register_routes(self, blueprint):
        blueprint.route('/')(self.get_all_data)
        blueprint.route('/<string:file_type>')(self.get_data)

    def get_data(self, file_type):
        try:
            if (file_type == 'json'):
                data = self._get_json_data()
            elif (file_type == 'csv'):
                data = self._get_csv_data()
            elif (file_type == 'pdf'):
                data = self._get_pdf_data()
            elif (file_type == 'pptx'):
                data = self._get_pptx_data()
            return jsonify(data), HTTPStatus.OK
        except: 
            return jsonify({'error': 'Unsupported file type'}), HTTPStatus.BAD_REQUEST

    def get_all_data(self):
        try:
            data = []
            data.append(self._get_json_data())
            data.append(self._get_csv_data())
            data.append(self._get_pdf_data())
            data.append(self._get_pptx_data())

            return jsonify(data), HTTPStatus.OK
        except:
            return jsonify({'error': 'error in getting data'}), HTTPStatus.BAD_REQUEST

    def _get_json_data(self):
        companies = self.company_repository.get_all()
        data = [{
            'id': c.id,
            'name': c.name,
            'industry': c.industry,
            'location': c.location,
            'employees': [{
                'id': e.id,
                'name': e.name,
                'role': e.role
            } for e in self.company_repository.get_by_id(c.id).employees],
            'performance': [{
                'quarter': p.quarter,
                'revenue': p.revenue,
                'profit_margin': p.profit_margin
            } for p in self.company_repository.get_by_id(c.id).performance]
        } for c in companies]

        return data
    
    def _get_csv_data(self):
        activities = self.member_activity_repository.get_all()
        return [self._serialize_activity(a) for a in activities]
        
    def _get_pdf_data(self):
        performances = self.quarterly_performance_repository.get_all()
        return [self._serialize_performance(p) for p in performances]

    def _get_pptx_data(self):
        data = []
        data.append(self._get_key_highlights())
        data.append(self._get_revenue_distribution())
        return data

    def _get_key_highlights(self):
        highlights = self.key_highlights_repository.get_all()
        return [self._serialize_highlight(h) for h in highlights]
    
    def _get_revenue_distribution(self):
        distributions = self.revenue_distribution_repository.get_all()
        return [self._serialize_distribution(d) for d in distributions]
    
    def _serialize_activity(self, activity):
        return {
            'id': activity.id,
            'date': activity.date.strftime('%Y-%m-%d'),
            'membership_id': activity.membership_id,
            'membership_type': activity.membership_type,
            'activity': activity.activity,
            'revenue': activity.revenue,
            'duration': activity.duration,
            'location': activity.location
        } 
    
    def _serialize_performance(self, performance):
        return {
            'id': performance.id,
            'year': performance.year,
            'quarter': performance.quarter,
            'revenue': performance.revenue,
            'memberships_sold': performance.memberships_sold,
            'duration': performance.duration
        } 
    
    def _serialize_highlight(self, highlight):
        return {
            'id': highlight.id,
            'total_revenue': highlight.total_revenue,
            'membership_sold': highlight.membership_sold,
            'top_location': highlight.top_location
        } 
    
    def _serialize_distribution(self, distribution):
        return {
            'id': distribution.id,
            'gym': distribution.gym,
            'pool': distribution.pool,
            'tennis_court': distribution.tennis_court,
            'personal_training': distribution.personal_training
        } 
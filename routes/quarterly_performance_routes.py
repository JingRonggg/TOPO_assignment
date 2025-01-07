from flask import Blueprint, jsonify, request
from http import HTTPStatus

quarterly_performance_blueprint = Blueprint('quarterly_performance', __name__)

class QuarterlyPerformanceController:
    def __init__(self, quarterly_performance_repository):
        self.repository = quarterly_performance_repository

    def register_routes(self, blueprint):
        blueprint.route('/', methods=['GET'])(self.get_all_performances)
        blueprint.route('/<int:id>', methods=['GET'])(self.get_performance)
        blueprint.route('/year/<int:year>', methods=['GET'])(self.get_performances_by_year)
        blueprint.route('/', methods=['POST'])(self.create_performance)

    def get_all_performances(self):
        performances = self.repository.get_all()
        return jsonify([self._serialize_performance(p) for p in performances]), HTTPStatus.OK

    def get_performance(self, id):
        performance = self.repository.get_by_id(id)
        if not performance:
            return jsonify({'error': 'Performance record not found'}), HTTPStatus.NOT_FOUND
        return jsonify(self._serialize_performance(performance)), HTTPStatus.OK

    def get_performances_by_year(self, year):
        performances = self.repository.get_by_year(year)
        return jsonify([self._serialize_performance(p) for p in performances]), HTTPStatus.OK

    def create_performance(self):
        data = request.get_json()
        try:
            performance = QuarterlyPerformance(
                year=data['year'],
                quarter=data['quarter'],
                revenue=float(data['revenue']),
                memberships_sold=int(data['memberships_sold']),
                duration=int(data['duration'])
            )
            created = self.repository.create(performance)
            return jsonify(self._serialize_performance(created)), HTTPStatus.CREATED
        except (KeyError, ValueError) as e:
            return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

    def _serialize_performance(self, performance):
        return {
            'id': performance.id,
            'year': performance.year,
            'quarter': performance.quarter,
            'revenue': performance.revenue,
            'memberships_sold': performance.memberships_sold,
            'duration': performance.duration
        } 
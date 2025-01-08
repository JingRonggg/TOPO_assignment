from flask import Blueprint, jsonify, request
from http import HTTPStatus
from ..repositories.revenue_distribution_repository import RevenueDistributionRepository
from ..models import RevenueDistribution

revenue_distribution_blueprint = Blueprint('revenue_distribution', __name__)

class RevenueDistributionController:
    def __init__(self, revenue_distribution_repository):
        self.repository = revenue_distribution_repository

    def register_routes(self, blueprint):
        blueprint.route('/', methods=['GET'])(self.get_all_distributions)
        blueprint.route('/<int:id>', methods=['GET'])(self.get_distribution)

    def get_all_distributions(self):
        distributions = self.repository.get_all()
        return jsonify([self._serialize_distribution(d) for d in distributions]), HTTPStatus.OK

    def get_distribution(self, id):
        distribution = self.repository.get_by_id(id)
        if not distribution:
            return jsonify({'error': 'Revenue distribution not found'}), HTTPStatus.NOT_FOUND
        return jsonify(self._serialize_distribution(distribution)), HTTPStatus.OK

    def _serialize_distribution(self, distribution):
        return {
            'id': distribution.id,
            'gym': distribution.gym,
            'pool': distribution.pool,
            'tennis_court': distribution.tennis_court,
            'personal_training': distribution.personal_training
        } 
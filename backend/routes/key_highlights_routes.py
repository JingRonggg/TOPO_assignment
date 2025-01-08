from flask import Blueprint, jsonify, request
from http import HTTPStatus
from ..repositories.key_highlights_repository import KeyHighlightsRepository
from ..models import KeyHighlights

key_highlights_blueprint = Blueprint('key_highlights', __name__)

class KeyHighlightsController:
    def __init__(self, key_highlights_repository):
        self.repository = key_highlights_repository

    def register_routes(self, blueprint):
        blueprint.route('/', methods=['GET'])(self.get_all_highlights)
        blueprint.route('/<int:id>', methods=['GET'])(self.get_highlight)

    def get_all_highlights(self):
        highlights = self.repository.get_all()
        return jsonify([self._serialize_highlight(h) for h in highlights]), HTTPStatus.OK

    def get_highlight(self, id):
        highlight = self.repository.get_by_id(id)
        if not highlight:
            return jsonify({'error': 'Key highlight not found'}), HTTPStatus.NOT_FOUND
        return jsonify(self._serialize_highlight(highlight)), HTTPStatus.OK

    def _serialize_highlight(self, highlight):
        return {
            'id': highlight.id,
            'total_revenue': highlight.total_revenue,
            'membership_sold': highlight.membership_sold,
            'top_location': highlight.top_location
        } 
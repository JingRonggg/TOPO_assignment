from flask import Blueprint, jsonify, request
from http import HTTPStatus
from datetime import datetime
from models import MemberActivity

member_activity_blueprint = Blueprint('member_activities', __name__)

class MemberActivityController:
    def __init__(self, member_activity_repository):
        self.member_activity_repository = member_activity_repository

    def register_routes(self, blueprint):
        blueprint.route('/', methods=['GET'])(self.get_all_activities)
        blueprint.route('/<int:activity_id>', methods=['GET'])(self.get_activity)
        blueprint.route('/', methods=['POST'])(self.create_activity)
        blueprint.route('/membership/<membership_id>')(self.get_activities_by_membership)
        blueprint.route('/activity-type/<activity_type>')(self.get_activities_by_type)

    def get_all_activities(self):
        activities = self.member_activity_repository.get_all()
        return jsonify([self._serialize_activity(a) for a in activities]), HTTPStatus.OK

    def get_activity(self, activity_id):
        activity = self.member_activity_repository.get_by_id(activity_id)
        if not activity:
            return jsonify({'error': 'Activity not found'}), HTTPStatus.NOT_FOUND
        return jsonify(self._serialize_activity(activity)), HTTPStatus.OK

    def create_activity(self):
        data = request.get_json()
        try:
            activity = MemberActivity(
                date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
                membership_id=data['membership_id'],
                membership_type=data['membership_type'],
                activity=data['activity'],
                revenue=float(data['revenue']),
                duration=int(data['duration']),
                location=data['location']
            )
            created_activity = self.member_activity_repository.create(activity)
            return jsonify(self._serialize_activity(created_activity)), HTTPStatus.CREATED
        except (KeyError, ValueError) as e:
            return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

    def get_activities_by_membership(self, membership_id):
        activities = self.member_activity_repository.get_by_membership_id(membership_id)
        return jsonify([self._serialize_activity(a) for a in activities]), HTTPStatus.OK

    def get_activities_by_type(self, activity_type):
        activities = self.member_activity_repository.get_by_activity_type(activity_type)
        return jsonify([self._serialize_activity(a) for a in activities]), HTTPStatus.OK

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
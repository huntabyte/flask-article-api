from flask_restx import Namespace, Resource

api = Namespace("health", description="Health check related operations")


class Health(Resource):
    def get(self):
        return {"status": "OK", "message": "Server is healthy"}


api.add_resource(Health, "")

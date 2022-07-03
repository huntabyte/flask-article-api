from flask import request
from flask_restx import Namespace, Resource, fields
from src.articles.services import (
    create_article,
    get_all_articles,
    get_article,
    update_article,
    delete_article,
)

api = Namespace("articles", description="Article related operations")

article_fields = api.model(
    "Article", {"title": fields.String, "content": fields.String}
)


class ArticleList(Resource):
    def get(self):
        """Get a list of articles"""
        return get_all_articles()

    @api.doc(body=article_fields)
    def post(self):
        """Create a new article"""
        return create_article(request.get_json())


class Article(Resource):
    def get(self, article_id):
        """Get an article by ID"""
        return get_article(article_id)

    @api.doc(body=article_fields)
    def put(self, article_id):
        """Update an article by ID"""
        return update_article(article_id, request.get_json())

    def delete(self, article_id):
        """Delete an article by ID"""
        return delete_article(article_id)


api.add_resource(ArticleList, "")
api.add_resource(Article, "/<int:article_id>")

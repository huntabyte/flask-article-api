from src import db
from src.articles.models import Article
from src.articles.schemas import article_schema, article_list_schema


def create_article(data):
    """Given serialized data, deserialize it and create a new article"""
    article = article_schema.load(data)
    db.session.add(article)
    db.session.commit()
    return article_schema.dump(article), 201


def get_all_articles():
    """Deserialize and return all articles in database"""
    return article_list_schema.dump(Article.query.all()), 200


def get_article(article_id):
    """Given an article ID, return a serialized article object"""
    if not (article := Article.query.filter_by(id=article_id).first()):
        return {"message": f"Article with ID {article_id} does not exist"}, 404

    return article_schema.dump(article), 200


def update_article(article_id, data):
    if not (article := Article.query.filter_by(id=article_id).first()):
        return {"message": f"Article with ID {article_id} does not exist"}, 404

    article_schema.load(data, instance=article, partial=True)
    db.session.commit()
    return article_schema.dump(article), 200


def delete_article(article_id):
    if not (article := Article.query.filter_by(id=article_id).first()):
        return {"message": f"Article with ID {article_id} does exist"}, 404

    db.session.delete(article)
    db.session.commit()
    return "", 204

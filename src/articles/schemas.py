from src import ma
from src.articles.models import Article


class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        load_instance = True
        ordered = True


article_schema = ArticleSchema()
article_list_schema = ArticleSchema(many=True)

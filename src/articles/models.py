from datetime import datetime, timezone
from src import db

Column = db.Column
Model = db.Model


class Article(Model):
    __tablename__ = "articles"

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(255), nullable=False)
    content = Column(db.Text, nullable=False)
    created_at = Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Article {self.title} - {self.content[0:10]}>"

from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor='cherry',
    size='large',
    rating=5,
)

c2 = Cupcake(
    flavor='chocolate',
    size='small',
    rating=9,
    image='https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg'
)

c3 = Cupcake(
    flavor='red velvet',
    size='medium',
    rating=10,
    image='https://images.unsplash.com/photo-1610306212789-7508d076e925?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80'
)

c4 = Cupcake(
    flavor='chocolate and vanilla',
    size='large',
    rating=7,
    image='https://media.hswstatic.com/eyJidWNrZXQiOiJjb250ZW50Lmhzd3N0YXRpYy5jb20iLCJrZXkiOiJnaWZcLzEwLW1vc3QtcG9wdWxhci1jdXBjYWtlLWZsYXZvcnMtNi5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjIwMH19fQ=='
)

c5 = Cupcake(
    flavor='carrot',
    size='small',
    rating=5,
    image='https://images.unsplash.com/photo-1487124504955-e42a39e11aaf?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1012&q=80'
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()

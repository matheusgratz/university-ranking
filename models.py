def create_classes(db):
    class University_Ranking(db.Model):
        __tablename__ = 'universities_ranking'

        ranking = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(64))
        location = db.Column(db.String(64))
        continent = db.Column(db.String(64))
        number_students = db.Column(db.Float)
        students_staff_ratio = db.Column(db.String(64))
        perc_intl_students = db.Column(db.String(64))
        gender_ratio = db.Column(db.String(64))
        overall_score = db.Column(db.Float)
        teaching_score = db.Column(db.Float)
        research_score = db.Column(db.Float)
        citations_score = db.Column(db.Float)
        industry_income_score = db.Column(db.Float)
        intl_outlook_score = db.Column(db.Float)
        latitude = db.Column(db.Float)
        longitude = db.Column(db.Float)

        def __repr__(self):
            return '<University_Ranking %r>' % (self.title)
    return University_Ranking



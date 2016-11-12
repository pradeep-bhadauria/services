from mgn import db
class Testtable(db.Model):
	__tablename__ = 'test'
	__table_args__ = {"schema":"test"}
	id = db.Column(db.BigInteger, primary_key=True)
	name = db.Column(db.String(45), unique=True)
	desc = db.Column(db.String(100))
	updated = db.Column(db.DateTime, nullable=True)
	
	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'desc': self.desc,
			'updated': str(self.updated)
		}
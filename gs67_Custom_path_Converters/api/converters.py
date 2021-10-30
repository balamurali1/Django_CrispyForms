class FourDigitYearConverter:
	regex = '[0-9]{4}' #[0-9] ante 0 nundi 9 varuku yevaina numbers thisukovali ani, {4} ante only 4digits numbers matrame thisukovali ani artha..

	def to_python(self,value):
		return int(value)

	def to_url(self,value):
		return f'{value:4d}' #d is the integer type	
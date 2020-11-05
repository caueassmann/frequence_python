class Numbers:
	"""docstring for Numbers"""
	def __init__(self,number,frequencia, frequencia_rel, frequencia_acl, frequencia_acl_rel):
		self.frequencia = frequencia
		self.number = number
		self.frequencia_rel = frequencia_rel
		self.frequencia_acl = frequencia_acl
		self.frequencia_acl_rel = frequencia_acl_rel

		def setNumber(self,number):
			self.number = number

		def getNumber(self):
			return self.number


		def setFrequencia(self,frequencia):
			self.frequencia = frequencia
		
		def getFrequencia(self):
			return self.frequencia

		def setFrequenciaRel(self,frequencia_rel):
			self.frequencia_rel = frequencia_rel
		
		def getFrequenciaRel(self):
			return self.frequencia_rel

		def setFrequenciaAcl(self,frequencia_acl):
			self.frequencia_acl = frequencia_acl
		
		def getFrequenciaAcl(self):
			return self.frequencia_acl

		def setFrequenciaAclRel(self,frequencia_acl_rel):
			self.frequencia_acl_rel = frequencia_acl_rel
		
		def getFrequenciaAclRel(self):
			return self.frequencia_acl_rel

		
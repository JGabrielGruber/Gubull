from rest_framework import serializers
from .models        import RFID

class RFIDSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = RFID
		fields = ['identificacao', 'brinco', 'data']
	
	def create(self, validated_data):
		user = RFID.objects.create(
			brinco=validated_data['brinco'])
		return user

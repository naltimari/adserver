from django.conf import settings
from urls import publicidade

def get_advertising_tags(request):
	tag = None
	for regexp in publicidade:
		if regexp.resolve(request.path):
			tag = regexp
			break
	
	return { 'tag_publicidade': tag.name }
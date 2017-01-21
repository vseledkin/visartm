from models.models import Topic 
from visual.models import Polygon
import json

def visual(model, params):
	root_topic = Topic.objects.filter(model = model, layer = 0)[0]
	root_polygon = Polygon()
	root_polygon.topic = root_topic
	root_polygon.rect_top = 0
	root_polygon.rect_left = 0
	root_polygon.rect_width = 50000
	root_polygon.rect_height = 30000
	root_polygon.points_from_rect()
	root_polygon.save()
	return 'root=' + json.dumps(root_polygon.to_json_object()) + ';'
	

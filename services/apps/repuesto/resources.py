from import_export import resources
from apps.repuesto.models import Repuesto

class RepuestoResources(resources.ModelResource):
    class Meta:
        model = Repuesto
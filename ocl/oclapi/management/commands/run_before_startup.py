from django.core.management import BaseCommand
from django.db import connections

from oclapi.models import ConceptContainerVersionModel
from sources.models import SourceVersion
from collection.models import CollectionVersion, CollectionItem

class Command(BaseCommand):
    help = 'run before startup'

    def handle(self, *args, **options):
        self.run_db_migrations()

        self.clear_all_processing()


    def run_db_migrations(self):
        db = connections['default']
        print 'Deleting concepts and mappings fields from SourceVersion'
        db.get_collection('sources_sourceversion').update({},{'$unset': {'concepts':1, 'mappings':1}}, multi=True)

        print 'Deleting _ocl_processing from SourceVersion'
        db.get_collection('sources_sourceversion').update({},{'$unset': {'_ocl_processing':1}}, multi=True)
        print 'Deleting _ocl_processing from CollectionVersion'
        db.get_collection('collection_collectionversion').update({},{'$unset': {'_ocl_processing':1}}, multi=True)

        print 'Migrating concepts and mappings in collections to a new model'
        for collection_version in CollectionVersion.objects.all():
            already_migrated = True
            for concept in collection_version.concepts:
                already_migrated = False
                CollectionItem(collection_id=collection_version.id, concept_id=concept).save()
            for mapping in collection_version.mappings:
                already_migrated = False
                CollectionItem(collection_id=collection_version.id, mapping_id=mapping).save()

            if not already_migrated:
                collection_version.concepts = []
                collection_version.mappings = []
                collection_version.save()

    def clear_all_processing(self):
        ConceptContainerVersionModel.clear_all_processing(SourceVersion)
        ConceptContainerVersionModel.clear_all_processing(CollectionVersion)

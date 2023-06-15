# File: beetsplug/ArtistConsolidator.py
from beets.plugins import BeetsPlugin
from beets.importer import action
from beets.ui import Subcommand

class ArtistConsolidatorPlugin(BeetsPlugin):
    def __init__(self):
        super(ArtistConsolidatorPlugin, self).__init__()
        self.config.add({
            'mappings': []
        })
        self.import_stages = [self.imported]
        self.register_listener('import_task_choice', self.modify)

    def modify(self, session, task):
        mappings = self.config['mappings'].as_pairs()
        if task.choice_flag == action.APPLY:
            for item in task.items:
                for original_names, new_name in mappings:
                    if item.albumartist in original_names:
                        item.albumartist = new_name
                        item.store()

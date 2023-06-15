# File: beetsplug/ArtistConsolidator.py
from beets.plugins import BeetsPlugin
from beets.importer import action
from beets.ui import Subcommand

class ModifyArtistPlugin(BeetsPlugin):
    def __init__(self):
        super(ModifyArtistPlugin, self).__init__()

        self.import_stages = [self.imported]
        self.register_listener('import_task_choice', self.modify)

    def modify(self, session, task):
        if task.choice_flag == action.APPLY:
            for item in task.items:
                if item.albumartist in ["Prince & 3rdEyeGirl", 
                                        "Prince & The New Power Generation", 
                                        "Prince & The Revolution", 
                                        "Prince And The Revolution", 
                                        "Prince and The Revolution", 
                                        "The Artist (Formerly Known As Prince)"]:
                    item.albumartist = "Prince"
                    item.store()
                elif item.albumartist in ["The Jimi Hendrix Experience", "Band of Gypsys"]:
                    item.albumartist = "Jimi Hendrix"
                    item.store()
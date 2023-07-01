#!/usr/bin/env python3
# File: beetsplug/ArtistConsolidator.py
from beets.plugins import BeetsPlugin
from beets.importer import action
from beets.ui import Subcommand

class ArtistConsolidatorPlugin(BeetsPlugin):
    def __init__(self):
        super(ArtistConsolidatorPlugin, self).__init__()

        self.register_listener('import_task_choice', self.consolidate_artists)

    def commands(self):
        cmd = Subcommand('consolidate_artists',
                         help='rename artist variants to a single name')
        return [cmd]

    def consolidate_artists(self, session, task):
        if task.choice_flag is action.ASIS:
            return

        artist_name_mapping = self.config['artist_mapping'].get(dict)
        for key in artist_name_mapping:
            if task.albumartist == key:
                task.albumartist = artist_name_mapping[key]
                self._log.info(u'Changed album artist to: {0}', task.albumartist)

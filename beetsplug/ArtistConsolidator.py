from beets.plugins import BeetsPlugin
from beets import config
import logging

log = logging.getLogger('beets.ArtistConsolidator')

class ArtistConsolidatorPlugin(BeetsPlugin):
    def __init__(self):
        super(ArtistConsolidatorPlugin, self).__init__()
        self.config.add({
            'artist_dict': {}
        })
        self.artist_dict = self.config['artist_dict']  # Use it directly

        self.register_listener('import_task_choice', self.consolidate_artists)

    def consolidate_artists(self, session, task):
        if task.is_album:
            for item in task.items:
                # Check if this item is a part of a compilation
                if item.get('comp', False):
                    # This item is a part of a compilation, skip it
                    continue

                for original, consolidated in self.artist_dict.items():
                    if item.albumartist == original:
                        log.info(f"Changing albumartist from {original} to {consolidated}")
                        item.albumartist = consolidated
                        item.artist = consolidated  # If you want to update the artist field too
                        item.store()
        else:
            # If it's a singleton, update the albumartist and artist fields for the item only.
            for item in task.items:
                for original, consolidated in self.artist_dict.items():
                    if item.albumartist == original:
                        log.info(f"Changing albumartist from {original} to {consolidated}")
                        item.albumartist = consolidated
                        item.artist = consolidated  # If you want to update the artist field too
                        item.store()

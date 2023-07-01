from beets.plugins import BeetsPlugin
from beets import config
import logging

log = logging.getLogger('beets.ArtistConsolidator')

class ArtistConsolidatorPlugin(BeetsPlugin):
    def __init__(self):
        super(ArtistConsolidatorPlugin, self).__init__()
        self.config.add({
            'artist_dict': {},
            'update_track_artists': False  # Default option set to False
        })
        self.artist_dict = self.config['artist_dict']  # Use it directly
        self.update_track_artists = self.config['update_track_artists'].get(bool)

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
                        if self.update_track_artists:
                            item.artist = consolidated  # Update track artist only if option is set to True
                        item.store()
        else:
            # If it's a singleton, update the albumartist fields for the item only.
            for item in task.items:
                for original, consolidated in self.artist_dict.items():
                    if item.albumartist == original:
                        log.info(f"Changing albumartist from {original} to {consolidated}")
                        item.albumartist = consolidated
                        if self.update_track_artists:
                            item.artist = consolidated  # Update track artist only if option is set to True
                        item.store()

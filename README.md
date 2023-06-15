# ArtistConsolidator
Simple Beets Plugin to Consolidate Artists and Bands that have gone by several different names into 1 folder

Right now it just works for Prince and Jimi Hendrix because these were the ones I needed to clean up my personal library, but it's easy to add more artists as needed. I may look at expanding this to allow you to specify the artist and band names yourself in your config.yaml file, if there's any interest in this.

For example, my library import originally created the following folders:

Prince

Prince & 3rdEyeGirl

Prince & The New Power Generation

Prince & The Revolution

Prince And The Revolution

Prince and The Revolution

The Artist (Formerly Known As Prince)

This is obviously not ideal for keeping a tidy library. This plugin will change the album artist value for all of these to just 'Prince' so they are all consolidated into one folder.

To install, copy the file ArtistConsolidator.py to your beetsplug folder (if you don't have one, you can create one) and add 'ArtistConsolidator' to your list of plugins in config.yaml

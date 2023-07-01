# beets-ArtistConsolidator

Simple Beets Plugin to Consolidate Artists and Bands that have gone by several different names into 1 folder.

For example, my library import originally created the following folders:

Prince

Prince & 3rdEyeGirl

Prince & The New Power Generation

Prince & The Revolution

Prince And The Revolution

Prince and The Revolution

The Artist (Formerly Known As Prince)

This is obviously not ideal for keeping a tidy library. This plugin will change the album artist value for all of these to just 'Prince' so they are all consolidated into one folder.

To install, copy the file ArtistConsolidator.py to your beetsplug folder (if you don't have one, you can create one) and add 'ArtistConsolidator' to your list of plugins in config.yaml. More details on this are available here: https://beets.readthedocs.io/en/stable/dev/plugins.html

In your config.yaml file, add the following lines. This example shows Prince and Jimi Hendrix, obviously you can add as many as you need. 
```
ArtistConsolidator:
    artist_mapping:
        "The Artist (Formerly Known As Prince)": "Prince"
        "Prince & 3rdEyeGirl": "Prince"
        "Prince & The New Power Generation": "Prince"
        "Prince & The Revolution": "Prince"
        "Prince And The Revolution": "Prince"
        "Prince and The Revolution": "Prince"
        "The Jimi Hendrix Experience": "Jimi Hendrix"
        "Band of Gypsys": "Jimi Hendrix"
```

Note, the quotation marks are not taken literally, so in the event that you need to include an artist name that includes quotation marks, you can use escape characters in 1 of 2 ways:

```
"\"Artist Name\""
'"Artist Name"'
```

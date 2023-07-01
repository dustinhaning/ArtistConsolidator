# beets-ArtistConsolidator

Simple Beets Plugin to Consolidate Artists and Bands that have gone by several different names into 1 folder.

For example, my library import originally created the following folders:
```
Prince
Prince & 3rdEyeGirl
Prince & The New Power Generation
Prince & The Revolution
Prince And The Revolution
Prince and The Revolution
The Artist (Formerly Known As Prince)
```
This is obviously not ideal for keeping a tidy library. This plugin will change the album artist value for all of these to just 'Prince' so they are all consolidated into one folder.

This can also be useful for split albums that have 2 album artists, if you want to have it go to one artist folder.

For example, in my library I had these 2 artist folders because they had a split album:
```
Fit for an Autopsy
Fit for an Autopsy _ Thy Art Is Murder _ Malevolence
```
Lastly, for Classical albums, you may want to have them in folders for the original composor, the performance composor, or the perfomance ensemble.

For Example the ablum ["Water Music • Music For The Royal Fireworks" by Georg Friedrich Händel / L'Arte Dell'Arco, Federico Guglielmo](https://www.discogs.com/release/12419841-Georg-Friedrich-H%C3%A4ndel-LArte-DellArco-Federico-Guglielmo-Water-Music-Music-For-The-Royal-Fireworks)

By default, Beets created an artist folder like this:
```
George Frideric Handel; L'Arte dell'Arco, Federico Guglielmo
```
Instead, I can use this plugin to have this go to any of these folders, depending on preferences:
```
George Frideric Handel
Handel
L'Arte dell'Arco, Federico Guglielmo
L'Arte dell'Arco
Federico Guglielmo
```
To install, copy the file ArtistConsolidator.py to your beetsplug folder (if you don't have one, you can create one) and add 'ArtistConsolidator' to your list of plugins in config.yaml. More details on this are available here: https://beets.readthedocs.io/en/stable/dev/plugins.html

In your config.yaml file, add the following lines. This example shows Prince and Jimi Hendrix, obviously you can add as many as you need. The first name is the original name and the second one is what you want to change it to.

```
ArtistConsolidator:
    artist_dict:
        "The Artist (Formerly Known As Prince)": "Prince"
        "Prince & 3rdEyeGirl": "Prince"
        "Prince & The New Power Generation": "Prince"
        "Prince & The Revolution": "Prince"
        "Prince And The Revolution": "Prince"
        "Prince and The Revolution": "Prince"
        "The Jimi Hendrix Experience": "Jimi Hendrix"
        "Band of Gypsys": "Jimi Hendrix"
```

Note: Quotes are technically not needed most of the time, but certain things like colons, numbers, and boolans like Yes, No, True, or False, and Null have special uses in .yaml files, and there's a chance they could be in a band or artist name. So it's best practice to just use quotes. However, in the event that you need to include an artist name that includes quotation marks, you can use escape characters in 1 of 2 ways with either \ or by using single quotes and double quotes:

```
"\"Artist Name\""
'"Artist Name"'
```

This is beta software and I haven't been able to test every scenario and I don't know how it will interact with other plugins, so proceed with caution. 

# Grok-Map: Ancient Texts Map Enhancement Project

## What This Is
This folder contains ALL the map data from the Ancient Texts Study App.
Grok should use this to enhance the map with:

1. **More precise historical boundaries** (GeoJSON polygons with proper coordinates)
2. **Time-slider functionality** — boundaries for EVERY major period from 3000 BC to present
3. **More megalithic/anomalous sites** (currently 30+, target 100+)
4. **More detailed site descriptions and connections**
5. **Better empire boundary polygons** (current ones are simplified)
6. **Any new journey routes** for biblical narratives

## How the Map Works
- The app uses **Leaflet.js** (loaded from CDN) in a single HTML file
- All map data is defined as JavaScript arrays/objects in `app.js`
- The build system (`build.py`) assembles everything into one HTML file
- Map categories: `biblical`, `watcher`, `megalith`, `pyramid`, `dss`, `cultural`

## Data Format

### Sites (MAP_SITES array)
```javascript
{cat:'megalith', name:'Site Name', lat:37.22, lng:38.92,
 desc:'Description of the site...',
 refs:'Genesis 11:8-9', // scripture references (optional)
 note:'Interesting notes...',  // optional
 img:'https://...'  // optional image URL
}
```

### Journeys (MAP_JOURNEYS array)
```javascript
{
    id: 'journey_id',
    name: 'Journey Name',
    color: '#c9a84c',  // hex color
    weight: 3,          // line thickness
    dash: '8,4',        // optional dash pattern
    desc: 'Description',
    refs: 'Genesis 12-25',
    waypoints: [
        {lat:30.96, lng:46.1, label:'Starting Point', ref:'Gen 11:31'},
        {lat:36.87, lng:39.03, label:'Next Stop', ref:'Gen 12:1'}
    ]
}
```

### Empire Boundaries
```javascript
{name:'Empire Name (~dates)', color:'#hex', coords:[[lat,lng],[lat,lng],...]}
```
These are rendered as Leaflet polygons with dashed outlines and transparent fill.

## Current Basemap Options
1. Google Satellite (default, zoom 20)
2. Google Hybrid (labels)
3. ESRI Satellite
4. Nat Geo World Map
5. CartoDB Dark
6. OpenStreetMap
7. OpenTopoMap

## Files in This Folder
- `README.md` — this file
- `SITES.json` — all current map sites
- `JOURNEYS.json` — all current journey routes
- `EMPIRES.json` — all current empire boundary polygons
- `CATEGORIES.json` — map category definitions
- `ENHANCEMENT_TASKS.md` — specific tasks for Grok

## Integration
When Grok produces enhanced data:
1. Updated JSON files go back here
2. Claude Code integrates them into `src/js/app.js`
3. `python build.py` rebuilds the HTML

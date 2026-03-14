// Ancient Texts Library — Service Worker
const CACHE_NAME = 'ancient-texts-20260314001759';
const CORE_ASSETS = [
    './',
    './index.html',
    './manifest.webmanifest',
    './data/manifest.json',
    './data/text_intros.json',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => cache.addAll(CORE_ASSETS))
    );
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys =>
            Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
        )
    );
    self.clients.claim();
});

self.addEventListener('fetch', event => {
    // Network-first for ALL requests — always try to get fresh content
    // Falls back to cache when offline
    event.respondWith(
        fetch(event.request).then(resp => {
            if (resp.ok) {
                const clone = resp.clone();
                caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
            }
            return resp;
        }).catch(() => caches.match(event.request))
    );
});

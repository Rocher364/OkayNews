const CACHE_NAME = 'okaynews-v1';
const urlsToCache = [
  '/',
  '/static/css/styles.css', // Asire w ou gen chemen sa yo
  '/static/js/main.js'
];

// Enstalasyon
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
});

// Rekipere done (Fetch)
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
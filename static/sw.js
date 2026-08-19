const CACHE="agroconnect-v1";
const ASSETS=["/","/static/index.html","/static/styles.css","/static/app.js","/static/manifest.json"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS))));
self.addEventListener("fetch",e=>{
  if(e.request.method!=="GET") return;
  e.respondWith(caches.match(e.request).then(cached=>cached||fetch(e.request).catch(()=>caches.match("/"))));
});

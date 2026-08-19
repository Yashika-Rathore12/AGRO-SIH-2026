const $ = id => document.getElementById(id);

const translations = {
  en: {
    heroTitle: "One simple dashboard for the whole farm journey.",
    heroText: "Monitor field conditions, screen crop stress, plan irrigation, forecast harvest and find stronger buyer options.",

    eyebrow: "SMART AGRICULTURE • SIH 2026",
    offline: "Offline-first PWA",
    refresh: "↻ Refresh",

    controlRoom: "Today's control room",
    farmIntelligence: "FARM INTELLIGENCE",

    crop: "Crop",
    moisture: "Soil moisture",
    temperature: "Temperature",
    bestMandi: "Best mandi",

    liveTelemetry: "live telemetry",
    microclimate: "microclimate",

    soilClimate: "Soil & microclimate",
    latestSensor: "Latest sensor snapshot",
    quickAdvisory: "Quick advisory",
    explainableRules: "Explainable rules from farm telemetry",
    generateAdvisory: "Generate farm advisory",

    leafHealth: "Leaf health AI",
    uploadLeaf: "Upload a clear leaf photo",
    runAI: "Run AI screening",

    mandiIntelligence: "Mandi intelligence",
    regionalPrices: "Regional price snapshot",

    harvestForecast: "Harvest forecast",
    expectedHarvest: "Expected quantity + harvest window",
    forecast: "Forecast harvest",

    buyerLogistics: "Buyer & logistics match",
    connectHarvest: "Connect harvest quantity to nearby demand",
    findBuyers: "Find best buyers",

    mobileTelemetry: "Mobile telemetry simulator",
    sensorIngestion: "Demonstrates sensor ingestion and offline queueing",
    sendTelemetry: "Send telemetry",
    syncQueue: "Sync offline queue",

    area: "Area (acres)",
    quantity: "Quantity (t)",
    cropLabel: "Crop",

    footer: "AgroConnect AI • SIH 2026 prototype • Built with FastAPI + SQLite + HTML/CSS/JavaScript"
  },

  hi: {
    heroTitle: "पूरे खेत की यात्रा के लिए एक सरल डैशबोर्ड।",
    heroText: "खेत की स्थिति देखें, फसल तनाव की जांच करें, सिंचाई की योजना बनाएं, उत्पादन का अनुमान लगाएं और बेहतर खरीदार खोजें।",

    eyebrow: "स्मार्ट कृषि • SIH 2026",
    offline: "ऑफलाइन-फर्स्ट PWA",
    refresh: "↻ रिफ्रेश",

    controlRoom: "आज का फार्म कंट्रोल रूम",
    farmIntelligence: "फार्म इंटेलिजेंस",

    crop: "फसल",
    moisture: "मिट्टी की नमी",
    temperature: "तापमान",
    bestMandi: "सबसे अच्छी मंडी",

    liveTelemetry: "लाइव टेलीमेट्री",
    microclimate: "माइक्रोक्लाइमेट",

    soilClimate: "मिट्टी और माइक्रोक्लाइमेट",
    latestSensor: "नवीनतम सेंसर जानकारी",
    quickAdvisory: "त्वरित सलाह",
    explainableRules: "फार्म टेलीमेट्री के आधार पर सलाह",
    generateAdvisory: "फार्म सलाह तैयार करें",

    leafHealth: "पत्ती स्वास्थ्य AI",
    uploadLeaf: "पत्ती की साफ तस्वीर अपलोड करें",
    runAI: "AI जांच शुरू करें",

    mandiIntelligence: "मंडी इंटेलिजेंस",
    regionalPrices: "क्षेत्रीय बाजार मूल्य",

    harvestForecast: "फसल उत्पादन अनुमान",
    expectedHarvest: "अनुमानित मात्रा और कटाई का समय",
    forecast: "फसल अनुमान देखें",

    buyerLogistics: "खरीदार और लॉजिस्टिक्स",
    connectHarvest: "फसल की मात्रा को स्थानीय मांग से जोड़ें",
    findBuyers: "सर्वश्रेष्ठ खरीदार खोजें",

    mobileTelemetry: "मोबाइल टेलीमेट्री सिम्युलेटर",
    sensorIngestion: "सेंसर डेटा और ऑफलाइन कतार का प्रदर्शन",
    sendTelemetry: "टेलीमेट्री भेजें",
    syncQueue: "ऑफलाइन डेटा सिंक करें",

    area: "क्षेत्रफल (एकड़)",
    quantity: "मात्रा (टन)",
    cropLabel: "फसल",

    footer: "AgroConnect AI • SIH 2026 प्रोटोटाइप • FastAPI + SQLite + HTML/CSS/JavaScript"
  }
};

function setNetwork(){
  const online=navigator.onLine;
  $("networkBadge").textContent=online?"● Online":"● Offline";
  $("networkBadge").className="badge "+(online?"online":"offline");
}
window.addEventListener("online",()=>{setNetwork();syncQueue()});
window.addEventListener("offline",setNetwork);

function applyLanguage(lang) {
  const t = translations[lang];

  $("heroTitle").textContent = t.heroTitle;
  $("heroText").textContent = t.heroText;

  document.querySelector(".eyebrow").textContent = t.eyebrow;
  document.querySelector(".hero-chip").textContent = t.offline;

  document.querySelector(".section-title h3").textContent = t.controlRoom;
  document.querySelector(".section-title .eyebrow").textContent = t.farmIntelligence;
  document.querySelector(".section-title .ghost").textContent = t.refresh;

  const metrics = document.querySelectorAll(".metric");

  if (metrics.length >= 4) {
    metrics[0].querySelector("span").textContent = t.crop;
    metrics[1].querySelector("span").textContent = t.moisture;
    metrics[2].querySelector("span").textContent = t.temperature;
    metrics[3].querySelector("span").textContent = t.bestMandi;

    metrics[1].querySelector("small").textContent = t.liveTelemetry;
    metrics[2].querySelector("small").textContent = t.microclimate;
  }

  const cards = document.querySelectorAll(".card");

  if (cards.length >= 6) {
    cards[0].querySelector("h3").textContent = t.soilClimate;
    cards[0].querySelector("p").textContent = t.latestSensor;

    cards[1].querySelector("h3").textContent = t.quickAdvisory;
    cards[1].querySelector("p").textContent = t.explainableRules;
    cards[1].querySelector(".primary").textContent = t.generateAdvisory;

    cards[2].querySelector("h3").textContent = t.leafHealth;
    cards[2].querySelector("p").textContent = t.uploadLeaf;
    cards[2].querySelector(".primary").textContent = t.runAI;

    cards[3].querySelector("h3").textContent = t.mandiIntelligence;
    cards[3].querySelector("p").textContent = t.regionalPrices;

    cards[4].querySelector("h3").textContent = t.harvestForecast;
    cards[4].querySelector("p").textContent = t.expectedHarvest;
    cards[4].querySelector(".primary").textContent = t.forecast;

    cards[5].querySelector("h3").textContent = t.buyerLogistics;
    cards[5].querySelector("p").textContent = t.connectHarvest;
    cards[5].querySelector(".primary").textContent = t.findBuyers;
  }

  const telemetryCard = document.querySelector(".telemetry-form");

  if (telemetryCard) {
    telemetryCard.querySelector("h3").textContent = t.mobileTelemetry;
    telemetryCard.querySelector("p").textContent = t.sensorIngestion;

    const buttons = telemetryCard.querySelectorAll("button");

    if (buttons[0]) buttons[0].textContent = t.sendTelemetry;
    if (buttons[1]) buttons[1].textContent = t.syncQueue;
  }

  const footer = document.querySelector("footer");
  if (footer) footer.textContent = t.footer;

  localStorage.setItem("agro_lang", lang);
}

$("language").addEventListener("change", e => {
  applyLanguage(e.target.value);
});

function setResult(id, html, cls="muted"){ $(id).className="result "+cls; $(id).innerHTML=html; }

async function api(url, options={}){
  const res=await fetch(url,options);
  if(!res.ok){throw new Error(await res.text())}
  return res.json();
}

async function loadDashboard(){
  try{
    const d=await api("/api/dashboard");
    $("mCrop").textContent=d.farm?.crop||"—";
    $("mArea").textContent=(d.farm?.area_acres||"—")+" acres";
    $("mMoisture").textContent=(d.telemetry?.soil_moisture??"—")+"%";
    $("mTemp").textContent=(d.telemetry?.temperature??"—")+"°C";
    const best=(d.market||[]).sort((a,b)=>b.price-a.price)[0];
    $("mMandi").textContent=best?.mandi||"—";
    $("mPrice").textContent=best?"₹"+best.price+"/q":"—";
    $("tMoisture").textContent=(d.telemetry?.soil_moisture??"—")+"%";
    $("tN").textContent=d.telemetry?.nitrogen??"—";
    $("tP").textContent=d.telemetry?.phosphorus??"—";
    $("tK").textContent=d.telemetry?.potassium??"—";
    $("tTemp").textContent=(d.telemetry?.temperature??"—")+"°C";
    $("tHumidity").textContent=(d.telemetry?.humidity??"—")+"%";
    renderMarket(d.market||[]);
  }catch(e){console.error(e)}
}

function renderMarket(rows){
  if(!rows.length){$("marketTable").textContent="No market data." ;return}
  $("marketTable").innerHTML=`<table class="market-table"><thead><tr><th>Mandi</th><th>Price/q</th><th>Arrival</th></tr></thead><tbody>`+
    rows.map(r=>`<tr><td>${r.mandi}</td><td><b>₹${r.price}</b></td><td>${r.arrival_tonnes} t</td></tr>`).join("")+
    `</tbody></table>`;
}

async function getAdvisory(){
  const t=await api("/api/dashboard");
  const x=t.telemetry;
  try{
    const r=await api("/api/advisory",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({
      farm_id:t.farm.id,crop:t.farm.crop,soil_moisture:x.soil_moisture,nitrogen:x.nitrogen,
      phosphorus:x.phosphorus,potassium:x.potassium,temperature:x.temperature,humidity:x.humidity
    })});
    const cls=r.severity==="Action"?"warn":"good";
    setResult("advisoryBox",`<b>Health score: ${r.health_score}/100</b><br>• ${r.actions.join("<br>• ")}<br><small>${r.note}</small>`,cls);
  }catch(e){setResult("advisoryBox",e.message,"danger")}
}

$("leafImage").addEventListener("change",()=>{
  const f=$("leafImage").files[0];
  if(!f)return;
  $("preview").src=URL.createObjectURL(f);
  $("previewWrap").classList.remove("hidden");
});

async function scanLeaf(){
  const f=$("leafImage").files[0];
  if(!f){setResult("diseaseResult","Please choose a leaf image first.","warn");return}
  const fd=new FormData(); fd.append("image",f); fd.append("farm_id","1");
  try{
    const r=await api("/api/ai/disease",{method:"POST",body:fd});
    setResult("diseaseResult",`<b>${r.diagnosis}</b> · ${r.confidence}% screening confidence<br>${r.explanation}<br><small>Action: ${r.recommended_action}</small>`,"good");
  }catch(e){setResult("diseaseResult",e.message,"danger")}
}

async function runForecast(){
  try{
    const r=await api("/api/forecast",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({
      crop:$("forecastCrop").value,area_acres:Number($("forecastArea").value)
    })});
    const y=r.yield;
    const prices=r.price;
    const peak=prices.reduce((a,b)=>a.expected_price>b.expected_price?a:b);
    setResult("forecastResult",`<b>${y.expected_yield_tonnes} tonnes</b> expected<br>Harvest window: <b>${y.window_start_days}–${y.window_end_days} days</b><br>7-day peak price signal: <b>₹${peak.expected_price}/q</b><br><small>Confidence: ${y.confidence}% · ${y.basis}</small>`,"good");
  }catch(e){setResult("forecastResult",e.message,"danger")}
}

async function matchBuyers(){
  try{
    const crop=$("buyerCrop").value, qty=Number($("buyerQty").value);
    const r=await api("/api/buyers/match",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({crop,quantity_tonnes:qty})});
    if(!r.matches.length){setResult("buyerResult","No matching buyer in the demo database.","warn");return}
    setResult("buyerResult",r.matches.slice(0,3).map((b,i)=>`<div class="rank"><div><b>${i+1}. ${b.buyer}</b><small>${b.location} · ${b.distance_km} km · demand ${b.demand_tonnes} t</small></div><strong>${b.match_score}%</strong></div>`).join(""),"good");
  }catch(e){setResult("buyerResult",e.message,"danger")}
}

function queueGet(){return JSON.parse(localStorage.getItem("agro_queue")||"[]")}
function queueSet(q){localStorage.setItem("agro_queue",JSON.stringify(q));$("queueBadge").textContent=q.length+" queued"}

async function sendTelemetry(){
  const payload={
    farm_id:1,soil_moisture:Number($("sMoisture").value),temperature:Number($("sTemp").value),
    humidity:Number($("sHumidity").value),nitrogen:Number($("sN").value),
    phosphorus:Number($("sP").value),potassium:Number($("sK").value)
  };
  if(!navigator.onLine){
    const q=queueGet();q.push(payload);queueSet(q);alert("Offline: telemetry saved on this device.");
    return;
  }
  try{await api("/api/telemetry",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)});await loadDashboard();alert("Telemetry stored successfully.");}
  catch(e){const q=queueGet();q.push(payload);queueSet(q);alert("Server unavailable: telemetry queued locally.")}
}

async function syncQueue(){
  const q=queueGet();
  if(!navigator.onLine||!q.length){queueSet(q);return}
  const remaining=[];
  for(const payload of q){
    try{await api("/api/telemetry",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)})}
    catch(e){remaining.push(payload)}
  }
  queueSet(remaining);if(!remaining.length)loadDashboard();
}

window.addEventListener("load",()=>{
  window.addEventListener("load", () => {

  const lang = localStorage.getItem("agro_lang") || "en";

  $("language").value = lang;

  applyLanguage(lang);

  setNetwork();

  queueSet(queueGet());

  loadDashboard();

});
  setNetwork();queueSet(queueGet());loadDashboard();
});

if ("serviceWorker" in navigator) navigator.serviceWorker.register("/static/sw.js").catch(()=>{});

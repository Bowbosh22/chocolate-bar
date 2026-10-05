import re,base64
s=open('/mnt/user-data/uploads/chocolate-bar-braza-demo-v2.html',encoding='utf-8').read()
vid=base64.b64encode(open('build/hero.mp4','rb').read()).decode()
pst=base64.b64encode(open('build/poster.jpg','rb').read()).decode()

# 1. polices
s=re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Bodoni[^"]*" rel="stylesheet">',
 '<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">',s)
s=s.replace('--display:"Bodoni Moda",Georgia,serif;','--display:"Poppins",system-ui,sans-serif;\n  --script:"Pacifico",cursive;\n  --rose:#F8BFC4;\n  --rose-2:#FCE3E6;\n  --framboise-2:#D6336C;\n  --blanc:#FFF8F5;')
s=s.replace('--body:"Jost",system-ui,sans-serif;','--body:"Poppins",system-ui,sans-serif;')
s=s.replace('<title>Chocolate Bar Braza — Créations chocolatées à Brazzaville</title>','<title>Chocolate Bar Braza — Chocolaterie-crêperie à Brazzaville</title>')

# 2. CSS bandeau/en-tête/hero -> nouveau
a=s.index('/* ---------- bandeau + en-tête ---------- */')
b=s.index('/* ---------- créations ---------- */')
newcss='''/* ---------- bandeau + en-tête ---------- */
.demo-ribbon{position:relative;z-index:30;background:var(--cacao);color:var(--ivoire);font-size:13px;text-align:center;padding:8px 16px}
.demo-ribbon b{font-weight:600}
header.top{position:absolute;top:34px;left:0;right:0;z-index:20;padding-top:26px}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;width:min(1280px,100% - 48px)}
.wordmark{text-decoration:none;color:var(--cacao);display:flex;flex-direction:column;line-height:1}
.wordmark .w1{font-family:var(--script);font-size:40px;letter-spacing:.005em}
.wordmark .w2{font-weight:600;font-size:14px;letter-spacing:.14em;margin:-2px 0 0 auto;padding-right:6px}
nav.main{display:flex;gap:34px;align-items:center;font-size:14px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
nav.main a{text-decoration:none;color:var(--cacao)}
nav.main a:hover{color:var(--framboise-2)}
.cartlink{display:inline-flex;align-items:center;gap:8px;color:var(--cacao);text-decoration:none;font-weight:700}
.cartlink svg{width:26px;height:26px}
.order{background:var(--framboise-2);color:#fff;text-decoration:none;font-weight:700;font-size:14px;letter-spacing:.04em;text-transform:uppercase;padding:15px 24px;border-radius:12px;box-shadow:0 4px 0 #a72350;transition:transform .15s,box-shadow .15s}
.order:hover{transform:translateY(2px);box-shadow:0 2px 0 #a72350}

/* ---------- hero ---------- */
.hero{position:relative;min-height:calc(100svh - 34px);overflow:hidden;background:var(--rose)}
.hero svg.waves{position:absolute;inset:0;width:100%;height:100%}
.hero .vwrap{position:absolute;left:-7%;top:24%;width:46%;max-width:640px;aspect-ratio:4/5;transform:rotate(-7deg);z-index:2}
.hero .vwrap::before{content:"";position:absolute;inset:-14px;border-radius:44px;background:#F9B79F;transform:rotate(5deg)}
.hero .vid{position:relative;width:100%;height:100%;border-radius:36px;overflow:hidden;box-shadow:0 30px 60px -24px rgba(59,29,20,.6);background:#3b1d14}
.hero video{width:100%;height:100%;object-fit:cover;display:block}
.hero .copy{position:absolute;z-index:3;left:44%;right:5%;top:42%;text-align:center}
.hero h1{font-family:var(--display);font-weight:800;font-size:clamp(34px,4.6vw,64px);line-height:1.08;letter-spacing:-.025em;color:var(--cacao)}
.hero h1 em{display:block;font-family:var(--script);font-style:normal;font-weight:400;color:var(--framboise-2);font-size:1.18em;line-height:1.05;margin:-.04em 0 -.02em;letter-spacing:0}
.hero p.sub{margin:22px auto 30px;max-width:30em;font-size:clamp(16px,1.5vw,21px);font-weight:600;color:#9b4a5f}
.cta-main{display:inline-flex;align-items:center;gap:18px;background:var(--framboise-2);color:#fff;text-decoration:none;font-weight:700;font-size:17px;padding:17px 26px;border-radius:12px;box-shadow:0 5px 0 #a72350;transition:transform .15s,box-shadow .15s}
.cta-main:hover{transform:translateY(2px);box-shadow:0 3px 0 #a72350}
.cta-main i{width:1px;height:22px;background:rgba(255,255,255,.7)}

'''
s=s[:a]+newcss+s[b:]

# 3. HTML header + hero
a=s.index('<header class="top">')
b=s.index('<section class="creations"')
newhtml='''<header class="top">
  <div class="wrap">
    <a class="wordmark" href="#" aria-label="Chocolate Bar Braza, accueil"><span class="w1">chocolate</span><span class="w2">bar braza</span></a>
    <nav class="main" aria-label="Navigation principale">
      <a class="hide-s" href="#creations">Créations</a>
      <a class="hide-s" href="#douceur">Ma douceur</a>
      <a class="hide-s" href="#carte">La carte</a>
      <a class="hide-s" href="#venir">Contact</a>
      <a class="cartlink" href="#carte" aria-label="Voir la carte et ma commande">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M2 3h3l.6 2H21l-2.2 8.2a2 2 0 0 1-1.9 1.5H8.4l.4 1.3H19v2H7.3L4.4 5H2zM9 20.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm9 0a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
        <span id="cartCount">0</span>
      </a>
      <a class="order" href="https://wa.me/242064141414?text=Bonjour%20Chocolate%20Bar%2C%20j%27aimerais%20passer%20une%20commande." target="_blank" rel="noopener">Commander</a>
    </nav>
  </div>
</header>

<main>
  <section class="hero" aria-label="Accueil">
    <svg class="waves" viewBox="0 0 1440 900" preserveAspectRatio="none" aria-hidden="true">
      <path d="M0,540 C180,490 340,440 560,448 C800,458 960,540 1180,530 C1300,524 1390,500 1440,478 L1440,900 L0,900 Z" fill="#FFF8F5"/>
      <ellipse cx="700" cy="930" rx="250" ry="170" fill="#F9B79F"/>
      <ellipse cx="1260" cy="965" rx="320" ry="120" fill="#EDBBCB"/>
    </svg>
    <div class="vwrap">
      <div class="vid">
        <video id="heroVideo" autoplay muted loop playsinline preload="auto" poster="data:image/jpeg;base64,__POSTER__" aria-label="Chocolat fondu nappant des bouchées">
          <source src="data:video/mp4;base64,__VIDEO__" type="video/mp4">
        </video>
      </div>
    </div>
    <div class="copy">
      <h1>Nous sommes <em>Chocolate Bar</em> Braza.</h1>
      <p class="sub">Chocolaterie-crêperie au cœur de Brazzaville : crêpes, gaufres, pancakes et créations au chocolat.</p>
      <a class="cta-main" href="#creations">Découvrir les créations <i></i><span aria-hidden="true">→</span></a>
    </div>
  </section>

  '''
s=s[:a]+newhtml+s[b:]

# 4. JS hero + panier
a=s.index('/* ---------- hero : vidéo si disponible')
b=s.index('</script>',a)
newjs='''/* ---------- hero : vidéo ---------- */
const video = document.getElementById("heroVideo");
if(matchMedia("(prefers-reduced-motion: reduce)").matches){
  video.removeAttribute("autoplay"); video.pause();
} else {
  const p = video.play(); if(p && p.catch) p.catch(()=>{});
}
'''
s=s[:a]+newjs+s[b:]
s=s.replace('if(!entries.length){ el.classList.remove("show"); return; }','if(!entries.length){ el.classList.remove("show"); setCart(0); return; }')
s=s.replace('  document.getElementById("basketSum").textContent','  setCart(count);\n  document.getElementById("basketSum").textContent',1)
s=s.replace('function renderBasket(){','function setCart(n){ const c=document.getElementById("cartCount"); if(c) c.textContent=n; }\nfunction renderBasket(){',1)

# 5. surcharges de style pour les sections suivantes
over='''
/* ---------- harmonisation avec l'accueil ---------- */
.creations{background:var(--blanc);color:var(--cacao)}
.creations .sec-head p{opacity:.72}
.card{color:var(--ivoire)}
.card.big{flex-direction:row}
.card.big .media{aspect-ratio:auto;flex:1.25;min-height:0}
.card.big .media svg{width:min(78%,360px)}
.card.big .info{flex:.75;align-content:end;padding:30px}
.card.big .txt{min-height:5.2em}
.basket{visibility:hidden;transition:transform .4s cubic-bezier(.2,.9,.3,1),visibility 0s .4s}
.basket.show{visibility:visible;transition:transform .4s cubic-bezier(.2,.9,.3,1)}
.douceur{background:var(--rose-2)}
.stage{background:#fff}
.venir{background:var(--rose-2)}
.sec-head h2,.douceur h2,.venir h2,.stage h3{font-weight:800;letter-spacing:-.025em}
.info h3,.item h3,.venir .cta h3{font-weight:700;letter-spacing:-.01em}
.info h3{font-size:24px}
.btn,.add,.opt,.tab{font-weight:600}
.btn-dark:hover{background:var(--framboise-2);color:#fff}
.venir dt{color:var(--framboise-2)}
@media (max-width:900px){
  .card.big{flex-direction:column}
  .card.big .media{aspect-ratio:1/.82;flex:none}
  .card.big .info{padding:24px 26px 26px}
  header.top{position:relative;top:auto;padding:16px 0;background:var(--rose)}
  .hide-s{display:none}
  .wordmark .w1{font-size:32px}
  .order{padding:12px 16px;font-size:12px}
  .hero{min-height:0;display:flex;flex-direction:column;background:var(--rose)}
  .hero svg.waves{display:none}
  .hero .copy{position:relative;left:auto;right:auto;top:auto;padding:28px 24px 0;order:1}
  .hero .vwrap{position:relative;left:auto;top:auto;width:78%;max-width:none;margin:56px auto 0;transform:rotate(-4deg);order:2}
  .hero{padding-bottom:70px}
  .hero::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:48px;background:var(--blanc);border-radius:48px 48px 0 0 / 40px 40px 0 0}
}
'''
s=s.replace('</style>',over+'</style>',1)
s=s.replace('__VIDEO__',vid).replace('__POSTER__',pst)
open('chocolate-bar-braza-demo-v3.html','w',encoding='utf-8').write(s)
print(len(s)//1024,'Ko')

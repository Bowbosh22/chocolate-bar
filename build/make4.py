import re,base64
s=open('chocolate-bar-braza-demo-v3.html',encoding='utf-8').read()
img=base64.b64encode(open('build/fountain.jpg','rb').read()).decode()

# polices
s=re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Pacifico[^"]*" rel="stylesheet">',
 '<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Archivo:wdth,wght@62..125,400..900&display=swap" rel="stylesheet">',s)
s=s.replace('--display:"Poppins",system-ui,sans-serif;','--display:"Archivo",system-ui,sans-serif;')
s=s.replace('--body:"Poppins",system-ui,sans-serif;','--body:"Archivo",system-ui,sans-serif;\n  --slab:"Alfa Slab One",Georgia,serif;')

# CSS en-tête + hero
a=s.index('/* ---------- bandeau + en-tête ---------- */')
b=s.index('/* ---------- créations ---------- */')
css='''/* ---------- annonce, en-tête, bandeau ---------- */
.demo-ribbon{position:relative;z-index:30;background:var(--rose-2);color:var(--cacao);font-size:13px;text-align:center;padding:7px 16px}
.demo-ribbon b{font-weight:700}
.announce{background:#111;color:#fff;text-align:center;font-weight:800;font-stretch:88%;font-size:14px;letter-spacing:.01em;text-transform:uppercase;padding:13px 16px}
.announce a{margin-left:10px;text-decoration:underline;text-underline-offset:3px}
header.site{background:#fff;color:#111;position:relative;z-index:20}
header.site .bar{width:min(1560px,100% - 48px);margin:auto;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:16px 0 6px}
header.site .left,header.site .right{display:flex;align-items:center;gap:18px}
header.site .right{justify-content:flex-end}
header.site svg{width:26px;height:26px;display:block}
.iconbtn{background:none;border:0;color:#111;cursor:pointer;padding:4px;display:inline-flex;align-items:center;text-decoration:none}
.logo{display:inline-block;background:#111;color:#fff;font-family:var(--slab);font-size:clamp(22px,2.6vw,32px);letter-spacing:.02em;line-height:1;padding:9px 14px 8px;border-radius:4px;transform:rotate(-2.5deg);box-shadow:4px 4px 0 var(--framboise-2);text-decoration:none;text-transform:uppercase;white-space:nowrap}
.count{font-weight:800;font-size:15px;margin-left:6px}
nav.menu{display:flex;justify-content:center;gap:clamp(22px,4vw,64px);padding:14px 24px 20px;font-weight:800;font-stretch:88%;font-size:16px;text-transform:uppercase;letter-spacing:.005em}
nav.menu a{text-decoration:none;color:#111;padding:4px 0;border-bottom:3px solid transparent}
nav.menu a:hover{border-color:var(--framboise-2)}
.burger{display:none}
.marquee{background:#111;color:#fff;overflow:hidden;white-space:nowrap;padding:15px 0;font-family:var(--slab);font-size:19px;letter-spacing:.03em;text-transform:uppercase}
.marquee .track{display:inline-flex;gap:64px;animation:slide 38s linear infinite;will-change:transform}
.marquee .track span{display:inline-block}
@keyframes slide{to{transform:translateX(-50%)}}

/* ---------- hero ---------- */
.hero4{background:#fff;padding:34px 0 70px}
.hero4 .inner{width:min(1560px,100% - 48px);margin:auto;display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:36px;align-items:center}
.copy4{text-align:center;padding:0 clamp(0px,2.4vw,44px)}
.copy4 h1{font-family:var(--display);font-weight:900;font-stretch:80%;font-size:clamp(40px,5.2vw,84px);line-height:.94;letter-spacing:-.035em;text-transform:uppercase;color:#111;margin-bottom:24px}
.copy4 p{font-size:clamp(16px,1.35vw,19px);line-height:1.45;max-width:27em;margin:0 auto 30px;color:#222}
.btn-black{display:inline-block;background:#111;color:#fff;font-weight:800;font-stretch:88%;font-size:17px;text-transform:uppercase;text-decoration:none;padding:19px 30px;border-radius:10px;transition:background .2s,transform .15s}
.btn-black:hover{background:var(--framboise-2);transform:translateY(-2px)}
.panels{display:grid;grid-template-columns:1fr 1fr;gap:clamp(12px,1.6vw,24px)}
.panel{position:relative;aspect-ratio:4/5;border-radius:8px;overflow:hidden;background:#3b1d14}
.panel video,.panel img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.panel img{object-position:50% 38%}

'''
s=s[:a]+css+s[b:]

# HTML
a=s.index('<header class="top">')
b=s.index('<section class="creations"')
html='''<div class="announce">Les créations de la semaine sont là. <a href="#creations">Découvrez-les</a></div>

<header class="site">
  <div class="bar">
    <div class="left">
      <button class="iconbtn burger" id="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
      <a class="iconbtn" href="#venir" aria-label="Nous trouver">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.2A7 7 0 0 1 19 9.8C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.6"/></svg>
      </a>
    </div>
    <a class="logo" href="#" aria-label="Chocolate Bar Braza, accueil">Chocolate Bar</a>
    <div class="right">
      <a class="iconbtn" href="#carte" aria-label="Voir la carte et ma commande">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M3 4h2.5l2.2 11h10.6l2-8H6.2"/><circle cx="9" cy="19.5" r="1.4"/><circle cx="17" cy="19.5" r="1.4"/></svg>
        <span class="count" id="cartCount">0</span>
      </a>
    </div>
  </div>
  <nav class="menu" id="menu" aria-label="Navigation principale">
    <a href="#creations">Créations</a>
    <a href="#douceur">Ma douceur</a>
    <a href="#carte">La carte</a>
    <a href="#venir">Contact</a>
    <a href="https://wa.me/242064141414?text=Bonjour%20Chocolate%20Bar%2C%20j%27aimerais%20passer%20une%20commande." target="_blank" rel="noopener">Commander</a>
  </nav>
</header>

<div class="marquee" aria-hidden="true"><div class="track" id="track"><span>Chocolat fondant, crêpes et gaufres à Brazzaville</span><span>Chocolat fondant, crêpes et gaufres à Brazzaville</span><span>Chocolat fondant, crêpes et gaufres à Brazzaville</span><span>Chocolat fondant, crêpes et gaufres à Brazzaville</span></div></div>

<main>
  <section class="hero4" aria-label="Accueil">
    <div class="inner">
      <div class="copy4">
        <h1>Laissez-nous créer votre prochaine obsession.</h1>
        <p>Chocolaterie-crêperie au cœur de Brazzaville. Crêpes, gaufres, pancakes et créations nappées de chocolat, préparés sous vos yeux.</p>
        <a class="btn-black" href="#creations">Découvrir les créations</a>
      </div>
      <div class="panels">
        <div class="panel">
          <video id="heroVideo" autoplay muted loop playsinline preload="auto" poster="data:image/jpeg;base64,__POSTER__" aria-label="Chocolat fondu nappant des bouchées">
            <source src="data:video/mp4;base64,__VIDEO__" type="video/mp4">
          </video>
        </div>
        <div class="panel">
          <img src="data:image/jpeg;base64,__IMG__" alt="Fontaine de chocolat en service au comptoir de Chocolate Bar">
        </div>
      </div>
    </div>
  </section>

  '''
# récupérer les données vidéo/poster déjà intégrées dans v3
m=re.search(r'poster="data:image/jpeg;base64,([^"]+)"',s[a:b]); poster=m.group(1)
m=re.search(r'<source src="data:video/mp4;base64,([^"]+)"',s[a:b]); vid=m.group(1)
html=html.replace('__POSTER__',poster).replace('__VIDEO__',vid).replace('__IMG__',img)
s=s[:a]+html+s[b:]

# mobile : remplace les règles de l'ancien hero
i=s.index('  header.top{position:relative;top:auto')
j=s.index('\n}\n</style>',i)
mobile='''  .announce{font-size:12px;padding:11px 12px}
  .logo{font-size:19px;padding:8px 11px 7px}
  header.site .left,header.site .right{gap:8px}
  header.site .bar{padding:12px 0 12px}
  .burger{display:inline-flex}
  nav.menu{display:none;flex-direction:column;align-items:center;gap:6px;padding:6px 24px 18px;border-top:1px solid #eee}
  nav.menu.open{display:flex}
  nav.menu a{padding:10px 0}
  .marquee{font-size:15px;padding:12px 0}
  .hero4{padding:26px 0 48px}
  .hero4 .inner{grid-template-columns:1fr;gap:28px}
  .copy4 h1{font-size:clamp(38px,11vw,56px)}
  .panels{gap:10px}'''
s=s[:i]+mobile+s[j:]

# JS : menu + marquee
k=s.rindex('</script>')
js='''
/* ---------- menu mobile + bandeau défilant ---------- */
const burger=document.getElementById("burger"), menu=document.getElementById("menu");
burger.addEventListener("click",()=>{ const o=menu.classList.toggle("open"); burger.setAttribute("aria-expanded",o); });
menu.querySelectorAll("a").forEach(a=>a.addEventListener("click",()=>{ menu.classList.remove("open"); burger.setAttribute("aria-expanded","false"); }));
const track=document.getElementById("track"); track.innerHTML += track.innerHTML;
if(matchMedia("(prefers-reduced-motion: reduce)").matches){ track.style.animation="none"; }
'''
s=s[:k]+js+s[k:]
open('chocolate-bar-braza-demo-v4.html','w',encoding='utf-8').write(s)
print(len(s)//1024,'Ko')

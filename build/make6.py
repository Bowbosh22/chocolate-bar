import base64,html
s=open('/home/claude/chocolate-bar-braza-demo-v5.html',encoding='utf-8').read()

ITEMS=[
 ("Crêpes tagliatelle","Des rubans de crêpe dorés, une boule de glace, et deux sauces chocolat versées juste avant de servir.",4500,"Crêpes en rubans nappées de chocolat au lait et de chocolat blanc, avec une boule de glace"),
 ("Marbré fraise","Un gâteau au chocolat, une crème légère, un nappage marbré et une fraise posée sur le dessus.",4000,"Gâteau au chocolat marbré surmonté d'une fraise"),
 ("Zébré fraise-banane","Un glaçage zébré chocolat et vanille qui cache des tranches de fraise et de banane.",4500,"Gâteau zébré avec fraises et banane sur une planche en bois"),
 ("Le grand drip","Des étages de crème et de fraises sous une cascade de chocolat fondu.",5000,"Grand gâteau au chocolat dégoulinant avec fraises et chantilly"),
 ("Oreo waffle","Une gaufre moelleuse, une crème onctueuse aux morceaux d'Oreo et une sauce chocolat fondante.",3500,"Gaufre à l'Oreo nappée de sauce chocolat"),
 ("Milkshake vanille","Onctueux, frais et délicieux, coiffé de chantilly et de filets de chocolat.",3500,"Milkshake vanille avec chantilly et chocolat"),
 ("Milkshake Octobre Rose","Une touche de rose, beaucoup d'espoir : le milkshake qui soutient Octobre Rose.",3500,"Milkshake rose avec chantilly et coulis de fruits rouges"),
]
cards=""
for i,(n,t,p,alt) in enumerate(ITEMS,1):
    b=base64.b64encode(open(f'/home/claude/build/d{i}.jpg','rb').read()).decode()
    pr=f"{p:,}".replace(","," ")+" FCFA"
    cards+=f'''<article class="dcard">
        <div class="ph"><img src="data:image/jpeg;base64,{b}" alt="{html.escape(alt)}" loading="lazy"></div>
        <div class="tx"><h3>{html.escape(n)}</h3><p>{html.escape(t)}</p><span class="pr">{pr}</span>
        <button type="button" data-name="{html.escape(n)}" data-price="{p}">Ajouter à ma commande</button></div>
      </article>
      '''

section=f'''<section class="desserts" id="desserts" aria-label="Nos desserts">
    <div class="dh">
      <h2>Nos desserts</h2>
      <p>Préparés sur place et nappés de chocolat. Faites défiler pour tout voir.</p>
    </div>
    <div class="carousel">
      <button class="arrow prev" id="dPrev" type="button" aria-label="Desserts précédents"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button>
      <div class="rail" id="rail" tabindex="0" aria-label="Carrousel de desserts">
      {cards}</div>
      <button class="arrow next" id="dNext" type="button" aria-label="Desserts suivants"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>
    </div>
    <div class="progress" aria-hidden="true"><i id="dThumb"></i></div>
  </section>

  '''
a=s.index('<section class="hero4"')
s=s[:a]+section+s[a:]

css='''
/* ---------- carrousel desserts ---------- */
.desserts{background:#fff;padding:34px 0 40px}
.dh{width:min(1560px,100% - 48px);margin:0 auto 26px;display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.dh h2{font-weight:900;font-stretch:80%;text-transform:uppercase;font-size:clamp(36px,4.6vw,68px);letter-spacing:-.03em;line-height:.95;color:var(--cacao)}
.dh p{max-width:24em;color:var(--cacao);opacity:.78;font-size:16px}
.carousel{position:relative}
.rail{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding:8px 24px 30px;scrollbar-width:none;outline-offset:-4px}
.rail::-webkit-scrollbar{display:none}
.dcard{flex:0 0 clamp(270px,26vw,420px);scroll-snap-align:start;background:#fff;border-radius:8px;box-shadow:0 4px 22px rgba(90,45,29,.14);display:flex;flex-direction:column;overflow:hidden}
.dcard .ph{aspect-ratio:4/5;background:#FCEBDD;overflow:hidden}
.dcard img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .7s}
.dcard:hover img{transform:scale(1.04)}
.dcard .tx{padding:20px 18px 18px;text-align:center;display:flex;flex-direction:column;flex:1}
.dcard h3{font-weight:900;font-stretch:88%;text-transform:uppercase;font-size:20px;letter-spacing:-.005em;color:var(--cacao);margin-bottom:8px;line-height:1.1}
.dcard p{font-size:16px;line-height:1.42;color:#3a2a24;margin-bottom:14px;flex:1}
.dcard .pr{font-weight:800;color:var(--framboise-2);margin-bottom:14px}
.dcard button{background:var(--cacao);color:#fff;border:0;border-radius:8px;padding:17px 12px;font:800 15px/1 var(--body);font-stretch:88%;text-transform:uppercase;cursor:pointer;transition:background .2s}
.dcard button:hover{background:var(--framboise-2)}
.arrow{position:absolute;top:34%;z-index:3;width:72px;height:72px;border:0;background:var(--framboise-2);color:#fff;cursor:pointer;display:grid;place-items:center;transition:background .2s}
.arrow.prev{left:0;border-radius:0 6px 6px 0}
.arrow.next{right:0;border-radius:6px 0 0 6px}
.arrow:hover{background:#b02255}
.arrow svg{width:28px;height:28px}
.progress{width:min(1560px,100% - 48px);height:8px;margin:0 auto;background:#F8BFC4;border-radius:8px;position:relative;overflow:hidden}
.progress i{position:absolute;left:0;top:0;bottom:0;width:30%;background:var(--framboise-2);border-radius:8px;transition:left .15s linear,width .15s}
@media (max-width:900px){
  .dcard{flex-basis:78vw}
  .arrow{width:46px;height:56px;top:30%}
  .arrow svg{width:22px;height:22px}
  .rail{padding:8px 16px 26px}
}
@media (prefers-reduced-motion:reduce){ .rail{scroll-behavior:auto} .dcard img{transition:none} }
'''
k=s.index('</style>')
s=s[:k]+css+s[k:]

js='''
/* ---------- carrousel desserts ---------- */
(function(){
  const rail=document.getElementById("rail"), thumb=document.getElementById("dThumb");
  const prev=document.getElementById("dPrev"), next=document.getElementById("dNext");
  const step=()=>{ const c=rail.querySelector(".dcard"); return c.getBoundingClientRect().width+18; };
  function upd(){
    const max=rail.scrollWidth-rail.clientWidth, ratio=rail.clientWidth/rail.scrollWidth;
    thumb.style.width=(ratio*100)+"%";
    thumb.style.left=((max>0?rail.scrollLeft/max:0)*(100-ratio*100))+"%";
  }
  function go(dir){
    const max=rail.scrollWidth-rail.clientWidth;
    if(dir>0 && rail.scrollLeft>=max-4) rail.scrollTo({left:0});
    else if(dir<0 && rail.scrollLeft<=4) rail.scrollTo({left:max});
    else rail.scrollBy({left:dir*step()});
  }
  prev.addEventListener("click",()=>{ go(-1); stop(); });
  next.addEventListener("click",()=>{ go(1); stop(); });
  rail.addEventListener("scroll",upd,{passive:true});
  addEventListener("resize",upd); upd();
  rail.addEventListener("keydown",e=>{ if(e.key==="ArrowRight"){go(1);e.preventDefault();} if(e.key==="ArrowLeft"){go(-1);e.preventDefault();} });
  rail.querySelectorAll(".dcard button").forEach(b=>b.addEventListener("click",()=>add(b.dataset.name,Number(b.dataset.price))));
  /* défilement automatique doux, arrêté au survol, au toucher ou si l'utilisateur interagit */
  let timer=null;
  const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
  function start(){ if(reduce||timer) return; timer=setInterval(()=>go(1),4200); }
  function stop(){ clearInterval(timer); timer=null; }
  const box=document.getElementById("desserts");
  box.addEventListener("mouseenter",stop); box.addEventListener("mouseleave",start);
  box.addEventListener("focusin",stop); box.addEventListener("touchstart",stop,{passive:true});
  if("IntersectionObserver" in window){
    new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting?start():stop()),{threshold:.35}).observe(box);
  }
})();
'''
k=s.rindex('</script>')
s=s[:k]+js+s[k:]

# navigation et liens
s=s.replace('<a href="#creations">Créations</a>','<a href="#desserts">Desserts</a>\n    <a href="#creations">À l\'intérieur</a>')
s=s.replace('<a class="btn-black" href="#creations">','<a class="btn-black" href="#desserts">')
s=s.replace('<a href="#creations">Découvrez-les</a>','<a href="#desserts">Découvrez-les</a>')
s=s.replace('<h2>Les créations</h2>','<h2>À l\'intérieur</h2>')
open('/home/claude/chocolate-bar-braza-demo-v6.html','w',encoding='utf-8').write(s)
print(len(s)//1024,'Ko')

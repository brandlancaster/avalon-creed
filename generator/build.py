# Avalon Creed site generator. Sibling of the Order of Avalon v2 generator (/workspace/avalon-media/v2-build/build.py).
import os, re, json, html as H, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import doctrine as D
from content import *
OUT='/workspace/avalon-creed-site'
PAGES=[]
import shutil
shutil.copytree(os.path.dirname(os.path.abspath(__file__))+'/static',OUT,dirs_exist_ok=True)

NAV=[('The Creed','/creed/'),('The Way','/way/'),('FAQ','/faq/'),('Where We Stand','/positions/'),('The Order','/order/'),('Contact','/contact/')]
SUB={
 'creed':('The Creed','/creed/',[]),
 'way':('The Way','/way/',[('The Code','/way/code/'),('The Virtues','/way/virtues/'),('The Tenets','/way/tenets/')]),
 'faq':('FAQ','/faq/',[]), 'positions':('Where We Stand','/positions/',[]),
 'order':('The Order','/order/',[]), 'support':('Support','/support/',[]), 'contact':('Contact','/contact/',[]),
}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">'

def header(section):
    items=''
    for name,href in NAV:
        cur=' aria-current="page"' if (section and href==f'/{section}/') else ''
        items+=f'<li><a href="{href}"{cur}>{name}</a></li>'
    cur=' aria-current="page"' if section=='support' else ''
    items+=f'<li class="nav-support"><a href="/support/"{cur}>Support</a></li>'
    items+=f'<li class="nav-cta"><a href="{OOA}/join/" rel="noopener">Join the Order</a></li>'
    return f'''<a class="skip-link" href="#content">Skip to content</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="/"><picture><source srcset="/assets/seal-96.webp 1x, /assets/seal-192.webp 2x" type="image/webp"><img class="seal" src="/assets/seal-96.png" srcset="/assets/seal-96.png 1x, /assets/seal-192.png 2x" width="96" height="96" alt="Seal of the Avalon Creed"></picture><span class="wordmark"><span class="name">Avalon Creed</span><span class="latin">Credo Avallonis</span></span></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
<nav class="site-nav" id="site-nav" aria-label="Primary"><ul>{items}</ul></nav>
</div></header>'''

CALL=f'''<section class="call" aria-labelledby="call-h"><div class="wrap">
<p class="eyebrow">The Avalon Creed</p><h2 id="call-h">Walk the Way.</h2>
<p>The path is difficult. The standard is high. The purpose is clear. Read the Creed in full, and if it calls to you, answer.</p>
<div class="buttons center"><a class="button primary" href="/creed/">Read the Creed</a><a class="button" href="/support/">Support Avalon</a><a class="button ext" href="{OOA}/" rel="noopener">The Order of Avalon</a></div>
</div></section>'''

def footer():
    cols=('<div><h4><a href="/creed/">The Creed</a></h4><ul><li><a href="/creed/">Creed of Avalon</a></li><li><a href="/creed/#religion">Why a religion</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/positions/">Where We Stand</a></li></ul></div>'
          '<div><h4><a href="/way/">The Way</a></h4><ul><li><a href="/way/code/">The Code</a></li><li><a href="/way/virtues/">The Virtues</a></li><li><a href="/way/tenets/">The Tenets</a></li></ul></div>'
          f'<div><h4><a href="/order/">The Order</a></h4><ul><li><a href="/order/">About the Order</a></li><li><a href="{OOA}/">orderofavalon.com</a></li><li><a href="{OOA}/join/">Join the Order</a></li></ul></div>'
          f'<div><h4>Connect</h4><ul><li><a href="/support/">Support Avalon</a></li><li><a href="{GSG}" target="_blank" rel="noopener">Give on GiveSendGo</a></li><li><a href="/contact/">Contact</a></li></ul></div>')
    return f'''<footer class="site-footer"><div class="wrap"><div class="footer-grid">{cols}</div>
<div class="footer-base"><span>Avalon Creed · <span class="latin">Credo Avallonis</span></span><span>Copyright 2026 Avalon Creed. Belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment.</span></div></div></footer>'''

JS='''<script>
(function(){var b=document.querySelector('.nav-toggle'),n=document.getElementById('site-nav');if(!b||!n)return;
b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'Close':'Menu';});})();
</script>'''

def doc(path,title,desc,body,section=None,fname='index.html'):
    full=f'{title} | Avalon Creed' if (path!='/' or fname!='index.html') else 'Avalon Creed | Belief in Modern Chivalry'
    out=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(full)}</title>
<meta name="description" content="{H.escape(desc)}">
<meta name="theme-color" content="#150706">
<meta property="og:type" content="website"><meta property="og:site_name" content="Avalon Creed">
<meta property="og:title" content="{H.escape(full)}"><meta property="og:description" content="{H.escape(desc)}"><meta property="og:image" content="/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/assets/favicon-32.png" type="image/png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="/css/styles.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body>
{header(section)}
<main id="content" tabindex="-1">
{body}
</main>
{CALL}
{footer()}
{JS}
</body>
</html>
'''
    d=OUT+path; os.makedirs(d,exist_ok=True)
    open(d+fname,'w',encoding='utf-8').write(out)
    PAGES.append((path if fname=='index.html' else path+fname,full))

def inner(path,section,title,lede,content,desc=None,eyebrow=None):
    st,sh,subs=SUB[section]
    crumbs=f'<a href="/">Home</a> / ' + (f'<a href="{sh}">{st}</a> / {H.escape(title)}' if path!=sh else H.escape(st))
    sub=''
    if subs:
        lis=f'<li><a href="{sh}"{" aria-current=\"page\"" if path==sh else ""}>Overview</a></li>'
        for n,u in subs: lis+=f'<li><a href="{u}"{" aria-current=\"page\"" if u==path else ""}>{n}</a></li>'
        sub=f'<nav class="subnav" aria-label="{st}"><ul>{lis}</ul></nav>'
    body=f'''<div class="page-hero"><div class="wrap"><p class="crumbs">{crumbs}</p>
{f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ''}<h1>{title}</h1><p class="lede">{lede}</p></div></div>
{sub}
<div class="content"><div class="wrap">{content}</div></div>'''
    doc(path,title,desc or re.sub('<[^>]+>','',lede),body,section)

def cards(items,cls='grid'):
    s=f'<div class="{cls}">'
    for it in items:
        k=f'<p class="kicker">{it[3]}</p>' if len(it)>3 and it[3] else ''
        ext=it[2].startswith('http')
        s+=f'<a class="card" href="{it[2]}"{" rel=\"noopener\"" if ext else ""}>{k}<h3>{it[0]}</h3><p>{it[1]}</p><span class="textlink">{"Visit orderofavalon.com" if ext else "Read more"}</span></a>'
    return s+'</div>'
def pillars(items): return '<div class="pillars">'+''.join(f'<div class="pillar"><h3>{a}</h3><p>{b}</p></div>' for a,b in items)+'</div>'
def faq(items): return '<div class="faq">'+''.join(f'<details><summary>{q}</summary><div><p>{a}</p></div></details>' for q,a in items)+'</div>'
def lines(ls): return ''.join(f'<p>{H.escape(l)}</p>' for l in ls)

# ---- doctrine with resyncs ----
def fix_doctrine(h):
    h=h.replace('href="/the-code"','href="/way/code/"').replace('href="/the-virtues"','href="/way/virtues/"').replace('href="/the-tenets"','href="/way/tenets/"').replace('href="/faqs"','href="/faq/"')
    return h
code_html=fix_doctrine(D.code()).replace('avoid damage or agression unless','avoid damage or aggression unless')
tenets_html=fix_doctrine(D.tenets())
assert tenets_html.count(SOBRIETY_OLD)==1, 'sobriety tenet source changed'
tenets_html=tenets_html.replace(SOBRIETY_OLD,SOBRIETY_NEW)
intro,groups=D.virtues()
tiles=''.join(f'<a href="/way/virtues/#{a.lower()}">{a}<span>{", ".join(p for p,_ in ps)}</span></a>' for (a,b),ps in groups)
PILLARS3=[('Train the Body','Practical physical prowess, kept strong through daily training.'),('Train the Mind','A lifelong student: study, research, create, and apply what you learn.'),('Train the Spirit','Meditation, and contemplation of the Virtues and the Way.')]

# ---------------- HOME ----------------
home=f'''
<section class="hero" aria-label="Avalon Creed"><picture><source type="image/webp" srcset="/assets/banner-1200.webp 1200w, /assets/banner-2304.webp 2304w" sizes="(max-width:1200px) 100vw, 72rem"><img src="/assets/banner-2304.jpg" srcset="/assets/banner-1200.jpg 1200w, /assets/banner-2304.jpg 2304w" sizes="(max-width:1200px) 100vw, 72rem" width="2304" height="864" alt="The seal of the Avalon Creed, a winged sword crowned with a tower, in gold on crimson"></picture></section>
<section class="hero-copy"><div class="wrap">
<p class="eyebrow">The Avalon Creed</p>
<h1>Creed of Avalon</h1>
<p class="lede">Belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment.</p>
<div class="buttons center"><a class="button primary" href="/creed/">Read the Creed</a><a class="button" href="/way/">Walk the Way</a></div>
</div></section>

<section class="band" aria-labelledby="what-h"><div class="wrap split">
<div><p class="eyebrow">What Avalon is</p><h2 id="what-h">A creed for those who would live chivalry.</h2>
<div class="prose">{lines(CREED_OPEN)}</div>
<div class="buttons"><a class="button" href="/creed/">The Creed in full</a></div></div>
<div class="creed-panel" style="margin-top:0"><p class="kicker">Why “Avalon”?</p>{lines(WHY_AVALON).replace('<p>','<p class="poem">')}</div>
</div></section>

<section class="disclaimer" aria-labelledby="disc-h"><div class="wrap inner">
<p class="tag" id="disc-h">Know before you read on</p>
<div>
<p><strong>Avalon is not woke.</strong> The Avalon Creed stands firmly against most tenets of left-leaning ideology. We say so plainly, on the front page, so you can decide right away whether this is for you.</p>
<p class="links"><a class="textlink" href="/positions/">Read where Avalon stands</a><a class="textlink" href="/faq/">Read the FAQ</a></p>
</div></div></section>

<section class="band" aria-labelledby="mission-h"><div class="wrap center">
<p class="eyebrow" id="mission-h">The Quest</p>
<p class="mission-quote">“{MISSION}”</p>
</div></section>

<section class="band alt" aria-labelledby="rel-short-h"><div class="wrap">
<p class="eyebrow">A creed and a calling</p><h2 id="rel-short-h">A creed to live. A religion to those who hold it as one.</h2>
<p class="measure">{REL_SHORT} Avalon does not make a deity of anything, nor does it deny one, and it sits easily beside many faiths. What you do matters more to the Way than what you profess.</p>
<div class="buttons"><a class="button" href="/creed/#religion">Why Avalon is a religion</a></div>
</div></section>

<section class="band" aria-labelledby="way-h"><div class="wrap">
<p class="eyebrow">The Way</p><h2 id="way-h">The Code, the Virtues, and the Tenets.</h2>
<p class="measure">To follow The Way is to live in accordance with the principles of chivalry: to train the body, sharpen the mind, fortify the spirit, and stand ready to protect what is good.</p>
{cards([('The Code','The Avalon Code of Chivalry: eleven obligations, each explained.','/way/code/','The standard'),('The Virtues','Eight Arch Virtues, each with three pillar virtues: thirty-two in all.','/way/virtues/','The character'),('The Tenets','The beliefs, daily practices, and standards of Avalon.','/way/tenets/','The practice')])}
<h3 style="margin-top:2.4rem">Eight Arch Virtues</h3>
<p class="measure">The Avalon Creed names thirty-two virtues. They are learned first as eight Arch Virtues, each with three pillar virtues beside it: related to their Arch Virtue, not lesser than it.</p>
<div class="virtue-tiles">{tiles}</div>
</div></section>

<section class="band statement"><div class="wrap">
<p class="big">“To Defend Humanity Against Chaos.”</p><p class="attr">From the Avalon Code of Chivalry</p>
</div></section>

<section class="band alt" aria-labelledby="train-h"><div class="wrap">
<p class="eyebrow">The three pillars</p><h2 id="train-h">Train the body, the mind, and the spirit.</h2>
<p class="measure">These three pillars of being must be made and kept strong in order for one to stay on the Way through the difficulties of life. Martial arts are the core of chivalry: they forge mind, body, and spirit into one keen edge, and the weapon arts stand at the heart of Avalon’s culture. Not for aggression, but for the defense of the innocent and the effective service of the Way.</p>
{pillars(PILLARS3)}
</div></section>

<section class="band order-band" aria-labelledby="order-h"><div class="wrap">
<p class="eyebrow">The Order of Avalon</p><h2 id="order-h">For those who would live the Creed in full.</h2>
<p class="measure">Anyone can choose to follow the Way. The Order of Avalon is something more: a Martial Chivalric Order and Brotherhood founded on the Avalon Creed, which trains to a standard and puts that training to work to empower, enlighten, and protect. Men and women alike, held to the same standards.</p>
<div class="buttons"><a class="button primary ext" href="{OOA}/" rel="noopener">Visit the Order of Avalon</a><a class="button" href="/order/">Avalon and the Order</a></div>
</div></section>

<section class="band" aria-labelledby="faq-h"><div class="wrap">
<p class="eyebrow">Common questions</p><h2 id="faq-h">Know what you are answering.</h2>
{faq(FAQ[:5])}
<p style="margin-top:1.4rem"><a class="textlink" href="/faq/">All questions</a></p>
</div></section>
'''
doc('/','Home','The Avalon Creed: belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment. The Code, the Virtues, and the Tenets of Avalon.',home)

# ---------------- THE CREED ----------------
inner('/creed/','creed','Creed of Avalon','Belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment.',
 '<div class="split"><div class="prose doctrine-creed">'+lines(CREED_OPEN)+'<h2>Why “Avalon”?</h2>'+lines(WHY_AVALON)+'<h2>The Way</h2>'+lines(THE_WAY)+'</div>'
 f'<div><div class="creed-panel" style="margin-top:0"><p class="kicker">The Quest</p><p>“{MISSION}”</p></div>'
 +cards([('The Code','The obligations every follower of the Way takes up.','/way/code/'),('The Virtues','Eight Arch Virtues and their pillar virtues.','/way/virtues/'),('The Tenets','Beliefs, daily practices, and standards.','/way/tenets/')],'grid two')+'</div></div>'
 '<div style="margin-top:3rem">'+REL+'</div>'+KNIGHT_NOTE,
 desc='The Creed of Avalon: belief in Modern Chivalry as a Way of Life, Purpose, and Enlightenment, and why Avalon is a religion to those who hold it as one.',eyebrow='The Creed')

# ---------------- THE WAY ----------------
inner('/way/','way','The Way','To follow The Way is to live in accordance with the principles of chivalry.',
 pillars(PILLARS3)+
 '<p class="measure">It is to train the body, sharpen the mind, fortify the spirit, and stand ready to protect what is good. The Code sets the standard, the Virtues describe the character, and the Tenets set out the beliefs and daily practice.</p>'+
 cards([('The Code','The Avalon Code of Chivalry: eleven obligations, each explained.','/way/code/','The standard'),('The Virtues','Eight Arch Virtues and their pillar virtues: thirty-two in all.','/way/virtues/','The character'),('The Tenets','The beliefs, daily practices, and standards of Avalon.','/way/tenets/','The practice')])+
 '<div class="creed-panel"><p class="kicker">A creed to live by</p><p>Avalon is a creed and a way of life. For some it is a religion, and it is registered as a religion and a church so that the Way may be followed, and developed, freely. For others it is a calling and a discipline. What you do matters more to the Way than what you profess.</p><p><a class="textlink" href="/creed/#religion">Why Avalon is a religion</a></p></div>',
 eyebrow='The Way')

inner('/way/code/','way','The Code','The Avalon Code of Chivalry: the obligations every follower of the Way takes up. Open each to read it.',
 '<div class="doctrine">'+code_html+'</div>'+KNIGHT_NOTE)

vh='<p class="measure">The Avalon Creed names thirty-two virtues. The eight in larger type are the <strong>Arch Virtues</strong>. Beneath each are three <strong>pillar virtues</strong>. They are related to their Arch Virtue, not lesser than it. The grouping is a learning tool, because it is easier to hold eight virtues first than thirty-two.</p>'
vh+='<ul class="toc">'+''.join(f'<li><a href="#{a.lower()}">{a}</a></li>' for (a,_),_ in groups)+'</ul>'
vh+='<div class="doctrine">'+intro
for (a,b),ps in groups:
    vh+=f'<section class="arch" id="{a.lower()}"><details><summary><span class="t-lg">{a}</span></summary>{b}</details>'
    vh+='<p class="pillar-label">Pillar virtues</p><div class="pillar-virtues">'+''.join(f'<details id="{p.lower()}"><summary><span class="t-sm">{p}</span></summary>{pb}</details>' for p,pb in ps)+'</div></section>'
vh+='</div>'+KNIGHT_NOTE
inner('/way/virtues/','way','The Virtues','Eight Arch Virtues, each with three pillar virtues. Courage is the first of all virtues.',vh)

inner('/way/tenets/','way','The Tenets','Some of the beliefs, practices, and rituals of Avalon: daily practice, readiness, protection, direction, self-forging, the standard, and the stand against chaos.',
 KNIGHT_NOTE+'<div class="doctrine">'+tenets_html+'</div>')

# ---------------- FAQ / POSITIONS ----------------
inner('/faq/','faq','Frequently Asked Questions','Religion, who can follow the Way, reenactment, politics, and the Order.',faq(FAQ)+
 '<div class="buttons"><a class="button" href="/positions/">Read where Avalon stands</a><a class="button" href="/contact/">Ask a question</a></div>')
pos=''.join(f'<article class="position"><p class="kicker">Position {i:02d}</p><h2>{t}</h2>'+''.join(f'<p>{H.escape(p)}</p>' for p in ps)+'</article>' for i,(t,ps) in enumerate(POSITIONS,1))
inner('/positions/','positions','Where Avalon Stands','Current societal issues: Avalon’s positions, stated openly so you know where we stand before you walk the Way.',
 POS_INTRO+'<div class="positions">'+pos+'</div>',eyebrow='Positions')

# ---------------- THE ORDER ----------------
inner('/order/','order','Avalon and the Order','The Avalon Creed holds the teaching. The Order of Avalon is how its members live it.',
 '<div class="prose"><p>Avalon is the belief system: the Creed, the Code, the Virtues, and the Tenets, published openly on this site.</p>'
 '<p>Anyone can choose to follow the Way. That is not the same as joining the Order of Avalon. The Order is a Martial Chivalric Order: a committed Brotherhood of men and women, held to the same standards, that trains to a standard and puts that training to work to empower, enlighten, and protect.</p>'
 '<p>The first line of the Code makes the difference clear. <em>“To Serve and Defend Avalon, the Order, its Members, and its Missions”</em> is, in the Creed’s own words, specific to members of the Order of Avalon: a pledge to serve and protect.</p>'
 '<p>The Order is in its founding phase and is not yet open for membership. Those who answer now will help build it.</p></div>'+
 cards([('The Order of Avalon','Who the Order is, what it trains for, and why it exists now.',f'{OOA}/order/'),('The Roadmap','The road from a single pilgrim to a living Order, phase by phase.',f'{OOA}/roadmap/'),('Join the Waiting List','Put your name forward and hear first when the Order opens.',f'{OOA}/join/waiting-list/')])+
 f'<div class="buttons"><a class="button primary ext" href="{OOA}/" rel="noopener">Visit orderofavalon.com</a></div>',eyebrow='The Order')

# ---------------- SUPPORT ----------------
inner('/support/','support','Support Avalon','Help keep and teach the Way, and build the Order that lives it.',
 '<div class="donate-main"><p class="kicker">Give online</p><h2>GiveSendGo</h2>'
 '<p>Our fundraiser, <strong>Supporting the Order of Avalon</strong>, is on GiveSendGo. It funds the work of Avalon and the development and growth of the Order: its missions, its future chapters, and the places it will train and serve from.</p>'
 f'<div class="buttons"><a class="button primary" href="{GSG}" target="_blank" rel="noopener">Give on GiveSendGo</a></div>'
 '<p class="hint">Opens GiveSendGo in a new tab.</p></div>'
 '<div class="grid">'
 '<div class="card"><p class="kicker">Give directly</p><h3>Zelle</h3><p>Send to the Zelle tag:</p><p class="zelle-tag"><code>orderofavalon</code></p></div>'
 '<div class="card"><p class="kicker">Coming soon</p><h3>PayPal</h3><p>Opening soon.</p></div>'
 '<div class="card"><p class="kicker">Coming soon</p><h3>Cash App</h3><p>Opening soon.</p></div>'
 '</div>'
 '<div class="prose" style="margin-top:2rem"><p>Donations support Avalon, a religious nonprofit.</p>'
 '<p class="source">Legal: Donations are received by Avalon Church of Chivalry, a California nonprofit religious corporation.  Please consult your tax advisor regarding the deductibility of any gift.</p></div>'
 f'<div class="buttons"><a class="button ext" href="{OOA}/contact/?for=donations" rel="noopener">Questions about giving</a></div>',eyebrow='Support')

# ---------------- CONTACT ----------------
inner('/contact/','contact','Contact','Questions about the Creed, the Order, or giving.',
 '<div class="prose"><p>The Avalon Creed and the Order of Avalon share one contact form, kept on orderofavalon.com. Write to us there with any question about the Way, the Order, or supporting Avalon; check what applies, and we will be in touch.</p></div>'
 f'<div class="buttons"><a class="button primary ext" href="{OOA}/contact/" rel="noopener">Write to us</a><a class="button ext" href="{OOA}/join/waiting-list/" rel="noopener">Join the Order’s waiting list</a><a class="button ext" href="{OOA}/contact/?for=donations" rel="noopener">Questions about giving</a></div>')

# ---------------- 404 ----------------
doc('/','Page not found','This page could not be found.',
 '<div class="page-hero"><div class="wrap"><p class="eyebrow">Not found</p><h1>This path does not exist.</h1><p class="lede">The page you were looking for could not be found.</p><div class="buttons"><a class="button primary" href="/">Return home</a><a class="button" href="/creed/">Read the Creed</a></div></div></div>',fname='404.html')

open(OUT+'/robots.txt','w').write('User-agent: *\nAllow: /\n')
open(OUT+'/_redirects','w').write('/the-code /way/code/ 301\n/the-virtues /way/virtues/ 301\n/the-tenets /way/tenets/ 301\n/faqs /faq/ 301\n')
json.dump({'pages':PAGES},open(os.path.dirname(os.path.abspath(__file__))+'/manifest.json','w'),indent=1)
print(len(PAGES),'pages'); [print(p,'|',t) for p,t in PAGES]

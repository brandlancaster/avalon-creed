import re, html as H
SRC="/workspace/avalon-media/creed-build/src"
def main_of(name):
    s=open(f'{SRC}/{name}',encoding='utf-8').read()
    m=s[s.find('<main'):s.find('</main>')]
    m=m[m.find('>')+1:]
    return m
def clean(m):
    m=re.sub(r'<span[^>]*aria-hidden="true"[^>]*>[^<]*</span>','',m)
    m=re.sub(r'<span class="[^"]*text-(?:2xl|3xl)[^"]*">','<span data-t="lg">',m)
    m=re.sub(r'<span class="[^"]*text-base[^"]*">','<span data-t="sm">',m)
    m=re.sub(r'\s(?:class|style)="[^"]*"','',m)
    m=m.replace('data-t="lg"','class="t-lg"').replace('data-t="sm"','class="t-sm"')
    m=re.sub(r'<h1>.*?</h1>','',m,flags=re.S)
    m=re.sub(r'<p>\(click[^<]*\)</p>','',m)
    return m
def code(): return clean(main_of('ac-the-code.html'))
def tenets(): return clean(main_of('ac-the-tenets.html'))
def creed(): return clean(main_of('ac.html'))
def faq_parts():
    m=clean(main_of('ac-faqs.html'))
    i=m.find('<p>Current Societal Issues</p>')
    a=m[:i]+'</div>'; b=m[i+len('<p>Current Societal Issues</p>'):]
    b=b[:b.rfind('</div>')]
    return a,b
def virtues():
    m=clean(main_of('ac-the-virtues.html'))
    items=[]; pos=0
    # flat sibling <details>; bodies contain no nested details
    for d in re.finditer(r'<details><summary><span class="(t-lg|t-sm)">(.*?)</span></summary>(.*?)</details>',m,re.S):
        items.append((d.group(1)=='t-lg',d.group(2),d.group(3)))
    intro=''
    groups=[]
    for lg,t,b in items:
        if lg: groups.append([(t,b),[]])
        else: groups[-1][1].append((t,b))
    return intro,groups
if __name__=='__main__':
    i,g=virtues(); print([ (a[0],[p[0] for p in ps]) for a,ps in g])
    a,b=faq_parts(); print(len(a),len(b))
    print(creed()[:600])

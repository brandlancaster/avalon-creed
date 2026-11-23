# usage: make_deploy.py <branch> <outjs>   (Avalon Creed; adapted from contact-backend/make_deploy.py; static only, no _worker.js)
import json,blake3,base64,os,sys
branch,outjs=sys.argv[1],sys.argv[2]
root='/workspace/avalon-creed-site'; man={}; pay=[]
ct={'html':'text/html','css':'text/css','jpg':'image/jpeg','png':'image/png','webp':'image/webp','ico':'image/x-icon','txt':'text/plain'}
for d,_,fs in os.walk(root):
  for f in fs:
    if f.startswith('_') or f.startswith('.'): continue
    fp=os.path.join(d,f); rel='/'+os.path.relpath(fp,root)
    b=base64.b64encode(open(fp,'rb').read()).decode(); ext=f.rsplit('.',1)[1]
    h=blake3.blake3((b+ext).encode()).hexdigest()[:32]; man[rel]=h
    pay.append({"key":h,"value":b,"metadata":{"contentType":ct[ext]},"base64":True})
json.dump(pay,open('/tmp/creed_upload.json','w'))
json.dump({"hashes":list(set(man.values()))},open('/tmp/creed_hashes.json','w'))
J=json.dumps
js='''async () => { const form=new FormData(); form.append('manifest', JSON.stringify(%s)); form.append('branch',%s);
form.append('_redirects', new Blob([%s]), '_redirects');
const d=await cloudflare.request({method:'POST',path:'/accounts/'+accountId+'/pages/projects/avalon-creed/deployments',body:form});
return {id:d.result.id,url:d.result.url,env:d.result.environment,stage:d.result.latest_stage&&d.result.latest_stage.status}; }''' % (J(man),J(branch),J(open(root+'/_redirects').read()))
open(outjs,'w').write(js); print(len(man),'files; branch',branch, '; upload bytes', os.path.getsize('/tmp/creed_upload.json'))

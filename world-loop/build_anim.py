#!/usr/bin/env python3
import re, json, pathlib
base = pathlib.Path(__file__).parent
land = (base / "land_path.txt").read_text().strip()
coord_raw = (base / "coord_raw.txt").read_text()
coords = [[float(a), float(b)] for a, b in re.findall(r"\[([\d.]+),\s*([\d.]+)\]", coord_raw)]
COORD = json.dumps(coords)

template = r"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
  html,body{margin:0;padding:0;background:#0a2c4d;overflow:hidden}
  #svg{display:block;width:100vw;height:100vh}
</style></head>
<body>
<svg id="svg" viewBox="0 0 1000 423.4" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#11507f"/>
      <stop offset="100%" stop-color="#0a2742"/>
    </linearGradient>
    <radialGradient id="vign" cx="50%" cy="48%" r="78%">
      <stop offset="62%" stop-color="#000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0.28"/>
    </radialGradient>
  </defs>
  <rect x="0" y="0" width="1000" height="423.4" fill="url(#water)"/>
  <path id="land" d="__LAND__" fill="#2fa356" stroke="#1f7d40" stroke-width="0.4" stroke-linejoin="round"/>
  <g id="dyn"></g>
  <rect x="0" y="0" width="1000" height="423.4" fill="url(#vign)"/>
</svg>
<script>
const RAW = __COORD__;
// palette (contrast with green land / blue water) - red idle like the original
const IDLE_HALO="#ff4d4d", IDLE_DOT="#ff7a7a";
const ASK="#ffd60a";   // query / outgoing (yellow)
const RES="#2fe0ff";   // result / incoming (cyan)

function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
const rnd=mulberry32(70260615);

// light thinning to remove exact overlaps but keep clusters dense enough for fan-out
const MINSEP_PIN=7;
const P=[];
for(const c of RAW){ if(P.every(p=>Math.hypot(p[0]-c[0],p[1]-c[1])>=MINSEP_PIN)) P.push(c); }
const N=P.length;
function dist(a,b){return Math.hypot(P[a][0]-P[b][0],P[a][1]-P[b][1]);}

// closeness band: packets only travel within [MIN_D, MAXD] (ni muy cerca ni muy lejos)
const MIN_D=9, MAXD=46;
const NEAR=[...Array(N)].map((_,i)=>[...Array(N).keys()].filter(j=>j!==i&&dist(i,j)>=MIN_D&&dist(i,j)<=MAXD).sort((x,y)=>dist(i,x)-dist(i,y)));

// clusters = connected components within MAXD
const parent=[...Array(N).keys()];
function find(x){while(parent[x]!==x){parent[x]=parent[parent[x]];x=parent[x];}return x;}
for(let i=0;i<N;i++)for(let j=i+1;j<N;j++)if(dist(i,j)<=MAXD)parent[find(i)]=find(j);
const comp={}; for(let i=0;i<N;i++){(comp[find(i)]=comp[find(i)]||[]).push(i);}
let clusters=Object.values(comp).filter(c=>c.length>=4);
clusters.sort((a,b)=>P[a[0]][0]-P[b[0]][0]);

function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}

// lifecycle (seconds within a T-second loop)
const T_SEC=12;
const S={PRE:0.30,QUERY:0.90,PAUSE:0.35,RESULT:0.90,ACK:0.35};
const D={}; for(const k in S) D[k]=S[k]/T_SEC;
const ePRE=D.PRE, eQRY=ePRE+D.QUERY, ePAU=eQRY+D.PAUSE, eRES=ePAU+D.RESULT, eEND=eRES+D.ACK;
const DURN=eEND;
const DASH=8.5, KWANT=4;

// one cyclic, evenly-spaced sequence per cluster -> continents animate in parallel & loop
const TXNS=[];
clusters.forEach((cl,ci)=>{
  const emitters=cl.filter(i=>NEAR[i].length>=2).sort((a,b)=>NEAR[b].length-NEAR[a].length);
  if(!emitters.length) return;
  const Mc = cl.length>=10 ? 3 : 2;            // transactions per loop for this cluster
  const offset = (ci*0.1973)%1;                // desync clusters
  let ec = ci % emitters.length;
  for(let m=0;m<Mc;m++){
    const t0=(offset + m/Mc)%1;
    const e=emitters[ec % emitters.length]; ec++;
    const pool=NEAR[e].filter(j=>cl.includes(j));
    const k=Math.min(KWANT, pool.length);
    const targets=pool.slice(0,k);            // the k nearest peers (4-5 servers per comm)
    if(targets.length) TXNS.push({emitter:e,targets,t0});
  }
});

function env(dt,a,b){const up=0.04,dn=0.10,L=b-a,x=dt-a;if(x<0||x>L)return 0;let v=1;if(x<up)v=x/up;if(x>L-dn)v=Math.min(v,(L-x)/dn);return Math.max(0,Math.min(1,v));}

const dyn=document.getElementById('dyn');
function render(t){
  const col=new Array(N).fill(null), glow=new Float64Array(N);
  let dashes='';
  for(const tx of TXNS){
    const dt=((t-tx.t0)%1+1)%1;
    if(dt>=DURN) continue;
    const eg=env(dt,0,eEND);
    const ex=P[tx.emitter][0], ey=P[tx.emitter][1];
    col[tx.emitter]= dt<eRES ? ASK : RES; glow[tx.emitter]=Math.max(glow[tx.emitter],0.85*eg+0.15);
    for(const tg of tx.targets){
      const x2=P[tg][0], y2=P[tg][1], len=Math.hypot(x2-ex,y2-ey);
      let off=null, c=ASK;
      if(dt>=ePRE && dt<eQRY){ const p=(dt-ePRE)/D.QUERY; off=DASH-p*(len+2*DASH); c=ASK; }
      else if(dt>=eQRY && dt<ePAU){ off=-(len+DASH); c=ASK; }
      else if(dt>=ePAU && dt<eRES){ const p=(dt-ePAU)/D.RESULT; off=-(len+DASH)+p*(len+2*DASH); c=RES; }
      if(off!==null){
        dashes+=`<line x1="${ex.toFixed(2)}" y1="${ey.toFixed(2)}" x2="${x2.toFixed(2)}" y2="${y2.toFixed(2)}" stroke="${c}" stroke-width="1.9" stroke-linecap="round" stroke-dasharray="${DASH} ${(len+DASH).toFixed(2)}" stroke-dashoffset="${off.toFixed(2)}"/>`;
      }
      if(dt>=ePRE){ const tgEnv=env(dt,ePRE,eEND); if(tgEnv>glow[tg]){glow[tg]=tgEnv; col[tg]= dt<ePAU?ASK:RES;} }
    }
  }
  // pins (crisp: low-opacity halo circle + solid dot, no blur)
  let halos='', dots='';
  for(let i=0;i<N;i++){
    const x=P[i][0], y=P[i][1], g=glow[i];
    if(col[i]===null){
      halos+=`<circle cx="${x}" cy="${y}" r="3.0" fill="${IDLE_HALO}" opacity="0.16"/>`;
      dots +=`<circle cx="${x}" cy="${y}" r="1.9" fill="${IDLE_DOT}"/>`;
    } else {
      halos+=`<circle cx="${x}" cy="${y}" r="${(3.4+2.6*g).toFixed(2)}" fill="${col[i]}" opacity="${(0.42*g).toFixed(3)}"/>`;
      dots +=`<circle cx="${x}" cy="${y}" r="${(2.0+1.3*g).toFixed(2)}" fill="${col[i]}"/>`;
      dots +=`<circle cx="${x}" cy="${y}" r="${(0.7+0.5*g).toFixed(2)}" fill="#ffffff" opacity="0.9"/>`;
    }
  }
  dyn.innerHTML = `<g>${halos}</g><g>${dashes}</g><g>${dots}</g>`;
}
window.render=render; window.__ready=true; window.__N=N; window.__C=clusters.length; window.__TX=TXNS.length;
render(0);
</script>
</body></html>
"""
html = template.replace("__LAND__", land).replace("__COORD__", COORD)
(base / "anim.html").write_text(html)
print("wrote anim.html")

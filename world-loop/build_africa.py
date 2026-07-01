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
  text{font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700}
</style></head>
<body>
<svg id="svg" viewBox="0 0 1000 423.4" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#11507f"/><stop offset="100%" stop-color="#0a2742"/>
    </linearGradient>
    <radialGradient id="vign" cx="50%" cy="48%" r="78%">
      <stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="0.32"/>
    </radialGradient>
  </defs>
  <rect x="0" y="0" width="1000" height="423.4" fill="url(#water)"/>
  <path id="land" d="__LAND__" fill="#2fa356" stroke="#1f7d40" stroke-width="0.4" stroke-linejoin="round"/>
  <g id="dyn"></g>
  <rect id="vign" x="0" y="0" width="1000" height="423.4" fill="url(#vign)"/>
</svg>
<script>
const RAW=__COORD__;
const IDLE_HALO="#ff4d4d", IDLE_DOT="#ff7a7a";       // world pins: identical to the loop
const ETH_HALO="#ffcf00", ETH_DOT="#ffdd33";          // Ethiopia: yellow, no whitish glow

// world pins: same thinning as the loop animation
const MINSEP=7; const P=[];
for(const c of RAW){ if(P.every(p=>Math.hypot(p[0]-c[0],p[1]-c[1])>=MINSEP)) P.push(c); }
const N=P.length;

const FULL={x:0,y:0,w:1000,h:423.4};
const AFRICA={x:424.7,y:178.8,w:236.4,h:100.1};
function lerp(a,b,p){return a+(b-a)*p;}
function lerpBox(A,B,p){return {x:lerp(A.x,B.x,p),y:lerp(A.y,B.y,p),w:lerp(A.w,B.w,p),h:lerp(A.h,B.h,p)};}
function eio(p){return p<0.5?2*p*p:1-Math.pow(-2*p+2,2)/2;}
function eo(p){return 1-Math.pow(1-p,3);}
function backOut(p){const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(p-1,3)+c1*Math.pow(p-1,2);}

const AF=[
 {x:603.4,y:252.0,name:'Kenya',   lx:597.4,ly:253.1,anc:'end',  t0:2.0,eth:false},
 {x:527.4,y:235.0,name:'Cameroon',lx:533.4,ly:236.1,anc:'start',t0:2.5,eth:false},
 {x:451.4,y:201.1,name:'Senegal', lx:457.4,ly:202.2,anc:'start',t0:3.0,eth:false},
 {x:608.5,y:219.2,name:'Ethiopia',lx:614.5,ly:220.3,anc:'start',t0:3.8,eth:true},
];
const POP=0.5;
// bigger African nodes (only these are enlarged), in AFRICA-view viewBox units
const A_HALO=3.2, A_DOT=1.8, A_FONT=4.5;

// timeline: near-instant delay, quick zoom, spawns, ~2s hold. NO blinking anywhere.
const T=6.5, P1=0.2, P2=1.8;

const svg=document.getElementById('svg'), dyn=document.getElementById('dyn'), vign=document.getElementById('vign');
function render(t){
  const tsec=t*T;
  let vb;
  if(tsec<=P1) vb=FULL; else if(tsec<P2){const p=eio((tsec-P1)/(P2-P1)); vb=lerpBox(FULL,AFRICA,p);} else vb=AFRICA;
  svg.setAttribute('viewBox',`${vb.x.toFixed(2)} ${vb.y.toFixed(2)} ${vb.w.toFixed(2)} ${vb.h.toFixed(2)}`);
  vign.setAttribute('x',vb.x);vign.setAttribute('y',vb.y);vign.setAttribute('width',vb.w);vign.setAttribute('height',vb.h);

  // world pins: EXACTLY like the loop (static red dots; halo r3.0 op0.16, dot r1.9). no blinking.
  let wh='', wd='';
  for(let i=0;i<N;i++){
    wh+=`<circle cx="${P[i][0]}" cy="${P[i][1]}" r="3.0" fill="${IDLE_HALO}" opacity="0.16"/>`;
    wd+=`<circle cx="${P[i][0]}" cy="${P[i][1]}" r="1.9" fill="${IDLE_DOT}"/>`;
  }

  // african nodes: just appear (pop-in), then steady. no blinking, no comms.
  let ah='', ad='', al='';
  for(const nd of AF){
    const age=tsec-nd.t0; if(age<0) continue;
    const pp=Math.min(1,age/POP);
    const scale = age<POP ? Math.max(0.001,backOut(pp)) : 1;
    const o = eo(Math.min(1, age/(POP*0.7)));
    const halo=nd.eth?ETH_HALO:IDLE_HALO, dot=nd.eth?ETH_DOT:IDLE_DOT;
    ah+=`<circle cx="${nd.x}" cy="${nd.y}" r="${(A_HALO*scale).toFixed(2)}" fill="${halo}" opacity="${(0.22*o).toFixed(3)}"/>`;
    ad+=`<circle cx="${nd.x}" cy="${nd.y}" r="${(A_DOT*scale).toFixed(2)}" fill="${dot}" opacity="${o.toFixed(3)}"/>`;
    const lc=nd.eth?'#ffe680':'#eef5ff';
    al+=`<text x="${nd.lx}" y="${nd.ly}" text-anchor="${nd.anc}" font-size="${A_FONT}" fill="${lc}" opacity="${o.toFixed(3)}">${nd.name}</text>`;
  }
  dyn.innerHTML = `<g>${wh}</g><g>${wd}</g><g>${ah}</g><g>${ad}</g><g>${al}</g>`;
}
window.render=render; window.__ready=true;
render(0);
</script>
</body></html>
"""
html=template.replace("__LAND__",land).replace("__COORD__",COORD)
(base/"africa.html").write_text(html)
print("wrote africa.html")

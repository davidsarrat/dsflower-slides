## The same setup becomes dsFlower

<div style="margin-top: 0.2em;">
<svg viewBox="0 0 810 340" style="width: 100%; max-height: 330px;">

  <defs>
    <filter id="ylwGlow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="b">
        <animate attributeName="stdDeviation" values="1.4; 4.2; 1.4" dur="1.6s" repeatCount="indefinite"/>
      </feGaussianBlur>
      <feFlood flood-color="#FFD000" flood-opacity="0.9" result="c"/>
      <feComposite in="c" in2="b" operator="in" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <!-- SuperNode nodes (top row) -->
  <g transform="translate(120,65)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" :filter="$clicks>=1 ? 'url(#ylwGlow)' : 'none'" :fill="$clicks>=1 ? 'rgba(255,208,0,0.16)' : 'rgba(136,204,255,0.08)'" :stroke="$clicks>=1 ? '#FFD000' : 'rgba(136,204,255,0.20)'" :stroke-width="$clicks>=1 ? 2 : 1"/>
    <text y="-4" text-anchor="middle" :fill="$clicks>=1 ? '#FFD000' : '#88ccff'" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital A</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <g transform="translate(350,65)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" :filter="$clicks>=1 ? 'url(#ylwGlow)' : 'none'" :fill="$clicks>=1 ? 'rgba(255,208,0,0.16)' : 'rgba(136,204,255,0.08)'" :stroke="$clicks>=1 ? '#FFD000' : 'rgba(136,204,255,0.20)'" :stroke-width="$clicks>=1 ? 2 : 1"/>
    <text y="-4" text-anchor="middle" :fill="$clicks>=1 ? '#FFD000' : '#88ccff'" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital B</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <g transform="translate(580,65)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" :filter="$clicks>=1 ? 'url(#ylwGlow)' : 'none'" :fill="$clicks>=1 ? 'rgba(255,208,0,0.16)' : 'rgba(136,204,255,0.08)'" :stroke="$clicks>=1 ? '#FFD000' : 'rgba(136,204,255,0.20)'" :stroke-width="$clicks>=1 ? 2 : 1"/>
    <text y="-4" text-anchor="middle" :fill="$clicks>=1 ? '#FFD000' : '#88ccff'" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital C</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <!-- Server-side annotation -->
  <text x="735" y="52" fill="#88ccff" font-family="Roboto Mono" font-size="3.5" text-anchor="middle">Local Training</text>
  <text x="735" y="64" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.5" text-anchor="middle">+</text>
  <foreignObject x="635" y="57" width="200" height="36">
    <div xmlns="http://www.w3.org/1999/xhtml" style="height:100%;display:flex;align-items:center;justify-content:center;">
      <span :class="$clicks>=1 ? 'disc-on' : ''" :style="'font-family:Roboto Mono,monospace;font-size:11px;line-height:1;padding:1.5px 4px;border-radius:2px;white-space:nowrap;' + ($clicks>=1 ? 'background:#FFD000;color:#1a1206;font-weight:600;' : 'background:transparent;color:#b0b8c0;')">Differential Privacy</span>
    </div>
  </foreignObject>

  <!-- SuperLink node (bottom center) -->
  <g transform="translate(350,280)">
    <rect x="-100" y="-38" width="200" height="76" rx="14" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.20)" stroke-width="1"/>
    <text y="-6" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="6" font-weight="500">SuperLink</text>
    <text y="16" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Researcher</text>
  </g>

  <!-- Aggregation label (right of SuperLink) -->
  <text x="470" y="276" fill="#88ccff" font-family="Roboto Mono" font-size="3.5" class="g-term" data-g="FedAvg / FedProx / FedOpt" style="cursor:pointer;">Federated Aggregation</text>
  <text x="470" y="290" fill="#b0b8c0" font-family="Roboto Mono" font-size="3">Orchestrator Role</text>

  <!-- Global model broadcast UP (pink) -->
  <path d="M335,242 C260,185 125,145 105,105" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M335,242 L340,105" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M335,242 C400,185 535,145 565,105" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>

  <!-- Weight updates DOWN (blue) -->
  <path d="M140,105 C170,155 305,195 365,242" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M360,105 L365,242" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M600,105 C570,155 435,195 365,242" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>

  <!-- Label paths -->
  <path id="flQL" d="M82,118 C108,160 245,200 320,258" fill="none" stroke="none"/>
  <path id="flRL" d="M122,88 C148,135 280,172 348,225" fill="none" stroke="none"/>
  <path id="flQR" d="M352,218 C420,165 552,128 578,80" fill="none" stroke="none"/>
  <path id="flRR" d="M385,252 C455,205 588,165 622,115" fill="none" stroke="none"/>

  <!-- Labels -->
  <text fill="#ffaacc" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#flQL" startOffset="50%">global model</textPath></text>
  <text fill="#88ccff" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#flRL" startOffset="50%">weight updates</textPath></text>
  <text fill="#ffaacc" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#flQR" startOffset="50%">global model</textPath></text>
  <text fill="#88ccff" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#flRR" startOffset="50%">weight updates</textPath></text>

  <!-- Privacy origin info box (appears on click) -->
  <foreignObject x="620" y="130" width="190" height="112" v-click="1" class="priv-info-fo">
    <div xmlns="http://www.w3.org/1999/xhtml" class="priv-info">
      <div class="priv-info-title">Protection starts at the node</div>
      <div class="priv-info-body">Privacy controls act on every weight update <strong>before</strong> it ever reaches the analyst's SuperLink.</div>
    </div>
  </foreignObject>

</svg>
</div>

Data never leaves the hospital. Only **weight deltas** travel back.

<style>
.priv-info-fo { transition: opacity 0.05s linear !important; transition-delay: 0s !important; }
.priv-info { height: 100%; box-sizing: border-box; border-radius: 6px; padding: 10px 13px; display: flex; flex-direction: column; justify-content: center; gap: 5px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10); border-left: 2px solid rgba(255,208,0,0.65); }
.priv-info-title { font-family: 'Roboto Mono', monospace; font-weight: 600; font-size: 12.5px; line-height: 1.25; color: #FFD000; }
.priv-info-body { font-family: 'Montserrat', sans-serif; font-size: 10.5px; line-height: 1.5; color: #d8d0c8; }
.priv-info-body strong { color: #FFD000; font-weight: 700; }
.disc-on { border-bottom: none !important; animation: discGlow 1.6s ease-in-out infinite; }
@keyframes discGlow { 0%, 100% { box-shadow: 0 0 3px rgba(255,208,0,0.35); } 50% { box-shadow: 0 0 11px rgba(255,208,0,0.85); } }
</style>

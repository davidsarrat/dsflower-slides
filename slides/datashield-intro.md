## DataSHIELD: data stays, answers travel

<div style="margin-top:0.3em;">
<svg viewBox="0 0 720 200" style="width:100%; max-height: 230px;">

  <!-- Hospital server + researcher (click 1) -->
  <g v-click="1">
    <rect x="40" y="40" width="210" height="130" rx="12" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.28)" stroke-width="1"/>
    <text x="145" y="62" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="5.2" font-weight="500">Hospital server</text>
    <ellipse cx="145" cy="98" rx="30" ry="7" fill="rgba(255,179,102,0.15)" stroke="#ffb366" stroke-width="1"/>
    <path d="M115,98 V124 a30,7 0 0 0 60,0 V98" fill="rgba(255,179,102,0.10)" stroke="#ffb366" stroke-width="1"/>
    <text x="145" y="158" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="3.6">raw records stay here</text>
    <rect x="480" y="40" width="210" height="130" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
    <text x="585" y="62" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="5.2" font-weight="500">Researcher</text>
    <circle cx="585" cy="98" r="8" fill="none" stroke="#e0d8d0" stroke-width="1.3"/>
    <path d="M572,120 C572,105 598,105 598,120" fill="none" stroke="#e0d8d0" stroke-width="1.3"/>
    <text x="585" y="158" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.6">runs the analysis</text>
  </g>

  <!-- Authorized access (click 2) -->
  <g v-click="2">
    <line x1="252" y1="105" x2="478" y2="105" stroke="rgba(102,221,170,0.30)" stroke-width="1" stroke-dasharray="3 3"/>
    <text x="365" y="100" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="3.8">authorized access</text>
  </g>

  <!-- Query up + aggregate down (click 3) -->
  <g v-click="3">
    <path d="M476,82 C405,58 305,58 254,72" fill="none" stroke="#FFD000" stroke-width="2" stroke-dasharray="7 5">
      <animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/>
    </path>
    <text x="365" y="50" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="3.8">analysis request</text>
    <path d="M254,138 C305,152 405,152 476,128" fill="none" stroke="#66ddaa" stroke-width="2" stroke-dasharray="7 5">
      <animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/>
    </path>
    <text x="365" y="170" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="3.8">aggregate result</text>
  </g>

</svg>
</div>

<div v-click="3" class="text-center" style="font-size:0.9em; color:#c8b8a8; margin-top:0.2em;">
<strong style="color:#66ddaa;">Only aggregate statistics leave the server</strong>, never individual-level records, and the originals can't be reconstructed.
</div>

<div>
<div v-click="4" style="text-align:center; font-family:'Roboto Mono'; font-size:0.7em; color:#66ddaa; letter-spacing:0.06em; margin-top:0.7em;">ENFORCED BY DISCLOSURE CONTROL</div>
<div class="grid grid-cols-4 gap-3" style="margin-top:0.4em;">
  <div v-click="5" style="background:rgba(102,221,170,0.06); border:1px solid rgba(102,221,170,0.18); border-radius:8px; padding:0.55em;">
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.76em; font-weight:600;">Minimum count</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.2em;">No cell or subgroup below N is ever returned.</div>
  </div>
  <div v-click="6" style="background:rgba(102,221,170,0.06); border:1px solid rgba(102,221,170,0.18); border-radius:8px; padding:0.55em;">
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.76em; font-weight:600;">Approved functions</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.2em;">No raw-data access, no arbitrary code; only vetted functions run.</div>
  </div>
  <div v-click="7" style="background:rgba(102,221,170,0.06); border:1px solid rgba(102,221,170,0.18); border-radius:8px; padding:0.55em;">
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.76em; font-weight:600;">Model limits</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.2em;">Too many parameters per subject is blocked, so a model can't memorize people.</div>
  </div>
  <div v-click="8" style="background:rgba(102,221,170,0.06); border:1px solid rgba(102,221,170,0.18); border-radius:8px; padding:0.55em;">
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.76em; font-weight:600;">Anonymised plots</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.2em;">Graphs use k-nearest-neighbour centroids and added noise, never raw points.</div>
  </div>
</div>
<div v-click="9" style="text-align:center; font-size:0.62em; color:#b0b8c0; margin-top:0.5em;">Four of several configurable filters, all set by the data custodian.</div>
</div>

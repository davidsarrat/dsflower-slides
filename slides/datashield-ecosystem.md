## The DataSHIELD package ecosystem

<div class="text-center" style="font-size:0.86em; color:#c8b8a8; margin-top:1.4em;">Some of the available packages, each an open-source server + client pair <span style="color:#66ddaa;">validated and audited by the DataSHIELD community</span>.</div>

<div class="grid grid-cols-3 gap-4" style="margin-top:1em;">
  <div v-click="1" style="background:rgba(136,204,255,0.06); border:1px solid rgba(136,204,255,0.24); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <line x1="8" y1="40" x2="40" y2="40" stroke="#88ccff" stroke-width="2" stroke-linecap="round"/>
      <rect x="11" y="26" width="6" height="12" rx="1" fill="rgba(136,204,255,0.18)" stroke="#88ccff" stroke-width="1.5"/>
      <rect x="21" y="18" width="6" height="20" rx="1" fill="rgba(136,204,255,0.18)" stroke="#88ccff" stroke-width="1.5"/>
      <rect x="31" y="11" width="6" height="27" rx="1" fill="rgba(136,204,255,0.18)" stroke="#88ccff" stroke-width="1.5"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#88ccff; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsBase</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Federated GLMs, contingency tables and survival</div>
  </div>
  <div v-click="2" style="background:rgba(255,170,204,0.06); border:1px solid rgba(255,170,204,0.24); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <path d="M18,9 C32,16 32,16 24,24 C16,32 16,32 30,39" fill="none" stroke="#ffaacc" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M30,9 C16,16 16,16 24,24 C32,32 32,32 18,39" fill="none" stroke="#ffaacc" stroke-width="1.8" stroke-linecap="round"/>
      <line x1="21" y1="13" x2="27" y2="13" stroke="#ffaacc" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="20" y1="35" x2="28" y2="35" stroke="#ffaacc" stroke-width="1.4" stroke-linecap="round"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#ffaacc; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsOmics</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Federated GWAS and gene-expression analysis</div>
  </div>
  <div v-click="3" style="background:rgba(255,208,0,0.06); border:1px solid rgba(255,208,0,0.24); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <rect x="11" y="11" width="26" height="26" rx="2.5" fill="none" stroke="#FFD000" stroke-width="1.8"/>
      <line x1="11" y1="19" x2="37" y2="19" stroke="#FFD000" stroke-width="1.5"/>
      <line x1="24" y1="11" x2="24" y2="37" stroke="#FFD000" stroke-width="1.5"/>
      <line x1="11" y1="28" x2="37" y2="28" stroke="#FFD000" stroke-width="1.2"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#FFD000; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsOMOP</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Interoperability with OMOP common data model databases</div>
  </div>
  <div v-click="4" style="background:rgba(102,221,170,0.06); border:1px solid rgba(102,221,170,0.24); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <rect x="9" y="9" width="30" height="30" rx="4" fill="none" stroke="#66ddaa" stroke-width="1.8"/>
      <circle cx="24" cy="24" r="8.5" fill="none" stroke="#66ddaa" stroke-width="1.5"/>
      <line x1="24" y1="11" x2="24" y2="37" stroke="#66ddaa" stroke-width="1" stroke-dasharray="2 2"/>
      <line x1="11" y1="24" x2="37" y2="24" stroke="#66ddaa" stroke-width="1" stroke-dasharray="2 2"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsImaging</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Operability with images and imaging tools like segmentation and radiomics</div>
  </div>
  <div v-click="5" style="background:rgba(255,140,66,0.06); border:1px solid rgba(255,140,66,0.26); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <rect x="11" y="10" width="11" height="28" rx="1.5" fill="rgba(255,140,66,0.16)" stroke="#ff8c42" stroke-width="1.6"/>
      <rect x="26" y="10" width="11" height="28" rx="1.5" fill="rgba(255,140,66,0.16)" stroke="#ff8c42" stroke-width="1.6"/>
      <line x1="9" y1="18" x2="39" y2="18" stroke="#ff8c42" stroke-width="1" stroke-dasharray="2 2"/>
      <line x1="9" y1="24" x2="39" y2="24" stroke="#ff8c42" stroke-width="1" stroke-dasharray="2 2"/>
      <line x1="9" y1="30" x2="39" y2="30" stroke="#ff8c42" stroke-width="1" stroke-dasharray="2 2"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#ff8c42; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsVert</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Statistical inference on vertically partitioned data</div>
  </div>
  <div v-click="6" style="background:rgba(183,139,224,0.07); border:1px solid rgba(183,139,224,0.26); border-radius:10px; padding:1em 0.7em; text-align:center;">
    <svg viewBox="0 0 48 48" style="width:42px; height:42px; display:block; margin:0 auto;">
      <line x1="24" y1="24" x2="24" y2="11" stroke="#b78be0" stroke-width="1" stroke-linecap="round"/>
      <line x1="24" y1="24" x2="37" y2="20" stroke="#b78be0" stroke-width="1" stroke-linecap="round"/>
      <line x1="24" y1="24" x2="33" y2="36" stroke="#b78be0" stroke-width="1" stroke-linecap="round"/>
      <line x1="24" y1="24" x2="15" y2="36" stroke="#b78be0" stroke-width="1" stroke-linecap="round"/>
      <line x1="24" y1="24" x2="11" y2="20" stroke="#b78be0" stroke-width="1" stroke-linecap="round"/>
      <circle cx="24" cy="24" r="4.5" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.6"/>
      <circle cx="24" cy="10" r="2.6" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.3"/>
      <circle cx="38" cy="19" r="2.6" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.3"/>
      <circle cx="33" cy="37" r="2.6" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.3"/>
      <circle cx="15" cy="37" r="2.6" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.3"/>
      <circle cx="10" cy="19" r="2.6" fill="rgba(183,139,224,0.18)" stroke="#b78be0" stroke-width="1.3"/>
    </svg>
    <div style="font-family:'Roboto Mono'; color:#b78be0; font-size:0.92em; font-weight:600; margin-top:0.35em;">dsExposome</div>
    <div style="font-size:0.64em; color:#b0b8c0; margin-top:0.25em; line-height:1.35;">Exposome-wide association analysis</div>
  </div>
</div>

<div v-click="7" class="text-center" style="margin-top:1em; font-size:0.9em; color:#c8b8a8;">
<span style="font-family:'Roboto Mono'; color:#FFD000; font-weight:700; letter-spacing:0.06em;">SPOILER:</span> <strong>dsFlower</strong> is another package suite, built exactly the same way.
</div>

## Extending DataSHIELD's capabilities

<div style="margin-top: 0.3em;">
<svg viewBox="0 0 720 320" style="width: 100%; max-height: 380px;">

  <!-- Two R sessions baseline (click 1) -->
  <g v-click="1">
    <rect x="40" y="52" width="250" height="214" rx="14" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
    <text x="165" y="76" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Analyst R session</text>
    <text x="165" y="89" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.8">on the researcher's machine</text>
    <circle cx="165" cy="110" r="7" fill="none" stroke="#e0d8d0" stroke-width="1.2"/>
    <path d="M153,130 C153,117 177,117 177,130" fill="none" stroke="#e0d8d0" stroke-width="1.2"/>
    <rect x="430" y="52" width="250" height="214" rx="14" fill="rgba(136,204,255,0.05)" stroke="rgba(136,204,255,0.18)" stroke-width="1"/>
    <text x="555" y="76" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="4.5" font-weight="500">Server R session</text>
    <text x="555" y="89" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.8">on each hospital server</text>
    <ellipse cx="555" cy="104" rx="24" ry="6" fill="rgba(255,179,102,0.15)" stroke="#ffb366" stroke-width="1"/>
    <path d="M531,104 V126 a24,6 0 0 0 48,0 V104" fill="rgba(255,179,102,0.10)" stroke="#ffb366" stroke-width="1"/>
    <text x="555" y="142" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.6">raw data</text>
  </g>

  <!-- Server-side package added (click 2) -->
  <g v-click="2">
    <rect x="450" y="146" width="210" height="98" rx="10" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.28)" stroke-width="0.9"/>
    <circle cx="463" cy="159" r="6.5" fill="rgba(102,221,170,0.18)" stroke="#66ddaa" stroke-width="0.8"/>
    <line x1="463" y1="155.5" x2="463" y2="162.5" stroke="#66ddaa" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="459.5" y1="159" x2="466.5" y2="159" stroke="#66ddaa" stroke-width="1.1" stroke-linecap="round"/>
    <text x="560" y="164" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="3.6" font-weight="500">Server-side package</text>
    <text x="560" y="176" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.6">e.g. dsBase</text>
    <text x="555" y="197" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="2.7">Exposes vetted functions,</text>
    <text x="555" y="209" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="2.7">local compute on the data</text>
    <text x="555" y="228" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="2.5">extends what can be computed</text>
  </g>

  <!-- Client-side package added (click 3) -->
  <g v-click="3">
    <rect x="60" y="146" width="210" height="98" rx="10" fill="rgba(255,208,0,0.06)" stroke="rgba(255,208,0,0.24)" stroke-width="0.9"/>
    <circle cx="73" cy="159" r="6.5" fill="rgba(102,221,170,0.18)" stroke="#66ddaa" stroke-width="0.8"/>
    <line x1="73" y1="155.5" x2="73" y2="162.5" stroke="#66ddaa" stroke-width="1.1" stroke-linecap="round"/>
    <line x1="69.5" y1="159" x2="76.5" y2="159" stroke="#66ddaa" stroke-width="1.1" stroke-linecap="round"/>
    <text x="170" y="164" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="3.6" font-weight="500">Client-side package</text>
    <text x="170" y="176" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.6">e.g. dsBaseClient</text>
    <text x="165" y="197" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="2.7">Orchestrates queries, calls</text>
    <text x="165" y="209" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="2.7">the exposed functions</text>
    <text x="165" y="228" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="2.5">pools results across servers</text>
  </g>

  <!-- Flows reusing workflow terminology (click 4) -->
  <g v-click="4">
    <path d="M272,178 C330,170 390,170 448,178" fill="none" stroke="#FFD000" stroke-width="2" stroke-dasharray="7 5">
      <animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/>
    </path>
    <text x="360" y="168" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="2.9">queries</text>
    <path d="M448,214 C390,222 330,222 272,214" fill="none" stroke="#66ddaa" stroke-width="2" stroke-dasharray="7 5">
      <animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/>
    </path>
    <text x="360" y="232" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="2.9">aggregated results</text>
  </g>

</svg>
</div>

<div v-click="5" class="text-center" style="font-size:0.9em; color:#c8b8a8; margin-top:0.2em;">
DataSHIELD grows by installing <strong style="color:#e0d8d0;">package pairs</strong>: the server-side package adds a computation under disclosure control, its client-side package issues the queries and pools the answers across servers.
</div>

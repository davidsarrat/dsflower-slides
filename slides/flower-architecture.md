## Flower's two roles: SuperLink and SuperNode

<div style="margin-top: 0.2em;">
<svg viewBox="0 0 810 340" style="width: 100%; max-height: 330px;">

  <!-- SuperLink node (top center) -->
  <g transform="translate(350,60)">
    <rect x="-100" y="-38" width="200" height="76" rx="14" fill="rgba(136,204,255,0.10)" stroke="rgba(136,204,255,0.45)" stroke-width="1.2"/>
    <text y="-6" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="6" font-weight="500">SuperLink</text>
    <text y="16" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">coordinator</text>
  </g>

  <!-- Aggregation label (right of SuperLink) -->
  <text x="470" y="54" fill="#88ccff" font-family="Roboto Mono" font-size="3.5" class="g-term" data-g="FedAvg / FedProx / FedOpt" style="cursor:pointer;">Federated Aggregation</text>
  <text x="470" y="68" fill="#b0b8c0" font-family="Roboto Mono" font-size="3">Orchestrator Role</text>

  <!-- SuperNode nodes (bottom row) -->
  <g transform="translate(120,275)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.20)" stroke-width="1"/>
    <text y="-4" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital A</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <g transform="translate(350,275)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.20)" stroke-width="1"/>
    <text y="-4" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital B</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <g transform="translate(580,275)">
    <rect x="-80" y="-40" width="160" height="80" rx="14" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.20)" stroke-width="1"/>
    <text y="-4" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="5" font-weight="500">SuperNode</text>
    <text y="14" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.5" font-weight="500">Hospital C</text>
    <text y="28" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="2.8">own data</text>
  </g>

  <!-- Global model broadcast DOWN (pink) -->
  <path d="M335,98 C260,155 125,195 105,235" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M335,98 L340,235" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M335,98 C400,155 535,195 565,235" fill="none" stroke="#ffaacc" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>

  <!-- Weight updates UP (blue) -->
  <path d="M140,235 C170,185 305,145 365,98" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M360,235 L365,98" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>
  <path d="M600,235 C570,185 435,145 365,98" fill="none" stroke="#88ccff" stroke-width="2.5" stroke-dasharray="8 6">
    <animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/>
  </path>

  <!-- Label paths -->
  <path id="paQL" d="M82,222 C108,180 245,140 320,82" fill="none" stroke="none"/>
  <path id="paRL" d="M122,266 C148,219 280,182 348,129" fill="none" stroke="none"/>
  <path id="paQR" d="M352,136 C420,189 552,226 578,274" fill="none" stroke="none"/>
  <path id="paRR" d="M385,88 C455,135 588,175 622,225" fill="none" stroke="none"/>

  <!-- Labels -->
  <text fill="#ffaacc" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#paQL" startOffset="50%">global model</textPath></text>
  <text fill="#88ccff" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#paRL" startOffset="50%">weight updates</textPath></text>
  <text fill="#ffaacc" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#paQR" startOffset="50%">global model</textPath></text>
  <text fill="#88ccff" font-family="Roboto Mono" font-size="3.5" text-anchor="middle"><textPath href="#paRR" startOffset="50%">weight updates</textPath></text>

</svg>
</div>

The **SuperLink** coordinates the run and aggregates the results. Each **SuperNode** trains on its own data and sends back only weight updates.

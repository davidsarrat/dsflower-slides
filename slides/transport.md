## No exposed gRPC — ride the DataSHIELD channel

<div style="margin-top:0.6em;">
<svg viewBox="0 0 820 280" style="width:100%; max-height:290px;">

  <!-- Researcher -->
  <g transform="translate(120,140)">
    <rect x="-110" y="-58" width="220" height="116" rx="14" fill="rgba(255,208,0,0.07)" stroke="rgba(255,208,0,0.35)" stroke-width="1.2"/>
    <text y="-32" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="6" font-weight="600">Researcher</text>
    <text y="-12" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.4">Flower SuperLink</text>
    <text y="4" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3.2">local · plain gRPC</text>
    <text y="30" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3.2">+ R relay</text>
  </g>

  <!-- Channel -->
  <rect x="255" y="102" width="310" height="76" rx="12" fill="rgba(102,221,170,0.06)" stroke="rgba(102,221,170,0.35)" stroke-width="1.1" stroke-dasharray="7 5"/>
  <text x="410" y="128" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="4.4" font-weight="600">DataSHIELD channel</text>
  <text x="410" y="144" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.6">authenticated HTTPS / TLS (DSI)</text>
  <text x="410" y="160" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3.2">Flower's bytes tunneled inside</text>

  <!-- Hospital -->
  <g transform="translate(700,140)">
    <rect x="-110" y="-58" width="220" height="116" rx="14" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.35)" stroke-width="1.2"/>
    <text y="-32" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="6" font-weight="600">Hospital</text>
    <text y="-12" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4.4">Flower SuperNode</text>
    <text y="4" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3.2">local · plain gRPC</text>
    <text y="30" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3.2">+ tunnel forwarder</text>
  </g>

  <!-- connectors -->
  <path d="M231,132 L253,132" stroke="#66ddaa" stroke-width="2" stroke-dasharray="7 5"><animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/></path>
  <path d="M567,132 L589,132" stroke="#66ddaa" stroke-width="2" stroke-dasharray="7 5"><animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/></path>
  <path d="M589,150 L567,150" stroke="#88ccff" stroke-width="2" stroke-dasharray="7 5"><animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/></path>
  <path d="M253,150 L231,150" stroke="#88ccff" stroke-width="2" stroke-dasharray="7 5"><animate attributeName="stroke-dashoffset" from="0" to="-12" dur="0.8s" repeatCount="indefinite"/></path>

</svg>
</div>

<div class="mt-2" style="color:#c8b8a8; font-size:0.95em;">
The SuperNode ↔ SuperLink bytes travel <strong>inside the TLS DataSHIELD connection</strong> the researcher already has with Opal — a <span class="g-term" data-g="DSI tunnel">DSI tunnel</span>. No hospital opens a gRPC port; Flower itself is untouched, only the transport changes.
</div>

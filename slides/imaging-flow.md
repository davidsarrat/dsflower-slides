## Federated vision — the same round-trip

<div style="margin-top:0.4em;">
<svg viewBox="0 0 830 330" style="width:100%; max-height:320px;">

  <!-- store -->
  <g transform="translate(110,90)">
    <rect x="-95" y="-42" width="190" height="84" rx="12" fill="rgba(255,180,100,0.07)" stroke="rgba(255,180,100,0.30)" stroke-width="1"/>
    <text y="-14" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="4.6" font-weight="600">dsimaging-store</text>
    <text y="4" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.4">image collection</text>
    <text y="20" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.9">MinIO</text>
  </g>

  <!-- node -->
  <g transform="translate(410,90)">
    <rect x="-120" y="-52" width="240" height="104" rx="13" fill="rgba(136,204,255,0.07)" stroke="rgba(136,204,255,0.30)" stroke-width="1.1"/>
    <text y="-30" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="4.8" font-weight="600">DataSHIELD node</text>
    <text y="-12" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="3.6">dsImaging → images</text>
    <text y="4" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.6">ResNet-18 · DP-SGD</text>
    <text y="22" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="3">data never leaves</text>
  </g>

  <!-- researcher -->
  <g transform="translate(410,265)">
    <rect x="-120" y="-42" width="240" height="84" rx="13" fill="rgba(255,208,0,0.07)" stroke="rgba(255,208,0,0.30)" stroke-width="1.1"/>
    <text y="-12" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="4.8" font-weight="600">Researcher</text>
    <text y="6" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.6">SuperLink · aggregates</text>
    <text y="22" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="3">ds.flower.fit(model = "resnet18")</text>
  </g>

  <!-- store -> node -->
  <path d="M206,90 L288,90" fill="none" stroke="#ffb366" stroke-width="2.2" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/></path>
  <text x="247" y="80" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="3">resolve</text>

  <!-- node <-> researcher (weights up, model down) -->
  <path d="M388,142 L388,223" fill="none" stroke="#88ccff" stroke-width="2.2" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/></path>
  <text x="352" y="185" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="3">weights ↑</text>
  <path d="M432,223 L432,142" fill="none" stroke="#ffaacc" stroke-width="2.2" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/></path>
  <text x="470" y="185" text-anchor="middle" fill="#ffaacc" font-family="Roboto Mono" font-size="3">model ↓</text>

  <!-- via DSI note -->
  <text x="600" y="185" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="3">over the DSI tunnel</text>
  <text x="600" y="197" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.7">(only DP updates leave)</text>

</svg>
</div>

<div class="mt-1" style="color:#c8b8a8; font-size:0.92em;">
Vision changes nothing about the protocol: dsImaging feeds images to a model <strong>inside the node</strong>, DP-SGD protects the update, and the researcher exchanges weights over the same tunnel — exactly like the tabular case.
</div>

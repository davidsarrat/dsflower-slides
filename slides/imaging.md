## dsImaging — medical images as a resource

<div style="margin-top:0.4em;">
<svg viewBox="0 0 830 320" style="width:100%; max-height:320px;">

  <!-- dsimaging-store (left) -->
  <g transform="translate(150,150)">
    <rect x="-130" y="-78" width="260" height="156" rx="14" fill="rgba(255,180,100,0.07)" stroke="rgba(255,180,100,0.35)" stroke-width="1.2"/>
    <text y="-54" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="5.4" font-weight="600">dsimaging-store</text>
    <text y="-38" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.4">MinIO object store</text>
    <g transform="translate(-25,-16)">
      <rect x="0" y="0" width="14" height="14" rx="2" fill="rgba(255,180,100,0.38)"/>
      <rect x="18" y="0" width="14" height="14" rx="2" fill="rgba(255,180,100,0.22)"/>
      <rect x="36" y="0" width="14" height="14" rx="2" fill="rgba(255,180,100,0.30)"/>
      <rect x="0" y="18" width="14" height="14" rx="2" fill="rgba(255,180,100,0.22)"/>
      <rect x="18" y="18" width="14" height="14" rx="2" fill="rgba(255,180,100,0.34)"/>
      <rect x="36" y="18" width="14" height="14" rx="2" fill="rgba(255,180,100,0.20)"/>
    </g>
    <text y="48" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="3.6">image collection</text>
    <text y="65" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.9">managed by dsimaging-admin</text>
  </g>

  <!-- DataSHIELD node (right) -->
  <g transform="translate(600,150)">
    <rect x="-150" y="-92" width="300" height="184" rx="14" fill="rgba(255,255,255,0.045)" stroke="rgba(255,255,255,0.16)" stroke-width="1"/>
    <text y="-70" text-anchor="middle" fill="#e0d8d0" font-family="Roboto Mono" font-size="4" font-weight="500">DataSHIELD node</text>
    <text y="-46" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="3.8" font-weight="600">Opal resource</text>
    <text y="-33" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.9">imaging+dataset, endpoint + creds</text>
    <line x1="-122" y1="-22" x2="122" y2="-22" stroke="rgba(255,255,255,0.12)" stroke-width="0.6"/>
    <text y="-2" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="4.4" font-weight="600">dsImaging</text>
    <text y="12" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.9">resolver, streams images on demand</text>
    <line x1="-122" y1="26" x2="122" y2="26" stroke="rgba(255,255,255,0.12)" stroke-width="0.6"/>
    <text y="46" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="3.3">images ready for a model</text>
    <text y="60" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="2.8">like any DataSHIELD variable</text>
  </g>

  <!-- resolve + stream arrow -->
  <path d="M281,150 C330,150 380,150 420,150" fill="none" stroke="#ffb366" stroke-width="2.2" stroke-dasharray="8 6"><animate attributeName="stroke-dashoffset" from="0" to="-14" dur="0.8s" repeatCount="indefinite"/></path>
  <text x="350" y="140" text-anchor="middle" fill="#ffb366" font-family="Roboto Mono" font-size="3.2">resolve + stream</text>

</svg>
</div>

<div class="mt-1" style="color:#c8b8a8; font-size:0.92em;">
The collection lives in <strong>dsimaging-store</strong> (a MinIO bucket, managed with <strong>dsimaging-admin</strong>). An Opal <strong>resource</strong> points at it and carries the credentials; <strong>dsImaging</strong> resolves that resource and streams the images into the node — nothing is copied to disk, nothing leaves.
</div>

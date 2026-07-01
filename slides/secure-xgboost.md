## XGBoost: trees, not weights

<div class="grid grid-cols-2 gap-8 mt-2">
<div>

XGBoost is the workhorse for **tabular clinical data**, but it builds **decision trees**, so there are no weights to average like a neural network.

<div class="mt-3" v-click>

So how do hospitals train one shared model without pooling their rows?

</div>

<div class="mt-4" v-click>

**Each hospital sends only a <span class="g-term" data-g="Secure histogram">secure histogram</span>**: a count of gradients per feature bin, never the patients behind them.

</div>

</div>
<div>

<svg viewBox="0 0 320 240" style="width: 100%;">
  <!-- Hospitals -->
  <g v-click="2">
    <rect x="10" y="10" width="90" height="34" rx="7" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.25)" stroke-width="0.8"/>
    <text x="55" y="26" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="7">Hospital A</text>
    <text x="55" y="37" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="5">histogram</text>
    <rect x="10" y="50" width="90" height="34" rx="7" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.25)" stroke-width="0.8"/>
    <text x="55" y="66" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="7">Hospital B</text>
    <text x="55" y="77" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="5">histogram</text>
    <rect x="10" y="90" width="90" height="34" rx="7" fill="rgba(136,204,255,0.08)" stroke="rgba(136,204,255,0.25)" stroke-width="0.8"/>
    <text x="55" y="106" text-anchor="middle" fill="#88ccff" font-family="Roboto Mono" font-size="7">Hospital C</text>
    <text x="55" y="117" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="5">histogram</text>
  </g>

  <!-- SecAgg+ box -->
  <g v-click="3">
    <line x1="100" y1="27" x2="170" y2="62" stroke="rgba(102,221,170,0.4)" stroke-width="1"/>
    <line x1="100" y1="67" x2="170" y2="67" stroke="rgba(102,221,170,0.4)" stroke-width="1"/>
    <line x1="100" y1="107" x2="170" y2="72" stroke="rgba(102,221,170,0.4)" stroke-width="1"/>
    <rect x="170" y="50" width="80" height="34" rx="7" fill="rgba(102,221,170,0.08)" stroke="rgba(102,221,170,0.3)" stroke-width="0.8"/>
    <text x="210" y="65" text-anchor="middle" fill="#66ddaa" font-family="Roboto Mono" font-size="6.5" class="g-term" data-g="SecAgg" style="cursor:pointer;">SecAgg+</text>
    <text x="210" y="77" text-anchor="middle" fill="#b0b8c0" font-family="Roboto Mono" font-size="5">sum only</text>
  </g>

  <!-- Global tree -->
  <g v-click="4">
    <line x1="250" y1="67" x2="285" y2="67" stroke="rgba(255,208,0,0.4)" stroke-width="1"/>
    <circle cx="290" cy="67" r="6" fill="rgba(255,208,0,0.15)" stroke="#FFD000" stroke-width="0.8"/>
    <circle cx="278" cy="95" r="5" fill="rgba(255,208,0,0.1)" stroke="#FFD000" stroke-width="0.7"/>
    <circle cx="302" cy="95" r="5" fill="rgba(255,208,0,0.1)" stroke="#FFD000" stroke-width="0.7"/>
    <line x1="287" y1="72" x2="280" y2="90" stroke="#FFD000" stroke-width="0.7"/>
    <line x1="293" y1="72" x2="300" y2="90" stroke="#FFD000" stroke-width="0.7"/>
    <text x="290" y="125" text-anchor="middle" fill="#FFD000" font-family="Roboto Mono" font-size="6">global tree</text>
  </g>
</svg>

<div v-click="4" class="mt-1">

The server sees only the **combined sum**, picks the best tree split, and never the rows behind it.

</div>

</div>
</div>

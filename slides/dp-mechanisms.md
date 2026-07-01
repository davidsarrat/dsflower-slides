## One guarantee, the right mechanism per method

<div class="grid grid-cols-1 gap-3 mt-4">

<div class="step-card" style="padding:0.7em 1.1em;">
  <span style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600;"><span class="g-term" data-g="DP-SGD">DP-SGD</span></span>
  <span style="color:#88ccff; font-size:0.85em;"> · neural track</span>
  <div style="color:#b8b0a8; font-size:0.88em; margin-top:2px;">Per-sample gradient clipping + calibrated noise <strong>inside the training loop</strong> (Opacus). The tightest guarantee — noise placed where it costs the least accuracy.</div>
</div>

<div class="step-card" style="padding:0.7em 1.1em;">
  <span style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600;"><span class="g-term" data-g="DP-GBDT">DP-GBDT</span></span>
  <span style="color:#88ccff; font-size:0.85em;"> · trees track</span>
  <div style="color:#b8b0a8; font-size:0.88em; margin-top:2px;">Clipped, noised gradient / Hessian sums drive the split gains and leaf values (S-GBDT). Pure NumPy — no extra library on the node.</div>
</div>

<div class="step-card" style="padding:0.7em 1.1em;">
  <span style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600;"><span class="g-term" data-g="Output perturbation">Output perturbation</span></span>
  <span style="color:#88ccff; font-size:0.85em;"> · egress · any app</span>
  <div style="color:#b8b0a8; font-size:0.88em; margin-top:2px;">Whatever leaves the node is clipped + noised at the door. The universal fallback — works for anything, including an uploaded app.</div>
</div>

</div>

<div class="mt-5" v-click style="color:#c8b8a8; font-size:0.92em;">

**Adaptive:** the node picks the mechanism that fits the method — but all of them spend the same **(ε, δ)** budget on one shared RDP ledger.

</div>

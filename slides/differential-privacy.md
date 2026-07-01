## Differential Privacy — the one guarantee

<div style="color:#c8b8a8; margin-top:0.5em;">

The model comes out **almost the same whether or not any single patient was in the data**. So nothing the analyst receives — weights, metrics, the final model — can be traced back to one person.

</div>

<div class="grid grid-cols-2 gap-6 mt-6 items-center">
<div>

<div class="step-card" style="padding:0.7em 1.1em;">
  <span style="font-family:'Roboto Mono',monospace; color:#66ddaa; font-weight:600;">(ε, δ)</span>
  <span style="color:#b8b0a8; font-size:0.9em;"> — ε bounds the privacy loss, δ a tiny failure probability. Smaller ε means more privacy.</span>
</div>

<div class="step-card" style="padding:0.7em 1.1em; margin-top:0.6em;">
  <span style="font-family:'Roboto Mono',monospace; color:#66ddaa; font-weight:600;">Server-enforced</span>
  <span style="color:#b8b0a8; font-size:0.9em;"> — fixed ceilings on ε / δ / clip and a per-dataset <span class="g-term" data-g="RDP ledger">RDP ledger</span> the analyst can only read.</span>
</div>

</div>
<div>

It is the **only** privacy mechanism dsFlower ships — no template catalogue, no secret-sharing to configure.

The analyst **never sets the privacy level**; each node fixes it from its own DataSHIELD options.

<div class="mt-3" style="color:#a89888; font-size:0.85em;">One formal guarantee — applied with the right mechanism for each method&nbsp;→</div>

</div>
</div>

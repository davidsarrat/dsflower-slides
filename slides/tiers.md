## Two ways to put a model on the nodes

<div class="grid grid-cols-2 gap-6 mt-4">

<div>
<div style="font-family:'Roboto Mono',monospace; color:#66ddaa; font-weight:600; font-size:1.05em;">Tier 1 · nn.Module spec</div>
<div style="color:#b8b0a8; font-size:0.9em; margin-top:0.6em;">A small <strong>declarative language</strong> we built to describe a model: a stock-layer <strong>nn.Module</strong>, sent as data, never code. The node assembles and trains it.</div>
<div class="step-card" style="padding:0.7em 1em; margin-top:0.9em; border-color:rgba(102,221,170,0.3);">
  <span style="color:#66ddaa; font-size:0.85em;">Because the node holds a real <code>nn.Module</code>, it runs <strong>per-sample DP-SGD</strong>: noise calibrated to each patient's own gradient. The <strong>finest-grained, strongest</strong> differential privacy.</span>
</div>
</div>

<div>
<div style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600; font-size:1.05em;">Tier 2 · uploaded app</div>
<div style="color:#b8b0a8; font-size:0.9em; margin-top:0.6em;">A full <strong>Flower app</strong> for anything the spec cannot express. It runs <strong>arbitrary code</strong>, so it passes <strong>the gate</strong>:</div>
<div class="step-card" style="padding:0.7em 1em; margin-top:0.9em;">
  <div style="color:#b8b0a8; font-size:0.83em; line-height:1.9;">
  · fail-closed <strong>exfiltration scan</strong><br/>
  · <strong>sandbox</strong> + <strong>SHA-256</strong> pinned on every node<br/>
  · DP only at the <strong>output</strong> (coarser than DP-SGD)
  </div>
</div>
</div>

</div>

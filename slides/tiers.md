## Two ways to put a model on the nodes

<div class="grid grid-cols-2 gap-6 mt-4">

<div>
<div style="font-family:'Roboto Mono',monospace; color:#66ddaa; font-weight:600; font-size:1.05em;">Tier 1 · <span class="g-term" data-g="nn.Module spec">nn.Module spec</span></div>
<div style="color:#b8b0a8; font-size:0.9em; margin-top:0.5em;">A <strong>declarative description</strong> — not code — built from an allowlisted vocabulary of stock torch layers. The <strong>node</strong> assembles the <code>nn.Module</code> and owns the loop, loss and optimizer.</div>
<div class="step-card" style="padding:0.6em 1em; margin-top:0.8em; border-color:rgba(102,221,170,0.25);">
  <span style="color:#66ddaa; font-size:0.85em;">No researcher code runs → <strong>DP-SGD guaranteed by construction.</strong> Every built-in model lives here.</span>
</div>
</div>

<div>
<div style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600; font-size:1.05em;">Tier 2 · <span class="g-term" data-g="App tier">uploaded app</span></div>
<div style="color:#b8b0a8; font-size:0.9em; margin-top:0.5em;">A full <strong>Flower app</strong> for anything the spec can't express. It runs <strong>arbitrary code</strong>, so it must pass <strong>the gate</strong>:</div>
<div class="step-card" style="padding:0.6em 1em; margin-top:0.8em;">
  <div style="color:#b8b0a8; font-size:0.83em; line-height:1.8;">
  · fail-closed <strong>exfiltration scan</strong><br/>
  · <strong>sandbox</strong> + <strong>egress DP</strong> (output perturbation)<br/>
  · <strong>SHA-256</strong> pinned &amp; identical on every node
  </div>
</div>
</div>

</div>

<div class="mt-5" v-click style="text-align:center; color:#c8b8a8; font-size:0.92em;">Safe by default, extensible when you need it — the node stays in control either way.</div>

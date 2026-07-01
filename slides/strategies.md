## Aggregation — how the sites are combined

<div style="color:#c8b8a8; margin-top:0.4em;">

Each round, every site returns a weight update. The **strategy** on the SuperLink decides how those become the next global model.

</div>

<div class="grid grid-cols-2 gap-6 mt-5 items-center">
<div>

<div class="step-card" style="padding:0.8em 1.1em;">
  <span style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600;"><span class="g-term" data-g="FedAvg">FedAvg</span></span>
  <div style="color:#b8b0a8; font-size:0.9em; margin-top:3px;">A <strong>weighted average</strong> of the site updates, by dataset size. dsFlower's workhorse.</div>
</div>

<div class="step-card" style="padding:0.8em 1.1em; margin-top:0.6em;">
  <span style="font-family:'Roboto Mono',monospace; color:#88ccff; font-weight:600;"><span class="g-term" data-g="FedBN">FedBN</span></span>
  <div style="color:#b8b0a8; font-size:0.9em; margin-top:3px;">Keeps <strong>BatchNorm local</strong> — for imaging where each site has a different scanner.</div>
</div>

</div>
<div>

Because **every update is already differentially private**, a plain weighted average is all privacy needs — no secret-sharing, no trusted aggregator.

<div style="color:#a89888; font-size:0.85em; margin-top:0.9em;">The wider Flower strategy family — <span class="g-term" data-g="FedProx">FedProx</span>, <span class="g-term" data-g="FedAdam">FedAdam</span>, <span class="g-term" data-g="FedAdagrad">FedAdagrad</span> — sits behind the same API.</div>

</div>
</div>

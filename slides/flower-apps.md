## A Flower run is two apps

<div class="grid grid-cols-2 gap-6 mt-4">

<div class="step-card" style="padding: 0.9em 1.2em;">
  <div style="font-family:'Roboto Mono',monospace; color:#88ccff; font-weight:600; font-size:1.05em;">ServerApp</div>
  <div style="color:#b8b0a8; font-size:0.9em; margin-top:0.4em;">Runs on the <strong>SuperLink</strong>. Owns the <strong>strategy</strong>: how each round is configured and how the site updates are <strong>aggregated</strong> into the next global model.</div>
</div>

<div class="step-card" style="padding: 0.9em 1.2em;">
  <div style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600; font-size:1.05em;">ClientApp</div>
  <div style="color:#b8b0a8; font-size:0.9em; margin-top:0.4em;">Runs on every <strong>SuperNode</strong>. Loads the local data and <strong>trains / evaluates</strong> the model, returning only a weight update.</div>
</div>

</div>

<div class="mt-8" v-click>

### Submission — from the researcher's side

The researcher never logs into a hospital. They **compose the app and submit it to the run**; Flower packages it (a **FAB**) and ships it to every SuperNode, which spins up the ClientApp on demand. In dsFlower that submission travels **through DataSHIELD** — the same channel used for any federated query.

</div>

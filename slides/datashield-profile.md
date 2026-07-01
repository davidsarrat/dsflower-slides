## DataSHIELD on its own

<div class="grid grid-cols-2 gap-8" style="margin-top:1.4em;">
  <div class="flex flex-col gap-4">
    <div style="font-family:'Roboto Mono'; color:#66ddaa; font-size:0.78em; font-weight:700; letter-spacing:0.12em; text-align:center;">STRENGTHS</div>
    <div v-click="1" class="pc-card pc-green">
      <div class="pc-icon">
        <svg viewBox="0 0 24 24" width="38" height="38"><circle cx="12" cy="12" r="10.5" fill="none" stroke="#66ddaa" stroke-width="1.6"/><path d="M7 12.5l3.2 3.2L17 8.8" fill="none" stroke="#66ddaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div class="pc-label" style="color:#66ddaa;">Privacy-preservation expertise</div>
      <div class="pc-sub">Years of experience and a deep focus on patient privacy, keeping every analysis non-disclosive so raw data never leaves the site.</div>
    </div>
    <div v-click="2" class="pc-card pc-green">
      <div class="pc-icon">
        <svg viewBox="0 0 24 24" width="38" height="38"><circle cx="12" cy="12" r="10.5" fill="none" stroke="#66ddaa" stroke-width="1.6"/><path d="M7 12.5l3.2 3.2L17 8.8" fill="none" stroke="#66ddaa" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div class="pc-label" style="color:#66ddaa;">Institutional trust and adoption</div>
      <div class="pc-sub">Years embedded in biomedical institutions: ethics-board, legal and data-custodian approval already secured across hospital networks and consortia.</div>
    </div>
  </div>
  <div class="flex flex-col gap-4">
    <div style="font-family:'Roboto Mono'; color:#ff6b6b; font-size:0.78em; font-weight:700; letter-spacing:0.12em; text-align:center;">GAPS</div>
    <div v-click="3" class="pc-card pc-red">
      <div class="pc-icon">
        <svg viewBox="0 0 24 24" width="38" height="38"><circle cx="12" cy="12" r="10.5" fill="none" stroke="#ff6b6b" stroke-width="1.6"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round"/></svg>
      </div>
      <div class="pc-label" style="color:#ff6b6b;">Built for simple statistical studies</div>
      <div class="pc-sub">The engine was originally designed for classical epidemiology and more basic statistics. It runs one-shot aggregate queries, not heavy or iterative computation.</div>
    </div>
    <div v-click="4" class="pc-card pc-red">
      <div class="pc-icon">
        <svg viewBox="0 0 24 24" width="38" height="38"><circle cx="12" cy="12" r="10.5" fill="none" stroke="#ff6b6b" stroke-width="1.6"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7" fill="none" stroke="#ff6b6b" stroke-width="2" stroke-linecap="round"/></svg>
      </div>
      <div class="pc-label" style="color:#ff6b6b;">No machine-learning tools</div>
      <div class="pc-sub">No way to train a model over many rounds: no iterative parameter exchange, no support for modern neural networks or deep learning.</div>
    </div>
  </div>
</div>

<style scoped>
.pc-card {
  border: 1px solid;
  border-radius: 12px;
  padding: 1.1em 1em;
  text-align: center;
}
.pc-green { border-color: rgba(102,221,170,0.30); background: rgba(102,221,170,0.07); }
.pc-red   { border-color: rgba(255,107,107,0.30); background: rgba(255,107,107,0.07); }
.pc-icon { display: flex; justify-content: center; margin-bottom: 0.5em; }
.pc-label {
  font-family: 'Roboto Mono', monospace;
  font-weight: 600;
  font-size: 0.95em;
  margin-bottom: 0.4em;
}
.pc-sub {
  font-size: 0.7em;
  color: #b0b8c0;
  line-height: 1.45;
}
</style>

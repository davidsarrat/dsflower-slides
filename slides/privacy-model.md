## Privacy Model

Four layers of protection against the analyst:

<div style="display: flex; flex-direction: column; gap: 8px; margin-top: 1em;">

<div v-click style="background: rgba(102,221,170,0.10); border: 1px solid rgba(102,221,170,0.15); border-radius: 10px; padding: 0.5em 1.2em;">
  <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
    <span style="font-family: 'Roboto Mono', monospace; color: #66ddaa; font-weight: 600; font-size: 1.1em;">Layer 1</span>
    <span style="color: #e0d8d0; font-weight: 500;"><Glossary term="SecAgg+" /></span>
  </div>
  <div style="color: #b8b0a8; font-size: 0.9em;">Individual weight updates are encrypted. The researcher only sees the <strong>aggregate</strong>.</div>
</div>

<div v-click style="background: rgba(102,221,170,0.10); border: 1px solid rgba(102,221,170,0.15); border-radius: 10px; padding: 0.5em 1.2em;">
  <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
    <span style="font-family: 'Roboto Mono', monospace; color: #66ddaa; font-weight: 600; font-size: 1.1em;">Layer 2</span>
    <span style="color: #e0d8d0; font-weight: 500;"><Glossary term="Differential Privacy" /></span>
  </div>
  <div style="color: #b8b0a8; font-size: 0.9em;">Each node adds calibrated noise. Formal DP-SGD via Opacus, or lighter update-level noise for any framework.</div>
</div>

<div v-click style="background: rgba(102,221,170,0.10); border: 1px solid rgba(102,221,170,0.15); border-radius: 10px; padding: 0.5em 1.2em;">
  <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
    <span style="font-family: 'Roboto Mono', monospace; color: #66ddaa; font-weight: 600; font-size: 1.1em;">Layer 3</span>
    <span style="color: #e0d8d0; font-weight: 500;"><Glossary term="Disclosure control" /></span>
  </div>
  <div style="color: #b8b0a8; font-size: 0.9em;">Bucketed counts, suppressed per-node metrics, minimum sample sizes.</div>
</div>

<div v-click style="background: rgba(102,221,170,0.10); border: 1px solid rgba(102,221,170,0.15); border-radius: 10px; padding: 0.5em 1.2em;">
  <div style="display: flex; align-items: baseline; gap: 14px; margin-bottom: 2px;">
    <span style="font-family: 'Roboto Mono', monospace; color: #66ddaa; font-weight: 600; font-size: 1.1em;">Layer 4</span>
    <span style="color: #e0d8d0; font-weight: 500;">Approved functions (templates)</span>
  </div>
  <div style="color: #b8b0a8; font-size: 0.9em;">Only predefined Flower apps installed on the server can run. The analyst invokes a template by name, and only if every node has it.</div>
</div>

</div>

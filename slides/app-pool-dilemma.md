## Growing the App Pool

Today dsFlower ships a fixed set of reviewed templates. The open question is how to grow that pool without breaking the trust model.

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click class="step-card" style="border-color: rgba(255,170,80,0.28);">
  <div style="font-family: 'Roboto Mono', monospace; color: #ffaa50; font-weight: 600; font-size: 0.78em; letter-spacing: 0.05em;">DOESN'T SCALE</div>
  <div style="color: #e0d8d0; font-weight: 600; font-size: 1.15em; margin-top: 0.35em;">Hardcode more templates</div>
  <div style="color: #b8b0a8; font-size: 0.92em; margin-top: 0.45em;">Every new model waits on the dsFlower maintainers. The pool grows only as fast as one team can build.</div>
</div>

<div v-click class="step-card" style="border-color: rgba(255,120,120,0.32);">
  <div style="font-family: 'Roboto Mono', monospace; color: #ff7878; font-weight: 600; font-size: 0.78em; letter-spacing: 0.05em;">UNTRUSTED</div>
  <div style="color: #e0d8d0; font-weight: 600; font-size: 1.15em; margin-top: 0.35em;">Let analysts ship their own code</div>
  <div style="color: #b8b0a8; font-size: 0.92em; margin-top: 0.45em;">Running unreviewed code on patient data breaks the guarantees DataSHIELD is built on.</div>
</div>

</div>

<div class="mt-8 text-center glow-pulse" v-click style="color: #66ddaa; font-size: 1.15em; font-weight: 600;">
There is a third way.
</div>

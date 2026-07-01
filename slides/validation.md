## Does it actually work?

<div class="grid grid-cols-3 gap-4 mt-3">

<div class="step-card text-center">
  <div style="font-family: 'Roboto Mono'; font-size: 2.2em; color: #FFD000; font-weight: 600;">20<span style="font-size: 0.5em; color: #8a7d70;">/20</span></div>
  <div style="font-size: 0.8em; color: #c8b8a8;">model templates validated</div>
  <div style="font-size: 0.65em; color: #8a7d70; margin-top: 0.3em;">17 tabular/sequence/survival + 3 vision</div>
</div>

<div class="step-card text-center">
  <div style="font-family: 'Roboto Mono'; font-size: 2.2em; color: #66ddaa; font-weight: 600;">0</div>
  <div style="font-size: 0.8em; color: #c8b8a8;">client failures</div>
  <div style="font-size: 0.65em; color: #8a7d70; margin-top: 0.3em;">across every clinical & privacy run</div>
</div>

<div class="step-card text-center">
  <div style="font-family: 'Roboto Mono'; font-size: 2.2em; color: #88ccff; font-weight: 600;">3</div>
  <div style="font-size: 0.8em; color: #c8b8a8;">sites per federated run</div>
  <div style="font-size: 0.65em; color: #8a7d70; margin-top: 0.3em;">data never leaves any of them</div>
</div>

</div>

<div class="mt-4" v-click>

| Real-data evidence | Result |
|---|---|
| **PathMNIST** direct-image ResNet (1,500 images) | central 0.9947 vs federated **0.9860** accuracy |
| **LUNG1** radiomics from CT (422 rows) | loss 0.6503 &rarr; **0.6474** |
| **Clinical privacy** profiles (Breast Cancer, Diabetes, SUPPORT2) | all runs pass under SecAgg+ / DP-SGD |

</div>

<div v-click class="mt-3" style="font-size: 0.85em; color: #c8b8a8;">

Federated accuracy lands **within a hair of pooling all the data**, without the data ever moving.

</div>

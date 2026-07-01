## Models that ship with dsFlowerClient

<div class="grid grid-cols-2 gap-6 mt-2 items-center">
<div>

| Track | Built-in models |
|---|---|
| **Tabular** | LogReg · Linear · MLP |
| | Multiclass · Multilabel · Poisson |
| **Sequence** | LSTM · TCN |
| **Vision** | ResNet-18 · DenseNet-121 |
| **Trees** | XGBoost <span style="color:#a89888;">(DP-GBDT)</span> |

</div>
<div>

Every neural model is a **Tier-1 nn.Module spec** — pick it by name, the node builds it.

The stack is deliberately small:

<div class="step-card" style="padding:0.6em 1em; margin-top:0.6em;">
<span style="color:#FFD000; font-family:'Roboto Mono',monospace; font-size:0.9em;">PyTorch · torchvision · Opacus</span>
<div style="color:#b8b0a8; font-size:0.85em; margin-top:2px;">+ image readers for dsImaging. No scikit-learn, no bespoke frameworks.</div>
</div>

</div>
</div>

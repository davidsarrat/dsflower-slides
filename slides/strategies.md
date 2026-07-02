## Aggregation strategies

<div style="color:#c8b8a8; margin-top:0.3em;">You choose how the SuperLink combines the sites each round.</div>

<div class="grid grid-cols-2 gap-6 mt-4 items-center">
<div>

| Strategy | On the SuperLink |
|---|---|
| <span class="g-term" data-g="FedAvg">**FedAvg**</span> · default | Weighted average, by size |
| <span class="g-term" data-g="FedAdam">FedAdam</span> · <span class="g-term" data-g="FedAdagrad">FedAdagrad</span> · FedYogi | Adaptive optimizer |
| FedAvgM | Server momentum |

</div>
<div>

```r
ds.flower.fit(
  conns, target = "malignant",
  model = "mlp",
  strategy = "fedadam"
)
```

</div>
</div>

<div class="mt-4" style="color:#a89888; font-size:0.88em;">
Safe to choose freely: aggregation runs on updates that are <strong>already differentially private</strong>, so it can never weaken the guarantee.
</div>

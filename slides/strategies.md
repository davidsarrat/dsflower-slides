## Aggregation strategies — you choose, DP stays

| Strategy | What the SuperLink does | When |
|---|---|---|
| <span class="g-term" data-g="FedAvg">**FedAvg**</span> | Weighted average, by dataset size | Default |
| <span class="g-term" data-g="FedAdam">**FedAdam**</span> | Server-side Adam on the aggregate | Unstable convergence |
| <span class="g-term" data-g="FedAdagrad">**FedAdagrad**</span> | Server-side Adagrad | Sparse features |
| **FedYogi** | Server-side Yogi (steadier Adam) | Noisy updates |
| **FedAvgM** | Server-side momentum | Slow drift |

<div class="grid grid-cols-2 gap-6 mt-4 items-center">
<div>

```r
ds.flower.fit(
  conns, target = "malignant", model = "mlp",
  strategy = "fedadam", rounds = 10L
)
```

</div>
<div>

You can pick **any** of them, because the strategy runs on the researcher's SuperLink over updates that are **already differentially private**. By DP's **post-processing** theorem, no aggregation can weaken the (ε, δ) guarantee.

<div style="color:#a89888; font-size:0.82em; margin-top:0.6em;">Neural track; boosted trees keep their own booster aggregation.</div>

</div>
</div>

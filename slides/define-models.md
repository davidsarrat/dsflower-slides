## Defining your own model

<div class="grid grid-cols-2 gap-5 mt-2">
<div>

<div style="font-family:'Roboto Mono',monospace; color:#66ddaa; font-weight:600; margin-bottom:0.3em;">Tier 1 — register a spec</div>

```r
ds.flower.register_model(
  name  = "my_net",
  track = "neural",
  loss  = "cross_entropy",
  generate = function(p) {
    # declarative spec: allowlisted
    # torch layers only, no code
    list(hidden = c(128L, 64L),
         activation = "relu")
  }
)

ds.flower.fit(conns, model = "my_net", ...)
```

</div>
<div>

<div style="font-family:'Roboto Mono',monospace; color:#FFD000; font-weight:600; margin-bottom:0.3em;">Tier 2 — upload a full app</div>

```r
# a complete Flower app directory
ds.flower.app.upload(conns, app_dir = "my_app/")
```

<div style="color:#b8b0a8; font-size:0.88em; margin-top:0.9em; line-height:1.7;">
The spec is <strong>data, never code</strong> — the node builds and trains it under DP-SGD.<br/><br/>
The app <em>is</em> code — so it passes <strong>the gate</strong> (scan · sandbox · egress DP · hash) before it can touch any data.
</div>

</div>
</div>

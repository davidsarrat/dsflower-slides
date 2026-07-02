## The whole API is one call

<div class="grid grid-cols-2 gap-6 mt-3 items-center">
<div>

```r
# your data is already loaded under symbol "D"
conns <- datashield.login(
  builder$build(), assign = TRUE, symbol = "D")

fit <- ds.flower.fit(
  conns,
  target = "diagnosis",
  model  = "mlp",
  rounds = 10L
)
```

</div>
<div>

Three plain-language choices:

- `model`: **what** to train
- `target`: the **outcome** column
- `rounds`: **how long**

<div class="mt-4" v-click>

That's it. **Privacy is enforced by the server**, so the guarantee holds no matter what the analyst writes. There is no privacy knob to get wrong.

</div>

</div>
</div>

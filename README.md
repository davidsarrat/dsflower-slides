# dsFlower — slides

Slidev deck introducing **dsFlower**: privacy-preserving federated learning for
biomedical research, built on [Flower](https://flower.ai) and
[DataSHIELD](https://www.datashield.org).

**Live:** https://davidsarrat.github.io/dsflower-slides/

Covers: what Flower is (SuperLink / SuperNode, ClientApp / ServerApp + app
submission), the DataSHIELD architecture, the DSI transport (no exposed gRPC —
Flower's bytes ride the DataSHIELD TLS channel), the server- and client-side
stacks (PyTorch + torchvision + Opacus only), **differential privacy** as the
single enforced mechanism (DP-SGD / DP-GBDT / output perturbation, RDP ledger),
the two model tiers (nn.Module spec vs. gated uploaded app), the one-call
training API and the model-definition API, aggregation (FedAvg / FedBN), and
**dsImaging** (images served from a `dsimaging-store` MinIO collection, managed
with `dsimaging-admin`, resolved as an Opal resource).

Pairs with the live pkgdown demos at
https://davidsarrat.github.io/dsflower-demos/.

## Develop

```bash
npm install
npm run dev      # http://localhost:3030
npm run build    # static build into dist/
```

Slides live in `slides/` and are wired together from `slides.md`. Aesthetic and
the glossary popups live in `global-top.vue` / `global-bottom.vue` / `styles/`.
Deployed to GitHub Pages by `.github/workflows/deploy.yml` on push to `main`.

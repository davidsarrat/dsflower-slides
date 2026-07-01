<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'
import { useNav } from '@slidev/client'

const { currentPage, total } = useNav()

// Reset demo slide when navigating backward past it
watch(currentPage, (newPage, oldPage) => {
  if (oldPage > newPage && window.__demoResetFn) {
    window.__demoResetFn()
  }
})

// ── Global glossary popup (works inside markdown tables) ──
const glossaryOpen = ref(false)
const glossaryTitle = ref('')
const glossaryBody = ref('')

const glossaryMap = {
  'DP-SGD': { title: 'Differentially-Private SGD (DP-SGD)', body: `The differential-privacy mechanism for the <strong>neural track</strong>, via <strong>Opacus</strong>. During training each patient's gradient is <strong>clipped</strong> to a fixed norm, then <strong>calibrated Gaussian noise</strong> is added before the optimizer step.<br/><br/>This gives a provable <strong>(ε, δ)</strong> bound: a mathematical limit on how much any single patient can influence the model. The privacy budget is tracked per-dataset in a server-side <strong>RDP ledger</strong>, and the analyst can never exceed the server's ε ceiling.` },
  'Opacus': { title: 'Opacus (DP-SGD engine)', body: `<strong>Opacus</strong> is Meta's open-source library for training PyTorch models with <strong>differential privacy</strong>.<br/><br/>It wraps the model, optimizer and dataloader to automatically clip <strong>per-sample</strong> gradients and add calibrated noise, with a built-in privacy accountant that reports the spent (ε, δ). It also swaps DP-incompatible layers automatically (e.g. BatchNorm → GroupNorm).<br/><br/>In dsFlower it powers the enforced-DP neural track; nothing about it is chosen by the analyst.` },
  'Differential Privacy': { title: 'Differential Privacy', body: `The <strong>one privacy mechanism</strong> dsFlower enforces. Informally: the model's output is (almost) the <strong>same whether or not any single patient was in the data</strong>, so nothing the analyst receives can be traced back to an individual.<br/><br/>Formally it gives an <strong>(ε, δ)</strong> guarantee — ε bounds the privacy loss, δ a small failure probability. The right mechanism is applied per method: <strong>DP-SGD</strong> (neural), <strong>DP-GBDT</strong> (trees), <strong>output perturbation</strong> (egress). It is server-enforced: fixed ceilings on ε / δ / clip and a per-dataset RDP ledger the analyst can only read.` },
  'DP-GBDT': { title: 'DP-GBDT (trees track)', body: `The differential-privacy mechanism for the <strong>trees track</strong> (gradient-boosted decision trees).<br/><br/>Split gains and leaf values are computed from <strong>clipped, noised</strong> gradient/Hessian sums (an <strong>S-GBDT</strong>-style mechanism), so each tree respects the same <strong>(ε, δ)</strong> budget as the neural track. Implemented in pure NumPy — no XGBoost library is imported on the node.` },
  'Output perturbation': { title: 'Output perturbation (egress DP)', body: `A model-agnostic DP mechanism applied at <strong>egress</strong>: whatever leaves the node (a weight delta, a summary) is <strong>clipped and noised</strong> to satisfy the (ε, δ) budget before it is released.<br/><br/>It is the universal fallback — it works for any computation, including a researcher-uploaded app — though for a given budget it is looser than DP-SGD, which injects noise <em>inside</em> the training loop.` },
  'RDP ledger': { title: 'RDP privacy ledger', body: `Every DP release spends <strong>privacy budget</strong>. dsFlower tracks it per-dataset in a persistent server-side ledger using <strong>Rényi Differential Privacy (RDP)</strong> accounting, which composes many noisy steps tightly and converts to a final (ε, δ).<br/><br/>The analyst can only <strong>read</strong> the remaining budget; the server refuses any run that would exceed its ε ceiling.` },
  'DSI tunnel': { title: 'DSI transport (no exposed gRPC)', body: `Flower normally connects its SuperNode ↔ SuperLink over a dedicated <strong>gRPC</strong> port. dsFlower removes that: it carries those very bytes <strong>over the existing DataSHIELD channel</strong> (DSI), the same authenticated <strong>HTTPS/TLS</strong> connection the researcher already uses with Opal.<br/><br/>A tiny node-side forwarder and an R relay spool the bytes both ways. Flower itself is untouched — only the <strong>transport</strong> changes — so no hospital has to open a new port or expose gRPC to the internet.` },
  'nn.Module spec': { title: 'Tier 1 — nn.Module spec', body: `The safe, default way to define a model. The researcher sends a <strong>declarative spec</strong> (a description, not code) built from an <strong>allowlisted vocabulary</strong> of stock torch layers. The <strong>node</strong> assembles the <code>nn.Module</code> and owns the training loop, loss and optimizer.<br/><br/>Because <strong>no researcher code runs on the node</strong>, per-sample DP-SGD is guaranteed by construction. This covers every built-in model.` },
  'App tier': { title: 'Tier 2 — uploaded app (gated)', body: `For anything the spec can't express, the researcher can upload a full <strong>Flower app</strong> (a FAB). This runs <strong>arbitrary code</strong> on the node, so it passes a <strong>gate</strong>: a fail-closed <strong>exfiltration scan</strong> (an app that imports network/IO is rejected before any data is touched), a <strong>sandbox</strong>, an <strong>egress DP</strong> filter (output perturbation), and a <strong>SHA-256</strong> hash pinned and verified identically on every node.` },
  'Disclosure control': { title: 'Disclosure control', body: `The standard <strong>DataSHIELD</strong> guardrails that sit under everything dsFlower does: <strong>minimum sample sizes</strong> before a computation may run, <strong>suppressed per-node metrics</strong> (only aggregates leave), and non-disclosive result checks.<br/><br/>Differential privacy protects the model updates; disclosure control protects every other value the node returns.` },
  'FedAvg / FedProx / FedOpt': { title: 'Federated aggregation strategies', body: `<strong>FedAvg</strong>: weighted mean of the model weights from all sites, proportional to dataset sizes. Simple and effective when data is similar across sites.<br/><br/><strong>FedProx</strong>: adds a proximal penalty so no site's model drifts too far from the global one. For <strong>non-IID</strong> data (different patient populations).<br/><br/><strong>FedOpt</strong> (FedAdam, FedAdagrad): the SuperLink applies an <strong>adaptive optimizer</strong> to the aggregated update instead of plain averaging. Helps unstable convergence.<br/><br/><strong>FedBN</strong>: excludes BatchNorm from aggregation — each site keeps its own stats. For imaging with different scanners.` },
  'FedProx': { title: 'FedProx (Federated Proximal)', body: `A variant of FedAvg that adds a <strong>proximal penalty term</strong> to each site's local objective.<br/><br/>The penalty keeps each site's model from diverging too far from the current global model (controlled by <strong>proximal_mu</strong>). Essential for <strong>non-IID data</strong>: when hospitals have different patient populations, prevalences or demographics, plain FedAvg can degrade as local models drift apart.` },
  'FedAvg': { title: 'FedAvg (Federated Averaging)', body: `The standard federated learning aggregation strategy. Each hospital trains locally, sends its weight updates to the SuperLink, which computes the <strong>weighted mean</strong> proportional to dataset sizes.<br/><br/>Simple and effective when data distributions are <strong>similar across sites</strong>. For heterogeneous data, consider FedProx or FedAdam.` },
  'FedAdam': { title: 'FedAdam (Federated Adam)', body: `Part of the <strong>FedOpt</strong> family. Instead of simple averaging, the SuperLink applies the <strong>Adam optimizer</strong> (adaptive learning rates with momentum) to the aggregated weight updates.<br/><br/>Adam maintains per-parameter learning rates that adapt based on gradient history. This helps when training is <strong>unstable</strong> or convergence is slow.<br/><br/>Configured via <strong>server_learning_rate</strong> and <strong>tau</strong> (pseudo-gradient scaling).` },
  'FedAdagrad': { title: 'FedAdagrad (Federated Adagrad)', body: `Part of the <strong>FedOpt</strong> family. The SuperLink applies <strong>Adagrad</strong> (adaptive gradient) to the aggregated updates.<br/><br/>Adagrad accumulates squared gradients to scale learning rates per-parameter. Particularly useful for <strong>sparse features</strong> where some variables appear rarely across hospitals.<br/><br/>Configured via <strong>server_learning_rate</strong> and <strong>tau</strong>.` },
  'FedBN': { title: 'FedBN (Federated Batch Normalization)', body: `Excludes <strong>BatchNorm parameters</strong> from federated aggregation. Each hospital keeps its own batch normalization statistics (mean, variance).<br/><br/>Essential for <strong>medical imaging</strong> where different hospitals use different scanners, protocols, or staining methods. The intensity distributions vary across sites, so sharing BatchNorm statistics would degrade the model.<br/><br/>Only the non-BN weights (convolutions, fully connected layers) are averaged across sites.` },
}

function onGlossaryClick(e) {
  const el = e.target.closest('.g-term') || (e.target.classList?.contains('g-term') ? e.target : null)
  if (!el) return
  const term = el.dataset?.g || el.getAttribute('data-g')
  const entry = glossaryMap[term]
  if (entry) {
    glossaryTitle.value = entry.title
    glossaryBody.value = entry.body
    glossaryOpen.value = true
  }
}

function closeGlossary(e) {
  if (e.target === e.currentTarget) glossaryOpen.value = false
}

onMounted(() => document.addEventListener('click', onGlossaryClick))
onUnmounted(() => document.removeEventListener('click', onGlossaryClick))

// Countdown: 20 minutes
const totalSeconds = ref(20 * 60)
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    if (totalSeconds.value > 0) totalSeconds.value--
  }, 1000)
})

onUnmounted(() => clearInterval(timer))

const minutes = computed(() => Math.floor(totalSeconds.value / 60))
const seconds = computed(() => totalSeconds.value % 60)
const timeStr = computed(() =>
  `${String(minutes.value).padStart(2, '0')}:${String(seconds.value).padStart(2, '0')}`
)
const isLow = computed(() => totalSeconds.value < 60)

// Slide counter: exclude cover (1) and closing (last)
const showCountdown = computed(() => currentPage.value < total.value)
const isContentSlide = computed(() => currentPage.value > 1 && currentPage.value < total.value)
const contentIndex = computed(() => currentPage.value - 1)
const contentTotal = computed(() => total.value - 2)
</script>

<template>
  <!-- Countdown top-right (content slides only) -->
  <div v-if="showCountdown" class="countdown" :class="{ low: isLow }">
    {{ timeStr }}
  </div>

  <!-- Slide counter bottom-right (content slides only) -->
  <div v-if="isContentSlide" class="slide-counter">
    {{ contentIndex }} / {{ contentTotal }}
  </div>

  <!-- Global glossary popup -->
  <div v-if="glossaryOpen" @click="closeGlossary" class="glossary-backdrop">
    <div class="glossary-modal">
      <button @click="glossaryOpen = false" class="glossary-close">&times;</button>
      <div class="glossary-title">{{ glossaryTitle }}</div>
      <div class="glossary-body" v-html="glossaryBody" />
    </div>
  </div>
</template>

<style scoped>
.countdown {
  position: fixed;
  top: 16px;
  right: 20px;
  font-family: 'Roboto Mono', monospace;
  font-size: 14px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.5);
  z-index: 100;
  letter-spacing: 0.05em;
}

.countdown.low {
  color: rgba(255, 80, 60, 0.8);
}

.slide-counter {
  position: fixed;
  bottom: 16px;
  right: 20px;
  font-family: 'Roboto Mono', monospace;
  font-size: 13px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.4);
  z-index: 100;
  letter-spacing: 0.05em;
}

.glossary-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.65);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.glossary-modal {
  background: linear-gradient(135deg, rgba(20,14,10,0.98), rgba(30,20,14,0.98));
  border: 1px solid rgba(255,208,0,0.15);
  border-radius: 16px;
  max-width: 580px;
  width: 92%;
  padding: 2em 2.4em;
  position: relative;
  box-shadow: 0 12px 48px rgba(0,0,0,0.5);
}

.glossary-close {
  position: absolute;
  top: 14px;
  right: 18px;
  background: none;
  border: none;
  color: #888;
  font-size: 1.5em;
  cursor: pointer;
  line-height: 1;
  transition: color 0.2s;
}
.glossary-close:hover { color: #e0d8d0; }

.glossary-title {
  color: #FFD000;
  font-family: 'Roboto Mono', monospace;
  font-size: 1.15em;
  font-weight: 600;
  margin-bottom: 1em;
  padding-right: 1.5em;
}

.glossary-body {
  color: #d8d0c8;
  font-family: 'Montserrat', sans-serif;
  font-size: 0.95em;
  line-height: 1.85;
}
.glossary-body :deep(strong) {
  color: #FFD000;
  font-weight: 600;
}
</style>

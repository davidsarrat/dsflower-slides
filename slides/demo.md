<script setup>
import { ref, onMounted, onActivated, nextTick } from 'vue'
import { useSlideContext } from '@slidev/client'

const terminal = ref(null)
const slideCtx = useSlideContext()
let debounce = null

function resetDemo() {
  slideCtx.$clicks.value = 0
  nextTick(() => {
    nextTick(() => {
      if (terminal.value) {
        terminal.value.scrollTop = 0
        // Force-reset animations via reflow trick
        terminal.value.querySelectorAll('.exec-lines > div').forEach(el => {
          el.style.opacity = ''
          el.style.animationName = 'none'
          void el.offsetHeight
          el.style.animationName = ''
        })
      }
    })
  })
}

onActivated(() => resetDemo())
window.__demoResetFn = resetDemo

onMounted(() => {
  if (!terminal.value) return
  terminal.value.scrollTop = 0
  const observer = new MutationObserver(() => {
    clearTimeout(debounce)
    debounce = setTimeout(() => {
      if (!terminal.value) return
      const inner = terminal.value.firstElementChild
      if (!inner) return
      const visible = Array.from(inner.children).filter(
        el => !el.classList.contains('slidev-vclick-hidden')
      )
      const last = visible[visible.length - 1]
      if (last) {
        last.scrollIntoView({ behavior: 'smooth', block: 'end' })
      }
    }, 120)
  })
  observer.observe(terminal.value, {
    subtree: true, attributes: true, attributeFilter: ['class']
  })
})
</script>

## Usage Demo

<div ref="terminal" style="overflow-y: auto; scroll-behavior: smooth; height: 430px; margin-top: 0.3em; scrollbar-width: none;">
<div style="font-size: 0.62em; line-height: 1.4; font-family: 'Roboto Mono', monospace;">

<!-- Experiment setup -->
<div style="background: rgba(136,204,255,0.04); border: 1px solid rgba(136,204,255,0.12); border-radius: 10px; padding: 0.8em 1.2em; margin-bottom: 10px;">

<div style="color: #88ccff; font-size: 1.2em; font-weight: 600; margin-bottom: 6px;">Federated Heart Disease Risk</div>

<div style="color: #c8c0b8; font-size: 0.92em; line-height: 1.5; margin-bottom: 12px;">These are three of the institutions that originally collected the UCI Heart Disease data. Each keeps its own patients and never shares a row; together they train one shared model to predict whether a patient has heart disease.</div>

<!-- Institutions grid -->
<div style="display: flex; gap: 8px; margin-bottom: 12px;">
  <div style="flex:1; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10); border-radius: 8px; padding: 8px 10px; text-align: center;">
    <div style="color: #FFD000; font-weight: 600; font-size: 1.05em;">Cleveland</div>
    <div style="color: #c8c0b8; font-size: 0.85em;">USA</div>
    <div style="color: #88ccff; font-size: 0.9em; margin-top: 2px;">303</div>
  </div>
  <div style="flex:1; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10); border-radius: 8px; padding: 8px 10px; text-align: center;">
    <div style="color: #FFD000; font-weight: 600; font-size: 1.05em;">Hungary</div>
    <div style="color: #c8c0b8; font-size: 0.85em;">Budapest</div>
    <div style="color: #88ccff; font-size: 0.9em; margin-top: 2px;">261</div>
  </div>
  <div style="flex:1; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.10); border-radius: 8px; padding: 8px 10px; text-align: center;">
    <div style="color: #FFD000; font-weight: 600; font-size: 1.05em;">VA Long Beach</div>
    <div style="color: #c8c0b8; font-size: 0.85em;">USA</div>
    <div style="color: #88ccff; font-size: 0.9em; margin-top: 2px;">130</div>
  </div>
</div>

<!-- Dataset + Target -->
<div style="display: flex; gap: 16px; margin-bottom: 10px;">
  <div style="flex: 1;">
    <div style="color: #ffb366; font-weight: 500; margin-bottom: 3px;">Dataset</div>
    <div style="color: #e0d8d0;">UCI Heart Disease</div>
    <div style="color: #b8b0a8; font-size: 0.9em;">694 patients total (data never pooled)</div>
  </div>
  <div style="flex: 1;">
    <div style="color: #ffb366; font-weight: 500; margin-bottom: 5px;">Target</div>
    <div style="margin-bottom: 6px;"><span style="background:rgba(102,221,170,0.12); border:1px solid rgba(102,221,170,0.25); border-radius:4px; padding:3px 10px; color:#66ddaa;">outcome</span></div>
    <div style="color: #c8c0b8; font-size: 0.9em;">binary &middot; heart disease present</div>
  </div>
</div>

<!-- Features -->
<div style="margin-bottom: 10px;">
  <div style="color: #ffb366; font-weight: 500; margin-bottom: 4px;">Features <span style="color: #c8c0b8; font-weight: 400;">(10 clinical variables)</span></div>
  <div style="display: flex; flex-wrap: wrap; gap: 4px;">
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">age</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">sex</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">cp</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">trestbps</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">chol</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">fbs</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">restecg</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">thalach</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">exang</span>
    <span style="background:rgba(255,208,0,0.10); border:1px solid rgba(255,208,0,0.18); border-radius:4px; padding:2px 7px; color:#FFD000;">oldpeak</span>
  </div>
  <div style="color: #b8b0a8; font-size: 0.88em; margin-top: 5px;">Age and sex, chest-pain type, blood pressure, cholesterol, blood sugar, resting ECG, and the heart's response to exercise.</div>
</div>

<!-- Model config -->
<div style="display: flex; gap: 20px; padding-top: 6px; border-top: 1px solid rgba(255,255,255,0.06);">
  <div>
    <span style="color:#88ccff; font-weight: 500;">Model</span>
    <span style="color:#e0d8d0; margin-left: 6px;">Logistic Regression</span>
  </div>
  <div>
    <span style="color:#88ccff; font-weight: 500;">Strategy</span>
    <span style="color:#e0d8d0; margin-left: 6px;">FedAvg</span>
  </div>
  <div>
    <span style="color:#88ccff; font-weight: 500;">Rounds</span>
    <span style="color:#e0d8d0; margin-left: 6px;">10</span>
  </div>
</div>

</div>

<!-- Libraries -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; color: #c8b8a8;">
<span style="color:#78a9ff;">library</span>(<span style="color:#FFD000;">DSI</span>); <span style="color:#78a9ff;">library</span>(<span style="color:#FFD000;">DSOpal</span>); <span style="color:#78a9ff;">library</span>(<span style="color:#FFD000;">dsFlowerClient</span>)
</div>

<!-- Login -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; margin-top: 4px; color: #c8b8a8;">
builder <span style="color:#b0a8a0;">&lt;-</span> DSI::<span style="color:#78a9ff;">newDSLoginBuilder</span>()
<br/>builder$<span style="color:#78a9ff;">append</span>(server = <span style="color:#ffaacc;">"cleveland"</span>, url = <span style="color:#ffaacc;">"https://datashield.ccf.org"</span>, table = <span style="color:#ffaacc;">"dsflower_demo.heart_cleveland"</span>, <span style="color:#666;">...</span>)
<br/>builder$<span style="color:#78a9ff;">append</span>(server = <span style="color:#ffaacc;">"hungary"</span>, url = <span style="color:#ffaacc;">"https://datashield.semmelweis.hu"</span>, table = <span style="color:#ffaacc;">"dsflower_demo.heart_hungary"</span>, <span style="color:#666;">...</span>)
<br/>builder$<span style="color:#78a9ff;">append</span>(server = <span style="color:#ffaacc;">"va"</span>, url = <span style="color:#ffaacc;">"https://datashield.va.gov"</span>, table = <span style="color:#ffaacc;">"dsflower_demo.heart_va"</span>, <span style="color:#666;">...</span>)
<br/>conns <span style="color:#b0a8a0;">&lt;-</span> DSI::<span style="color:#78a9ff;">datashield.login</span>(logins = builder$<span style="color:#78a9ff;">build</span>(), assign = <span style="color:#88ccff;">TRUE</span>, symbol = <span style="color:#ffaacc;">"D"</span>)
</div>

<div v-click class="exec-lines" style="background: rgba(15,10,8,0.5); border-left: 3px solid #444; border-radius: 0 6px 6px 0; padding: 0.3em 0.7em; margin: 2px 0; color: #b8b0a8;">
<div style="animation-delay:0.1s">Logging into the collaborating servers</div>
<div style="animation-delay:0.7s">&nbsp; Login cleveland: <span style="color:#66ddaa;">OK</span> <span style="color:#b0a8a0;">(244 rows x 11 cols)</span></div>
<div style="animation-delay:1.4s">&nbsp; Login hungary: <span style="color:#66ddaa;">OK</span> <span style="color:#b0a8a0;">(210 rows x 11 cols)</span></div>
<div style="animation-delay:2.0s">&nbsp; Login va: <span style="color:#66ddaa;">OK</span> <span style="color:#b0a8a0;">(105 rows x 11 cols)</span></div>
<div style="animation-delay:2.4s">Assigned tables to symbol "D" &middot; <span style="color:#e0d8d0;">559 patients</span> across 3 sites (data never pooled)</div>
</div>

<!-- Fit -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; margin-top: 4px; color: #c8b8a8;">
run <span style="color:#b0a8a0;">&lt;-</span> dsFlowerClient::<span style="color:#78a9ff;">ds.flower.fit</span>(
<br/>&nbsp;&nbsp;conns,
<br/>&nbsp;&nbsp;symbol &nbsp;&nbsp;= <span style="color:#ffaacc;">"D"</span>,
<br/>&nbsp;&nbsp;target &nbsp;&nbsp;= <span style="color:#ffaacc;">"outcome"</span>,
<br/>&nbsp;&nbsp;features = <span style="color:#78a9ff;">c</span>(<span style="color:#ffaacc;">"age"</span>, <span style="color:#ffaacc;">"sex"</span>, <span style="color:#ffaacc;">"cp"</span>, <span style="color:#ffaacc;">"trestbps"</span>, <span style="color:#ffaacc;">"chol"</span>, <span style="color:#ffaacc;">"fbs"</span>, <span style="color:#ffaacc;">"restecg"</span>, <span style="color:#ffaacc;">"thalach"</span>, <span style="color:#ffaacc;">"exang"</span>, <span style="color:#ffaacc;">"oldpeak"</span>),
<br/>&nbsp;&nbsp;model &nbsp;&nbsp;&nbsp;= <span style="color:#ffaacc;">"sklearn_logreg"</span>,
<br/>&nbsp;&nbsp;strategy = <span style="color:#ffaacc;">"fedavg"</span>,
<br/>&nbsp;&nbsp;rounds &nbsp;&nbsp;= <span style="color:#88ccff;">10L</span>
<br/>)
</div>

<!-- Run output -->
<div v-click class="exec-lines" style="background: rgba(15,10,8,0.5); border-left: 3px solid #444; border-radius: 0 6px 6px 0; padding: 0.3em 0.7em; margin: 2px 0; color: #b8b0a8;">
<div style="animation-delay:0.3s">SuperLink started (PID: 16782)</div>
<div style="animation-delay:0.6s">&nbsp; Fleet API (SuperNodes): 127.0.0.1:9092</div>
<div style="animation-delay:1.0s">&nbsp; cleveland: SuperNode <span style="color:#66ddaa;">connected</span></div>
<div style="animation-delay:1.4s">&nbsp; hungary: SuperNode <span style="color:#66ddaa;">connected</span></div>
<div style="animation-delay:1.8s">&nbsp; va: SuperNode <span style="color:#66ddaa;">connected</span></div>
<div style="animation-delay:2.3s">&nbsp; Code verification <span style="color:#66ddaa;">passed</span> on all servers <span style="color:#b0a8a0;">(app hash matches server templates)</span></div>
<div style="animation-delay:3.0s"><span style="color:#88ccff;">[ROUND &nbsp;1/10]</span> 3 clients · distributed loss: 0.4490</div>
<div style="animation-delay:3.3s"><span style="color:#88ccff;">[ROUND &nbsp;2/10]</span> 3 clients · distributed loss: 0.4483</div>
<div style="animation-delay:3.6s"><span style="color:#88ccff;">[ROUND &nbsp;3/10]</span> 3 clients · distributed loss: 0.4474</div>
<div style="animation-delay:3.9s"><span style="color:#88ccff;">[ROUND &nbsp;4/10]</span> 3 clients · distributed loss: 0.4476</div>
<div style="animation-delay:4.2s"><span style="color:#88ccff;">[ROUND &nbsp;5/10]</span> 3 clients · distributed loss: 0.4469</div>
<div style="animation-delay:4.5s"><span style="color:#88ccff;">[ROUND &nbsp;6/10]</span> 3 clients · distributed loss: 0.4469</div>
<div style="animation-delay:4.8s"><span style="color:#88ccff;">[ROUND &nbsp;7/10]</span> 3 clients · distributed loss: 0.4461</div>
<div style="animation-delay:5.1s"><span style="color:#88ccff;">[ROUND &nbsp;8/10]</span> 3 clients · distributed loss: 0.4463</div>
<div style="animation-delay:5.4s"><span style="color:#88ccff;">[ROUND &nbsp;9/10]</span> 3 clients · distributed loss: 0.4453</div>
<div style="animation-delay:5.7s"><span style="color:#88ccff;">[ROUND 10/10]</span> 3 clients · distributed loss: 0.4451</div>
<div style="animation-delay:6.1s"><span style="color:#66ddaa;">Model saved to ./dsflower_output/sklearn_logreg_FedAvg_10r</span></div>
<div style="animation-delay:6.3s">SuperLink stopped.</div>
</div>

<!-- Validation: central vs federated parity -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; margin-top: 4px; color: #c8b8a8;">
<span style="color:#666;"># Validate on a held-out test set (135 patients, never seen in training)</span>
<br/>probs &nbsp;&nbsp;<span style="color:#b0a8a0;">&lt;-</span> <span style="color:#78a9ff;">ds.flower.predict</span>(run, newdata = test, type = <span style="color:#ffaacc;">"prob"</span>)
<br/>metrics <span style="color:#b0a8a0;">&lt;-</span> <span style="color:#78a9ff;">binary_metrics</span>(test$outcome, probs)
</div>

<div v-click style="background: rgba(15,10,8,0.5); border-left: 3px solid #66ddaa; border-radius: 0 6px 6px 0; padding: 0.4em 0.8em; margin: 2px 0; color: #b8b0a8;">
<div style="display:grid; grid-template-columns: 1.6fr 1fr 1fr 1fr; gap: 4px 12px; align-items:center;">
  <div style="color:#888;"></div><div style="color:#ffb366; text-align:right;">AUC</div><div style="color:#ffb366; text-align:right;">Accuracy</div><div style="color:#ffb366; text-align:right;">Log loss</div>
  <div style="color:#c8c0b8;">Central (pooled)</div><div style="text-align:right;">0.907</div><div style="text-align:right;">0.815</div><div style="text-align:right;">0.399</div>
  <div style="color:#e0d8d0;">Federated (dsFlower)</div><div style="text-align:right; color:#66ddaa;">0.902</div><div style="text-align:right; color:#66ddaa;">0.837</div><div style="text-align:right; color:#66ddaa;">0.412</div>
  <div style="color:#888;">&Delta; (fed &minus; central)</div><div style="text-align:right; color:#888;">&minus;0.005</div><div style="text-align:right; color:#888;">+0.022</div><div style="text-align:right; color:#888;">+0.013</div>
</div>
<div style="margin-top:6px; color:#b0a8a0;">Per-site held-out AUC &middot; cleveland <span style="color:#e0d8d0;">0.89</span> (n=59) &middot; hungary <span style="color:#e0d8d0;">0.93</span> (n=51) &middot; va <span style="color:#e0d8d0;">0.69</span> (n=25)</div>
<div style="margin-top:4px; color:#66ddaa;">Federated model matches the pooled-data baseline. No data ever moved.</div>
</div>

<!-- Predict on real held-out patients -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; margin-top: 4px; color: #c8b8a8;">
<span style="color:#666;"># 3 held-out patients (raw clinical values, all 10 features)</span>
<br/>patients <span style="color:#b0a8a0;">&lt;-</span> <span style="color:#78a9ff;">data.frame</span>(
<br/>&nbsp;&nbsp;age &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">61</span>, <span style="color:#88ccff;">53</span>, <span style="color:#88ccff;">69</span>),
<br/>&nbsp;&nbsp;sex &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">1</span>, <span style="color:#88ccff;">0</span>, <span style="color:#88ccff;">1</span>),
<br/>&nbsp;&nbsp;cp &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">4</span>, <span style="color:#88ccff;">2</span>, <span style="color:#88ccff;">4</span>),
<br/>&nbsp;&nbsp;trestbps = <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">140</span>, <span style="color:#88ccff;">140</span>, <span style="color:#88ccff;">140</span>),
<br/>&nbsp;&nbsp;chol &nbsp;&nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">207</span>, <span style="color:#88ccff;">216</span>, <span style="color:#88ccff;">208</span>),
<br/>&nbsp;&nbsp;fbs &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">0</span>, <span style="color:#88ccff;">0</span>, <span style="color:#88ccff;">0</span>),
<br/>&nbsp;&nbsp;restecg &nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">2</span>, <span style="color:#88ccff;">0</span>, <span style="color:#88ccff;">1</span>),
<br/>&nbsp;&nbsp;thalach &nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">138</span>, <span style="color:#88ccff;">142</span>, <span style="color:#88ccff;">140</span>),
<br/>&nbsp;&nbsp;exang &nbsp;&nbsp;&nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">1</span>, <span style="color:#88ccff;">1</span>, <span style="color:#88ccff;">1</span>),
<br/>&nbsp;&nbsp;oldpeak &nbsp;= <span style="color:#78a9ff;">c</span>(<span style="color:#88ccff;">1.9</span>, <span style="color:#88ccff;">2.0</span>, <span style="color:#88ccff;">2.0</span>))
<br/><span style="color:#78a9ff;">ds.flower.predict</span>(run, newdata = patients, type = <span style="color:#ffaacc;">"prob"</span>)
<br/><span style="color:#b0a8a0;">[1] 0.8820 0.4683 0.8904</span>
</div>

<div v-click style="background: rgba(15,10,8,0.5); border-left: 3px solid #444; border-radius: 0 6px 6px 0; padding: 0.4em 0.8em; margin: 2px 0; color: #b8b0a8;">
<div style="display:grid; grid-template-columns: 1.6fr 1fr 1fr; gap: 4px 12px; align-items:center;">
  <div style="color:#ffb366;">patient</div><div style="color:#ffb366; text-align:right;">pred. risk</div><div style="color:#ffb366; text-align:right;">actual</div>
  <div style="color:#b0a8a0;">61yo M · cp4</div><div style="text-align:right; color:#FFD000;">0.88</div><div style="text-align:right; color:#66ddaa;">disease &check;</div>
  <div style="color:#b0a8a0;">53yo F · cp2</div><div style="text-align:right; color:#FFD000;">0.47</div><div style="text-align:right; color:#66ddaa;">no disease &check;</div>
  <div style="color:#b0a8a0;">69yo M · cp4</div><div style="text-align:right; color:#FFD000;">0.89</div><div style="text-align:right; color:#66ddaa;">disease &check;</div>
</div>
</div>

<!-- Disconnect -->
<div v-click style="background: rgba(15,10,8,0.7); border-radius: 6px; padding: 0.5em 0.8em; margin-top: 4px; color: #c8b8a8;">
DSI::<span style="color:#78a9ff;">datashield.logout</span>(conns)
</div>

</div>
</div>

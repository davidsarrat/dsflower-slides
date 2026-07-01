---
class: match-slide
---

<div class="match-stage">

  <div class="match-title" :class="{ show: revealed }">It's a match!</div>

  <div class="match-photos">
    <div class="ava ava-left" :class="{ show: revealed }">
      <img src="/datashield-logo.png" />
    </div>
    <div class="ava ava-right" :class="{ show: revealed }">
      <img src="/flower-logo.png" />
    </div>
  </div>

  <div class="match-sub" :class="{ show: revealed }">DataSHIELD and Flower can combine federated learning capabilities with disclosure control mechanisms and biomedical domain expertise</div>

</div>

<script setup lang="ts">
import { ref } from 'vue'
import { onSlideEnter } from '@slidev/client'

// Wait for the slide-left transition (--slidev-transition-duration: 0.5s) to settle
// before playing, so the match animates after landing, not during the page change.
const ENTER_DELAY = 550
const revealed = ref(false)
onSlideEnter(() => {
  revealed.value = false
  setTimeout(() => { revealed.value = true }, ENTER_DELAY)
})
</script>

<style>
@font-face {
  font-family: 'Kaushan Script';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/kaushan-script.woff2') format('woff2');
}

.match-slide {
  background: linear-gradient(135deg, #ff7854 0%, #fd5068 45%, #fd267d 100%) !important;
  color: #fff;
}

.match-stage {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.6rem;
  overflow: hidden;
}

.match-title {
  font-family: 'Kaushan Script', cursive;
  font-size: 5.4em;
  line-height: 1;
  color: #fff;
  text-shadow: 0 3px 18px rgba(0,0,0,0.25);
  opacity: 0;
  transform: translateY(-22px) scale(0.7) rotate(-3deg);
  transition: opacity 0.5s ease, transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
  transition-delay: 0.15s;
}
.match-title.show {
  opacity: 1;
  transform: translateY(0) scale(1) rotate(0deg);
}

.match-photos {
  position: relative;
  width: 460px;
  height: 200px;
}

.ava {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 170px;
  height: 170px;
  margin: -85px 0 0 -85px;
  border-radius: 50%;
  background: #fff;
  border: 4px solid #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,0.28);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: transform 0.75s cubic-bezier(0.34, 1.4, 0.64, 1), opacity 0.5s ease;
}
.ava img {
  width: 82%;
  height: 82%;
  object-fit: contain;
}
.ava-left  { transform: translateX(-300px) rotate(-14deg); }
.ava-right { transform: translateX(300px)  rotate(14deg); }
.ava-left.show  { transform: translateX(-60px) rotate(-9deg); opacity: 1; }
.ava-right.show { transform: translateX(60px)  rotate(9deg);  opacity: 1; }

.match-sub {
  font-family: 'Roboto Mono', monospace;
  font-size: 0.95em;
  letter-spacing: 0.04em;
  max-width: 640px;
  text-align: center;
  line-height: 1.5;
  color: rgba(255,255,255,0.92);
  opacity: 0;
  transform: translateY(14px);
  transition: opacity 0.5s ease, transform 0.5s ease;
  transition-delay: 0.75s;
}
.match-sub.show { opacity: 1; transform: translateY(0); }
</style>

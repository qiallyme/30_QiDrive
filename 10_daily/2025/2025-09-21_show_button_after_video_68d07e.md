---
title: "Show button after video"
date: "2025-09-21"
created_at: "2025-09-21T22:41:04.190306+00:00"
conversation_id: "68d07ef4-88b4-8320-8ac9-7b737d822990"
tags:
  - ai_chat
  - export
---

# Show button after video

> **Date:** 2025-09-21 | **Conversation ID:** `68d07ef4-88b4-8320-8ac9-7b737d822990`

---

### **User**
how do i get a button on a site to show the video is over ot continue in dev.

---

### **Assistant**
Add a `video` event listener and toggle the button visibility/state when it ends. Example:  

```html
<video id="myVideo" controls>
  <source src="your-video.mp4" type="video/mp4">
</video>

<button id="continueBtn" style="display:none;">Continue</button>

<script>
const video = document.getElementById('myVideo');
const btn = document.getElementById('continueBtn');

video.addEventListener('ended', () => {
  btn.style.display = 'inline-block'; // show button
});

btn.addEventListener('click', () => {
  // do whatever "continue" means in dev
  console.log('Continuing...');
});
</script>
```

Key point: `video.addEventListener('ended', ...)` fires once playback finishes.  
Would you like me to make the button disabled instead of hidden until the video ends?

---

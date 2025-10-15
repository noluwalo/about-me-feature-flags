# LaunchDarkly SE Technical Exercise: about-me-feature-flags
 "About Me" site showing demoing LaunchDarkly feature flags (Setup instruction in Setup.md)


## Overview

As a **Senior Solutions Engineer**, the most important thing for me is to **"Wear the customers’ shoes"**. This means understanding who my customer is and what problem they need solved. I like to spend time in their world, see things from their perspective and design custom solutions/demos that earns trust through every interaction; solving real problems not just showing features **(#NotADemoMonkey)**. 

For this project I wanted to build and understand the process end-to-end, approaching it both as a Software Engineer and as a Solutions Engineer **(SE²)**! That meant **planning/whiteboarding**, **sketching flows**, **considering risk**, **designing the user experience**, and **understanding exactly** how LaunchDarkly fits into real-world engineering workflows and product decisions.

This repo isn’t just the final submission, it documents my thought process, trade-offs, debugging, and learnings along the way; so I can confidently articulate **how** and **why** these solutions provide value to customers.

To make things engaging (and fun), I built a small **"About Me" interactive site** and treated it like a **production feature rollout** with **flags, targeting, rollback, and experiments**.

This repo documents both **the build** and **the thought process**. A good SE doesnt just focus on **how** it works but also highlights the **value it creates/brings** to the customer.

---

## System Design Approach (Before Coding)

I began by outlining flows, thinking like a real delivery team and also thinking about how I would explain LD to a completely new user. By planning my steps thoughtfully, it allowed me to structure this repo from both a builder and a storyteller perspective.

### System Overview: How launch darkly works/communicates with a Website and Segement ###
<img width="2175" height="1097" alt="system Design Overview " src="https://github.com/user-attachments/assets/ecd5e557-de08-47f2-9d68-558c807f9bee" />


### Flags ### 
How in theory did I want these flags to work
**Flow 1 — Typewriter Animation** Release with instant rollback control 
<img width="848" height="916" alt="Flow1 Typewriter Animation (Release   Remediate)" src="https://github.com/user-attachments/assets/de207da3-ad0c-48ff-9488-4f0b3482dc56" />

**Flow 2 — Mode Toggle (Fun vs Professional)** Personalisation & targeting via context 
<img width="792" height="1045" alt="Flow2 Mode Toggle (Targeting)" src="https://github.com/user-attachments/assets/b254ab47-5cb7-4612-9346-431f1d5c7711" />


**Flow 3 — Surprise Me Button** Show experimentation & analytics impact ( A/B Testing + Segment integration )
<img width="834" height="1101" alt="flow3 suprise button (AB Experiment)" src="https://github.com/user-attachments/assets/2a9e4619-fec8-4387-8514-cbb7998af332" />


**UI Sketch Draft** 
How did i want the UI to look based on flags
<img width="1931" height="1118" alt="UI Sketch draft" src="https://github.com/user-attachments/assets/18af58a0-93d7-4c79-83eb-c6f4874a1ff0" />

---

## Feature Flags Implemented

| Flag | Purpose | Default / Variants | Functionality / Targeting | Risk / Goal |
|------|---------|--------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------|
| **typewriter-animation** | Animated typing effect for name display with pixel font styling | OFF (safe static text fallback) | Name appears character-by-character when ON | Medium (animation could affect performance) Instant rollback to static text if issues detected |
| **mode-toggle** | Switch between Professional vs Fun modes | Professional Mode / Fun Mode | Professional: Dark theme + work images Fun: Bright theme + hobbies  | Rule-based: Recruiters → Professional, Teammates → Fun; Context attributes: role, location, interest |
| **dynamic-content-widget** | A/B test experiment via "Surprise Me 🎲" button | Variant A / Variant B | Variant A: fantasy book recommendations; Variant B: personal fun facts | 50/50 traffic split; Metric: surprise_button_clicks tracked via Segment; Goal: determine which content type drives more engagement |


---

## How To Set Up
Setup instruction in Setup.md

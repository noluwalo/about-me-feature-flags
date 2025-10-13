# LaunchDarkly SE Technical Exercise: about-me-feature-flags
 "About Me" site showing demoing LaunchDarkly feature flags


## Overview

As a **Senior Solutions Engineer**, the most important thing for me is to **"Wear the customers’ shoes"**, understanding who my customer is and what problem they need solved. I spend time in their world, see things from their perspective, and design solutions that earns trust through every interaction, solving real problems not just showing features **(#NotADemoMonkey)**. 

For this project I wanted to build and understand end-to-end, approaching it both as a Software Engineer and as a Solutions Engineer **(SE²)**! That meant **planning/whiteboarding**, **sketching flows**, **considering risk**, **designing the user experience**, and **understanding exactly** how LaunchDarkly fits into real-world engineering workflows and product decisions.

This repo isn’t just the final submission, it documents my thought process, trade-offs, debugging, and learning along the way, so I can confidently articulate **how** and **why** these solutions provide value to engineering teams.

To make things engaging (and fun), I built a small **"About Me" interactive site** and treated it like a **production feature rollout** with **flags, targeting, rollback, and experiments**.

 This repo documents both **the build** and **the thought process**. A good SE doesnt just focus on **how** it works but also highlights the **value it creates/brings** to the customer.

---

## System Design Approach (Before Coding)

I began by outlining flows and thinking like a real delivery team and also how I would explain to a user completely new to LD. These planning steps helped me structure my thinking like both a builder and a storyteller.

### System Overview: How launch darkly works/communicates with a Website and Segement ###
<img width="2175" height="1097" alt="system Design Overview " src="https://github.com/user-attachments/assets/ecd5e557-de08-47f2-9d68-558c807f9bee" />


### Flags ### 
**Flow 1 — Typewriter Animation** Release with instant rollback control 
<img width="848" height="916" alt="Flow1 Typewriter Animation (Release   Remediate)" src="https://github.com/user-attachments/assets/de207da3-ad0c-48ff-9488-4f0b3482dc56" />

**Flow 2 — Mode Toggle (Fun vs Professional)** Personalisation & targeting via context 
<img width="792" height="1045" alt="Flow2 Mode Toggle (Targeting)" src="https://github.com/user-attachments/assets/b254ab47-5cb7-4612-9346-431f1d5c7711" />


**Flow 3 — Surprise Me Button** Show experimentation & analytics impact ( A/B Testing + Segment integration )
<img width="834" height="1101" alt="flow3 suprise button (AB Experiment)" src="https://github.com/user-attachments/assets/2a9e4619-fec8-4387-8514-cbb7998af332" />


**UI Sketch Draft** Layout + toggle and flag-driven behaviour 
<img width="1931" height="1118" alt="UI Sketch draft" src="https://github.com/user-attachments/assets/18af58a0-93d7-4c79-83eb-c6f4874a1ff0" />

---

## Feature Flags Implemented

| Flag | Purpose | Default / Variants | Functionality / Targeting | Risk / Goal |
|------|---------|--------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------|
| **typewriter-animation** | Animated typing effect for name display with pixel font styling | OFF (safe static text fallback) | Name appears character-by-character when ON | Medium (animation could affect performance) Instant rollback to static text if issues detected |
| **mode-toggle** | Switch between Professional vs Fun modes | Professional Mode / Fun Mode | Professional: Dark theme + work images Fun: Bright theme + hobbies  | Rule-based: Recruiters → Professional, Teammates → Fun; Context attributes: role, location, interest |
| **dynamic-content-widget** | A/B test experiment via "Surprise Me 🎲" button | Variant A / Variant B | Variant A: fantasy book recommendations; Variant B: personal fun facts | 50/50 traffic split; Metric: surprise_button_clicks tracked via Segment; Goal: determine which content type drives more engagement |


---

## Component Breakdown

###  Frontend (HTML/CSS/JavaScript)
- Typewriter animation (flag-controlled)
- Mode toggle button (professional vs fun content)
- Dynamic image/content cards
- 🎲 **Surprise Me** button (variants controlled by LD experiment flag)
- Debug panel for SE explanation/demo

---

## Segment Analytics Integration
Segment is used here to capture real-time user interactions with the feature flags. It lets us see what users actually do, which is critical for:

**Measuring impact**: Understand which content or mode engages users more (books vs fun facts, Professional vs Fun mode).

**Driving experiment**s: Feed metrics into LaunchDarkly to evaluate A/B tests and make data-driven decisions.

**Targeting audiences**: Segment Audiences can group users based on attributes such as role, location, or interests, which allows LaunchDarkly flags to deliver targeted experiences to specific groups without changing code.

**Transparency**: Pop-up notifications show exactly what’s being tracked, so it’s easy to follow along and debug.

**Customer insight**:Segment provides the analytics to see the experience/customer interactions from the user’s perspective.

Tracking the following events:

- `page_view`
- `Mode Toggle Clicked`
- `surprise_button_click`
- `typewriter_displayed`
- `debug_panel_viewed`
- `User Role Changed`
- `Identify Calls`

Events are also displayed as small **visual notifications** to make tracking transparent during demo sessions.

---

## how to set up

